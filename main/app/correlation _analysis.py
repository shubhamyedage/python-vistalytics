# from os.path import join, expanduser
# from main.utils.file_utils import read_csv_file, write_csv_file, get_files
# from main.utils.tree_utils import get_income_statement_tree_structure, get_string
#
# root_path = join(expanduser('~'), "PycharmProjects", "python-vistalytics", "main", "source")
# path = join(root_path, "in", 'test_src')
#
#
# def compare(v1, v2):
#     a = 1 if (v1 == 0) else 0
#     b = 1 if (v2 == 0) else 0
#     return True if(a ^ b) == 1 else False
#
#
# file_list = get_files(path)
# for f in file_list:
#     key_list = []
#     change = []
#     percent_change = []
#     data = read_csv_file(path, f)
#
#     data.dropna(how='all')
#     data.fillna(0, inplace=True)
#     data.replace('(%)', '', inplace=True, regex=True)
#     if 'TTM' in data:
#         data = data.drop('TTM', 1)
#     data = data.transpose()
#     # write_csv_file(join(path, 'temp.csv'), temp_data)
#
#     tree = get_income_statement_tree_structure()
#     for i, v in data.iterrows():
#         if not tree.__contains__(get_string(i)):
#             print(i)
#             data.drop(i, inplace=True)
#
#     write_csv_file(join(path, 'out', 'temp.csv'), data)
#     # print(data.transpose())
#     # plt.matshow(data.transpose().corr())
#     # plt.show()
