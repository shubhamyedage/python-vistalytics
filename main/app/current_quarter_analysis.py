from os.path import join, expanduser
from treelib import Tree
from main.utils.tree_utils import get_string, get_balance_statement_tree_structure, report_choices, \
    get_income_statement_tree_structure, get_cash_flow_statement
import main.common.constant as con
from main.utils.file_utils import get_files, read_csv_file

root_path = join(expanduser('~'), 'PycharmProjects', 'python-vistalytics', 'main', 'source')
tree = Tree()


def read_csv(resource_dir):
    src_dir_path = join(root_path, 'in', 'csv', resource_dir)
    files = get_files(src_dir_path)
    data_list = []
    for f in files:
        data_list.append(read_csv_file(src_dir_path, f))

    return data_list


def compare(v1, v2):
    a = 1 if (v1 == 0) else 0
    b = 1 if (v2 == 0) else 0
    return True if(a ^ b) == 1 else False


def process_data(data_list):
    for data in data_list:
        if con.TTM in data.columns:
            data.drop(con.TTM, 1, inplace=True)
        for i, v in data.iterrows():
            if tree.__contains__(get_string(i)):
                size_val = len(v)
                if compare(v[size_val - 2], v[size_val - 1]):
                    print("#############################################")
                    print("Index: " + i + " " + str(v[size_val - 2]) + " : " + str(v[size_val - 1]))

    return


print("Choices :\n\n\t1. Income Statement\n\t2. Balance Statement\n\t3. Cash Flow Statement")
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

data_list = read_csv(report_choice)
print(tree)
process_data(data_list)
