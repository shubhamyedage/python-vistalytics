# # This module gives correlation of metrics
# # Not Completed.
#
# from os.path import join, expanduser
# from utils.file_utils import FileUtils
# from utils.tree_structure import TreeStructure
#
#
# class CorrelationAnalysis:
#     def __init__(self):
#         self.root_path = join(expanduser('~'), "PycharmProjects", "python-vistalytics", "source")
#         self.file_utils = FileUtils()
#         self.tree_str = TreeStructure()
#
#     def _compare(self, v1, v2):
#         a = 1 if (v1 == 0) else 0
#         b = 1 if (v2 == 0) else 0
#         return True if(a ^ b) == 1 else False
#
#     def run(self):
#         path = join(self.root_path, "in", "test_src")
#         file_list = self.file_utils.get_files(path)
#         for f in file_list:
#             data = self.file_utils.read_csv(path, f)
#             if 'TTM' in data:
#                 data = data.drop('TTM', 1)
#             data = data.transpose()
#             # write_csv_file(join(path, 'temp.csv'), temp_data)
#
#             tree = self.tree_str.get_income_tree()
#             for i, v in data.iterrows():
#                 if not tree.__contains__(self.file_utils.get_string(i)):
#                     print(i)
#                     data.drop(i, inplace=True)
#
#             self.file_utils.write_csv(join(path, 'out', 'temp.csv'), data)
#             # print(data.transpose())
#             # plt.matshow(data.transpose().corr())
#             # plt.show()
