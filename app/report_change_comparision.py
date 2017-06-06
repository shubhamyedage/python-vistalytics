# This module compares average change in entity with root and parent entity for given time period.

from os.path import join, expanduser
import common.constant as con
from utils.file_utils import FileUtils
from utils.math_utils import MathUtils
from utils.tree_structure import TreeStructure


class ReportChangeComparision:
    def __init__(self):
        self.tree_str = TreeStructure()
        self.tree = self.tree_str.tree
        self.report_choice = con.INCOME_STATEMENTS
        self.file_utils = FileUtils()
        self.math_utils = MathUtils()
        self.root_path = join(expanduser('~'), 'PycharmProjects', 'python-vistalytics', 'source')

    def _read_csv(self, resource_dir):
        src_dir_path = join(self.root_path, 'in', 'csv', resource_dir)
        files = self.file_utils.get_files(src_dir_path)
        data_list = []
        for f in files:
            data_list.append(self.file_utils.read_csv(src_dir_path, f))
        return data_list

    def _process_data(self, data_list):
        for data in data_list:
            if con.TTM in data.columns:
                data.drop(con.TTM, 1, inplace=True)
            for i, v in data.iterrows():
                if self.tree.__contains__(self.tree_str.get_string(i)):
                    node = self.tree.get_node(self.tree_str.get_string(i))
                    node.data = {con.VALUES: v.tolist()}

    def _process_tree(self):
        root_node = self.tree.get_node(self.tree.root)
        try:
            values = root_node.data[con.VALUES]
        except TypeError:
            dummy_list = self.tree.children(root_node.identifier)
            root_node.data = {con.VALUES: [(x + y + z) for x, y, z in
                                           zip(dummy_list[0].data[con.VALUES], dummy_list[1].data[con.VALUES],
                                               dummy_list[2].data[con.VALUES])]}

        for i in self.tree.all_nodes():
            i.data[con.AVERAGE_CHANGE] = self.math_utils.average_change(i.data[con.VALUES])
            slope, const = self.math_utils.get_linear_function_properties(i.data[con.VALUES])
            i.data[con.AVERAGE_PERCENTAGE_CHANGE] = self.math_utils.average_change(
                self.math_utils.merge_list_percentage(i.data[con.VALUES], root_node.data[con.VALUES]))
            i.data[con.SLOPE_VALUE] = slope
            i.data[con.CONSTANT_VALUE] = const

    def _print_text(self):
        root_node = self.tree.get_node(self.tree.root)
        print('##################################################')
        print('For time period 2012-2016 analysed: \n \n')
        for i in self.tree.all_nodes():
            indicator_str1 = con.RAISED if i.data[con.AVERAGE_CHANGE] > 0 else con.DROPPED
            if i.is_root():
                print('Index ' + i.identifier.upper() + ' has ' + indicator_str1 + ' by '
                      + str(i.data[con.AVERAGE_CHANGE]) + '\n \n')
                root_str = {con.KEY: i.identifier.upper(), con.AVERAGE_CHANGE: i.data[con.AVERAGE_CHANGE],
                            con.INDICATOR: indicator_str1}
            else:
                indicator_str2 = con.INCREASED if i.data[con.AVERAGE_PERCENTAGE_CHANGE] > 0 else con.REDUCED
                print('Index ' + i.identifier.upper() + ' has ' + indicator_str1 + ' by '
                      + str(i.data[con.AVERAGE_CHANGE]))
                print('While total ' + str(root_str.get(con.KEY)) + ' has ' + str(root_str.get(con.INDICATOR)) + ' '
                      + i.identifier.upper() + ' has ' + indicator_str2 + ' by '
                      + str(i.data[con.AVERAGE_PERCENTAGE_CHANGE]) + '%')

                # Trend comparision with root node
                indicator_str3 = 'in ' + con.OPPOSITE_DIRECTION if i.data[con.SLOPE_VALUE] < 0 \
                    else con.RAPIDLY if i.data[con.SLOPE_VALUE] > root_node.data[con.SLOPE_VALUE] else con.SLOWLY
                print('Index ' + i.identifier.upper() + ' is growing ' + indicator_str3 + ' with rate '
                      + str(i.data[con.SLOPE_VALUE]) + ' as compared to base index ' + root_node.identifier.upper()
                      + ' where growth rate is ' + str(root_node.data[con.SLOPE_VALUE]))

                # # Comparision with all sibling nodes
                # nid = i.identifier
                # sibling_node = tree.siblings(nid)
                # for n in sibling_node:
                #     indicator_str3 = con.RAPIDLY if i.data[con.SLOPE_VALUE] > n.data[con.SLOPE_VALUE] else con.SLOWLY
                #     print('Index ' + i.identifier.upper() + ' is growing ' + indicator_str3 + ' with rate ' +
                #           str(i.data[con.SLOPE_VALUE]) + ' as compared to base index ' +
                #           n.identifier.upper() + ' where growth rate is ' + str(n.data[con.SLOPE_VALUE]))
                print('\n \n')

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
        print(self.report_choice)
        print(self.tree)
        data_list = self._read_csv(self.report_choice)
        # print(data_list)
        self._process_data(data_list)
        # print(self.tree.to_json(with_data=True))
        self._process_tree()
        # print(self.tree.to_json(with_data=True))
        self._print_text()


if __name__ == '__main__':
    ReportChangeComparision().run()
