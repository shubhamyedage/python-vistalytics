from os.path import join, expanduser
import main.common.constant as con
from main.utils.file_utils import get_files, read_csv_file
from main.utils.math_utils import average_change, merge_list_percentage, get_linear_function_properties
from main.utils.tree_utils import get_string, get_income_statement_tree_structure, get_cash_flow_statement, \
    report_choices, get_balance_statement_tree_structure

root_path = join(expanduser('~'), 'PycharmProjects', 'python-vistalytics', 'main', 'source')


def read_csv(resource_dir):
    src_dir_path = join(root_path, 'in', 'csv', resource_dir)
    files = get_files(src_dir_path)
    data_list = []
    for f in files:
        data_list.append(read_csv_file(src_dir_path, f))

    return data_list


def process_data(data_list, tree):
    for data in data_list:
        if con.TTM in data.columns:
            data.drop(con.TTM, 1, inplace=True)

        for i, v in data.iterrows():
            if tree.__contains__(get_string(i)):
                node = tree.get_node(get_string(i))
                node.data = {con.VALUES: v.tolist()}

    return tree


def process_tree(tree):
    root_node = tree.get_node(tree.root)
    try:
        print(root_node.data[con.VALUES])
    except TypeError:
        dummy_list = tree.children(root_node.identifier)
        root_node.data = {con.VALUES: [(x + y + z) for x, y, z in
                                       zip(dummy_list[0].data[con.VALUES], dummy_list[1].data[con.VALUES],
                                           dummy_list[2].data[con.VALUES])]}

    for i in tree.all_nodes():
        i.data[con.AVERAGE_CHANGE] = average_change(i.data[con.VALUES])
        slope, const = get_linear_function_properties(i.data[con.VALUES])
        i.data[con.AVERAGE_PERCENTAGE_CHANGE] = average_change(merge_list_percentage(i.data[con.VALUES],
                                                                                     root_node.data[con.VALUES]))
        i.data[con.SLOPE_VALUE] = slope
        i.data[con.CONSTANT_VALUE] = const
    return tree


def print_text(tree):
    root_node = tree.get_node(tree.root)
    print('##################################################')
    print('For time period 2012-2016 analysed: \n \n')
    for i in tree.all_nodes():
        indicator_str1 = con.RAISED if i.data[con.AVERAGE_CHANGE] > 0 else con.DROPPED
        if i.is_root():
            print('Index ' + i.identifier.upper() + ' has ' + indicator_str1 + ' by '
                  + str(i.data[con.AVERAGE_CHANGE]) + '\n \n')
            root_str = {con.KEY: i.identifier.upper(), con.AVERAGE_CHANGE: i.data[con.AVERAGE_CHANGE],
                        con.INDICATOR: indicator_str1}
        else:
            indicator_str2 = con.INCREASED if i.data[con.AVERAGE_PERCENTAGE_CHANGE] > 0 else con.REDUCED
            print('Index ' + i.identifier.upper() + ' has ' + indicator_str1 + ' by ' + str(i.data[con.AVERAGE_CHANGE]))
            print('While total ' + str(root_str.get(con.KEY)) + ' has ' + str(root_str.get(con.INDICATOR)) + ' '
                  + i.identifier.upper() + ' has ' + indicator_str2 + ' by ' +
                  str(i.data[con.AVERAGE_PERCENTAGE_CHANGE]) + '%')

            # Trend comparision with root node
            indicator_str3 = 'in ' + con.OPPOSITE_DIRECTION if i.data[con.SLOPE_VALUE] < 0 else con.RAPIDLY if i.data[con.SLOPE_VALUE] > root_node.data[con.SLOPE_VALUE] else con.SLOWLY
            print('Index ' + i.identifier.upper() + ' is growing ' + indicator_str3 + ' with rate ' +
                  str(i.data[con.SLOPE_VALUE]) + ' as compared to base index ' + root_node.identifier.upper() +
                  ' where growth rate is ' + str(root_node.data[con.SLOPE_VALUE]))

            # Comparision with all sibling nodes
            # nid = i.identifier
            # sibling_node = tree.siblings(nid)
            # for n in sibling_node:
            #     indicator_str3 = con.RAPIDLY if i.data[con.SLOPE_VALUE] > n.data[con.SLOPE_VALUE] else con.SLOWLY
            #     print('Index ' + i.identifier.upper() + ' is growing ' + indicator_str3 + ' with rate ' +
            #           str(i.data[con.SLOPE_VALUE]) + ' as compared to base index ' +
            #           n.identifier.upper() + ' where growth rate is ' + str(n.data[con.SLOPE_VALUE]))

            print('\n \n')
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
print(data_list)
tree = process_data(data_list, tree)
# print(tree.to_json(with_data=True))
tree = process_tree(tree)
# print(tree.to_json(with_data=True))
print_text(tree)
