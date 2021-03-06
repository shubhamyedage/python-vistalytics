# This module lists average change for last 3 years and 5 years, percentage change for last 3 years and 5 years, mean
# and deviation of each entity. Entity with more than 5% change are listed.
# It reads data from excel file.

from os.path import join, expanduser, splitext
import pandas as pd
from utils.file_utils import FileUtils
from utils.math_utils import MathUtils


class ReportOutlierDetection(object):
    def __init__(self):
        self.root_path = join(expanduser("~"), "PycharmProjects", "python-vistalytics", "source")
        self.ignore_keys = ['Margins % of Sales', 'Profitability', 'Cash Flow Ratios', 'Balance Sheet Items (in %)',
                            'Liquidity/Financial Health', 'Efficiency']
        self.sheet_list = ['Income_Statement', 'Balance_Sheet', 'Cash_Flow_Statement', 'Key_Ratios']
        self.math_utils = MathUtils()
        self.file_utils = FileUtils()

    def _process_data(self, values, v):
        std_dev = self.math_utils.get_std_dev(values)
        mean_val = self.math_utils.get_mean(values)
        if 0 < 3 * std_dev < abs(v - mean_val):
            return std_dev, mean_val
        return 0, 0

    def run(self):
        src_dir_path = join(self.root_path, "in", "combined")
        file_list = self.file_utils.get_files(src_dir_path)
        for f in file_list:
            data = self.file_utils.read_excel(src_dir_path, f, [0, 1, 2, 3])
            for j in range(0, 4):
                avg_change_3_years_list = []
                percentage_change_3_years_list = []
                avg_change_5_years_list = []
                percentage_change_5_years_list = []
                dev_list = []
                mean_list = []
                temp = data.get(j)
                if 'TTM' in temp:
                    temp = temp.drop('TTM', 1)
                temp.fillna(0, inplace=True)
                temp.replace('(%)', '', inplace=True, regex=True)

                for i, v in temp.iterrows():
                    size_val = len(v)
                    if not pd.isnull(i) and i not in self.ignore_keys and size_val is not 0:
                        v = [float(x) for x in v]
                        # Get mean and deviation
                        x, y = self._process_data(v[0:size_val-2], v[size_val - 1])
                        dev_list.append(x)
                        mean_list.append(y)

                        # Get average and percentage for 3 and 5 years.
                        val1 = self.math_utils.percentage_change(0 if x is 0 else v[size_val - 3], v[size_val - 1])
                        val2 = self.math_utils.percentage_change(0 if x is 0 else v[size_val - 5], v[size_val - 1])
                        avg_change_3_years_list.append(0 if abs(val1) < 5
                                                            else self.math_utils.average_change(v[len(v) - 3:]))
                        percentage_change_3_years_list.append(val1)
                        avg_change_5_years_list.append(0 if abs(val2) < 5
                                                            else self.math_utils.average_change(v[size_val - 5:]))
                        percentage_change_5_years_list.append(val2)
                        print("################################")
                        print("For Index: " + i + " Last change " + str(v[size_val-1]) + " is outlier.")
                    else:
                        avg_change_3_years_list.append(0)
                        percentage_change_3_years_list.append(0)
                        avg_change_5_years_list.append(0)
                        percentage_change_5_years_list.append(0)
                        dev_list.append(0)
                        mean_list.append(0)

                temp.insert(len(temp.columns), 'Deviation', dev_list)
                temp.insert(len(temp.columns), 'Mean', mean_list)
                temp.insert(len(temp.columns), 'Average Change Over Last 3 Years', avg_change_3_years_list)
                temp.insert(len(temp.columns), 'Average Change Over Last 3 Years (%)',
                            percentage_change_3_years_list)
                temp.insert(len(temp.columns), 'Average Change Over Last 5 Years',
                            avg_change_5_years_list)
                temp.insert(len(temp.columns), 'Average Change Over Last 5 Years (%)',
                            percentage_change_5_years_list)

                # print(temp)
                out_src_dir = join(self.root_path, 'out', splitext(f)[0].replace(" ", "_") + "_Combined_Report.xlsx")
                self.file_utils.write_excel(out_src_dir, temp, self.sheet_list[j])

if __name__ == '__main__':
    ReportOutlierDetection().run()
