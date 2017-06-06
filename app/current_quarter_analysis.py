# This module looks for entities with non-zero values in current year/quarter
# and zero values in last year and vice-versa.

from os.path import join, expanduser
from treelib import Tree
from utils.tree_structure import TreeStructure
import common.constant as con
from utils.file_utils import FileUtils


class CurrentQuarterAnalysis(object):
    def __init__(self):
        self.root_path = join(expanduser('~'), 'PycharmProjects', 'python-vistalytics', 'source')
        self.tree = Tree()
        self.tree_str = TreeStructure()
        self.file_utils = FileUtils()
        self.report_choice = con.INCOME_STATEMENTS

    def _read_csv(self, resource_dir):
        src_dir_path = join(self.root_path, 'in', 'csv', resource_dir)
        files = self.file_utils.get_files(src_dir_path)
        data_list = []
        for f in files:
            data_list.append(self.file_utils.read_csv(src_dir_path, f))
        return data_list

    def _compare(self, v1, v2):
        a = 1 if (v1 == 0) else 0
        b = 1 if (v2 == 0) else 0
        return True if(a ^ b) == 1 else False

    def process_data(self, data_list):
        for data in data_list:
            if con.TTM in data.columns:
                data.drop(con.TTM, 1, inplace=True)
            for i, v in data.iterrows():
                if self.tree.__contains__(self.tree_str.get_string(i)):
                    size_val = len(v)
                    if self._compare(v[size_val - 2], v[size_val - 1]):
                        print("#############################################")
                        print("Index: " + i + " " + str(v[size_val - 2]) + " : " + str(v[size_val - 1]))

    def run(self):
        print("Choices :\n\n\tDefault: Income Statement\n\t1: Balance Statement\n\t2: Cash Flow Statement")
        c = input()
        try:
            self.report_choice = self.tree_str.report_choices[int(c)]
            if self.report_choice is con.BALANCE_STATEMENTS:
                self.tree_str.get_balance_tree()
            else:
                self.tree_str.get_cash_flow_tree()
        except KeyError:
            self.report_choice = con.INCOME_STATEMENTS
            self.tree_str.get_income_tree()
        except ValueError:
            self.report_choice = con.INCOME_STATEMENTS
            self.tree_str.get_income_tree()
        self.tree = self.tree_str.tree
        data_list = self._read_csv(self.report_choice)
        print(self.tree)
        self.process_data(data_list)


if __name__ == '__main__':
    CurrentQuarterAnalysis().run()
