# This module looks for trend between matrices and highlights matrices with opposite trend with respect to root node.

from os.path import join, expanduser
from utils.tree_structure import TreeStructure
import common.constant as con
from utils.file_utils import FileUtils
from utils.math_utils import MathUtils


class TrendAnalysis(object):
    def __init__(self):
        self.tree = TreeStructure().tree
        self.root_path = join(expanduser('~'), 'PycharmProjects', 'python-vistalytics', 'source')
        self.tree_str = TreeStructure()

    def _read_csv(self, resource_dir):
        src_dir_path = join(self.root_path, 'in', 'csv', resource_dir)
        files = FileUtils().get_files(src_dir_path)
        data_list = []
        for f in files:
            data_list.append(FileUtils().read_csv(src_dir_path, f))
        return data_list

    def _process_data(self, data_list):
        for data in data_list:
            if con.TTM in data.columns:
                data.drop(con.TTM, 1, inplace=True)

            data.dropna(how='all')
            data.fillna(0, inplace=True)
            data.replace('(%)', '', inplace=True, regex=True)

            for i, v in data.iterrows():
                if self.tree.__contains__(TreeStructure().get_string(i)):
                    node = self.tree.get_node(TreeStructure().get_string(i))
                    node.data = {con.VALUES: v.tolist()}

    def _process_tree(self):
        root_node = self.tree.get_node(self.tree.root)
        try:
            print(root_node.data[con.VALUES])
        except TypeError:
            dummy_list = self.tree.children(root_node.identifier)
            root_node.data = {con.VALUES: [(x + y + z) for x, y, z in
                                           zip(dummy_list[0].data[con.VALUES], dummy_list[1].data[con.VALUES],
                                               dummy_list[2].data[con.VALUES])], con.TAGGED: False}

        for i in self.tree.all_nodes():
            i.data[con.AVERAGE_CHANGE] = MathUtils().average_change(i.data[con.VALUES])
            slope, const = MathUtils().get_linear_function_properties(i.data[con.VALUES])
            i.data[con.AVERAGE_PERCENTAGE_CHANGE] = MathUtils().average_change(MathUtils().merge_list_percentage(
                i.data[con.VALUES], root_node.data[con.VALUES]))
            i.data[con.SLOPE_VALUE] = slope
            i.data[con.CONSTANT_VALUE] = const

    def _filter_nodes(self):
        node_id_list = []
        for node in self.tree.all_nodes():
            if not node.is_root():
                parent_node = self.tree.parent(node.identifier)
                if not MathUtils().compare(node.data[con.SLOPE_VALUE], parent_node.data[con.SLOPE_VALUE]) and\
                        not parent_node.data[con.TAGGED]:
                    node.data[con.TAGGED] = True
                    # print('###### Tagged Nodes: ' + node.identifier + ' data: ' + str(node.data))
                    node_id_list.append(node.identifier)
                else:
                    node.data[con.TAGGED] = False
                    # print('Un-tagged Nodes: ' + node.identifier + ' data: ' + str(node.data))
        return node_id_list

    def _get_node_list(self, sub_tree):
        node_id_list = []
        sub_tree_root_node = sub_tree.get_node(sub_tree.root)
        for node in sub_tree.all_nodes():
            self.tree.get_node(node.identifier).data[con.TAGGED] = False
            if not node.is_root() and MathUtils().compare(node.data[con.SLOPE_VALUE],
                                                          sub_tree_root_node.data[con.SLOPE_VALUE]):
                node_id_list.append(node.identifier)
        return node_id_list

    def _deep_compare(self, node_id_list):
        # root_node = self.tree.get_node(self.tree.root)
        # indicator_string = 'UP' if root_node.data[con.SLOPE_VALUE] > 0 else 'DOWN'
        for node_id in node_id_list:
            if self.tree.get_node(node_id).data[con.TAGGED]:
                sub_tree = self.tree.subtree(node_id)
                print("##############################################")
                if sub_tree.depth() > 0:
                    print_id_list = self._get_node_list(sub_tree)
                    # print("While root index " + self.tree.root + " has gone " + indicator_string + ' by rate of ' +
                    #       str(root_node.data[con.SLOPE_VALUE]))
                    #
                    # if not sub_tree.get_node(sub_tree.root) is root_node:
                    #     parent_node = sub_tree.get_node(sub_tree.root)
                    #     print("While parent index " + parent_node.identifier +
                    #           " is trending same as root index with rate of " +
                    #           str(parent_node.data[con.SLOPE_VALUE]))
                    print(print_id_list)
                else:
                    print(node_id)

    def run(self):
        print("Choices :\n\n\tDefault: Income Statement\n\t1: Balance Statement\n\t2: Cash Flow Statement")
        c = input()
        try:
            report_choice = self.tree_str.report_choices[int(c)]
            if report_choice is con.BALANCE_STATEMENTS:
                self.tree_str.get_balance_tree()
            else:
                self.tree_str.get_cash_flow_tree()

        except KeyError:
            report_choice = con.INCOME_STATEMENTS
            self.tree_str.get_income_tree()
        except ValueError:
            report_choice = con.INCOME_STATEMENTS
            self.tree_str.get_income_tree()

        self.tree = self.tree_str.tree
        print(report_choice)
        print(self.tree)
        data_list = self._read_csv(report_choice)
        # print(data_list)
        self._process_data(data_list)
        self._process_tree()
        # print(self.tree.to_json(with_data=True))
        node_id_list = self._filter_nodes()
        self._deep_compare(node_id_list)

if __name__ == '__main__':
    TrendAnalysis().run()
