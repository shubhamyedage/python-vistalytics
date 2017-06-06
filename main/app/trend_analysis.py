from os.path import join, expanduser
from treelib import Tree
from main.utils.tree_utils import get_string, get_balance_statement_tree_structure, get_income_statement_tree_structure,\
    get_cash_flow_statement, report_choices
import main.common.constant as con
from main.utils.file_utils import get_files, read_csv_file
from main.utils.math_utils import average_change, merge_list_percentage, get_linear_function_properties, compare


root_path = join(expanduser('~'), 'PycharmProjects', 'python-vistalytics', 'main', 'source')
tree = Tree()


def read_csv(resource_dir):
    src_dir_path = join(root_path, 'in', 'csv', resource_dir)
    files = get_files(src_dir_path)
    data_list = []
    for f in files:
        data_list.append(read_csv_file(src_dir_path, f))

    return data_list


def process_data(data_list):
    for data in data_list:
        if con.TTM in data.columns:
            data.drop(con.TTM, 1, inplace=True)

        data.dropna(how='all')
        data.fillna(0, inplace=True)
        data.replace('(%)', '', inplace=True, regex=True)

        for i, v in data.iterrows():
            if tree.__contains__(get_string(i)):
                node = tree.get_node(get_string(i))
                node.data = {con.VALUES: v.tolist()}

    return


def process_tree():
    root_node = tree.get_node(tree.root)
    try:
        print(root_node.data[con.VALUES])
    except TypeError:
        dummy_list = tree.children(root_node.identifier)
        root_node.data = {con.VALUES: [(x + y + z) for x, y, z in
                                       zip(dummy_list[0].data[con.VALUES], dummy_list[1].data[con.VALUES],
                                           dummy_list[2].data[con.VALUES])], con.TAGGED: False}

    for i in tree.all_nodes():
        i.data[con.AVERAGE_CHANGE] = average_change(i.data[con.VALUES])
        slope, const = get_linear_function_properties(i.data[con.VALUES])
        i.data[con.AVERAGE_PERCENTAGE_CHANGE] = average_change(merge_list_percentage(i.data[con.VALUES],
                                                                                     root_node.data[con.VALUES]))
        i.data[con.SLOPE_VALUE] = slope
        i.data[con.CONSTANT_VALUE] = const
    return


def filter_nodes():
    node_id_list = []
    for node in tree.all_nodes():
        if not node.is_root():
            parent_node = tree.parent(node.identifier)
            if not compare(node.data[con.SLOPE_VALUE], parent_node.data[con.SLOPE_VALUE]) and not parent_node.data[con.TAGGED]:
                node.data[con.TAGGED] = True
                # print('###### Tagged Nodes: ' + node.identifier + ' data: ' + str(node.data))
                node_id_list.append(node.identifier)
            else:
                node.data[con.TAGGED] = False
                # print('Un-tagged Nodes: ' + node.identifier + ' data: ' + str(node.data))
    return node_id_list


def get_node_list_to_print(sub_tree):
    node_id_list = []
    sub_tree_root_node = sub_tree.get_node(sub_tree.root)
    for node in sub_tree.all_nodes():
        tree.get_node(node.identifier).data[con.TAGGED] = False
        if not node.is_root() and compare(node.data[con.SLOPE_VALUE], sub_tree_root_node.data[con.SLOPE_VALUE]):
            node_id_list.append(node.identifier)

    return node_id_list


def deep_compare_and_print(node_id_list):
    # root_node = tree.get_node(tree.root)
    # indicator_string = 'UP' if root_node.data[con.SLOPE_VALUE] > 0 else 'DOWN'
    for node_id in node_id_list:
        if tree.get_node(node_id).data[con.TAGGED]:
            sub_tree = tree.subtree(node_id)
            if sub_tree.depth() > 0:
                print_id_list = get_node_list_to_print(sub_tree)
                # print("##############################################")
                # print("While root index " + tree.root + " has gone " + indicator_string + ' by rate of ' +
                #       root_node.data[con.SLOPE_VALUE])
                #
                # if not sub_tree.get_node(sub_tree.root) is root_node:
                #     parent_node = sub_tree.get_node(sub_tree.root)
                #     print("While parent index " + parent_node.identifier +
                #               " is trending same as root index with rate of " + parent_node.data[con.SLOPE_VALUE])
                print(print_id_list)
                # print("##############################################")
            else:
                print(node_id)

    return


print("Choices :\n\n\tDefault: Income Statement\n\t1: Balance Statement\n\t2: Cash Flow Statement")
c = input()
report_choice = con.INCOME_STATEMENTS
try:
    report_choice = report_choices[int(c)]
    if report_choice is con.BALANCE_STATEMENTS:
        tree = get_balance_statement_tree_structure()
    else:
        tree = get_cash_flow_statement()

except KeyError:
    report_choice = con.INCOME_STATEMENTS
    tree = get_income_statement_tree_structure()
except ValueError:
    report_choice = con.INCOME_STATEMENTS
    tree = get_income_statement_tree_structure()


print(report_choice)
# Main Code
print(tree)
data_list = read_csv(report_choice)
# print(data_list)
process_data(data_list)
process_tree()
# print(tree.to_json(with_data=True))
node_id_list = filter_nodes()
deep_compare_and_print(node_id_list)
