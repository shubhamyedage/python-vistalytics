# This module lists average change and percentage change over time period.
# It reads yearly data from  csv file.

from os.path import join, expanduser, splitext
import pandas as pd
from utils.file_utils import FileUtils
from utils.math_utils import MathUtils


class YearlyAverageChangeAnalysis(object):
    def __init__(self):
        self.root_path = join(expanduser("~"), "PycharmProjects", "python-vistalytics", "source")
        self.file_utils = FileUtils()
        self.math_utils = MathUtils()

    def run(self):
        src_dir_path = join(self.root_path, "in", "annual")
        file_list = self.file_utils.get_files(src_dir_path)

        for f in file_list:
            key_list = []
            avg_change_3_years_list = []
            percentage_change_3_years_list = []
            avg_change_5_years_list = []
            percentage_change_5_years_list = []
            data = self.file_utils.read_csv(src_dir_path, f)
            if 'TTM' in data:
                data = data.drop('TTM', 1)
            for i, v in data.iterrows():
                # Prepare columns.
                size_val = len(v)
                key_list.append(i)
                avg_change_3_years_list.append(self.math_utils.average_change(v[size_val - 3:]))
                percentage_change_3_years_list.append(self.math_utils.percentage_change(v[size_val - 3],
                                                                                        v[size_val - 1]))
                avg_change_5_years_list.append(self.math_utils.average_change(v[size_val - 5:]))
                percentage_change_5_years_list.append(self.math_utils.percentage_change(v[size_val - 5],
                                                                                        v[size_val - 1]))

            # Write to csv.
            output_data = {'Keys': key_list,
                           'Average Change Over Last 3 Years': avg_change_3_years_list,
                           'Average Change Over Last 3 Years (%)': percentage_change_3_years_list,
                           'Average Change Over Last 5 Years': avg_change_5_years_list,
                           'Average Change Over Last 5 Years (%)': percentage_change_5_years_list}
            output_data_frame = pd.DataFrame(output_data, columns=['Keys', 'Average Change Over Last 3 Years',
                                                                   'Average Change Over Last 3 Years (%)',
                                                                   'Average Change Over Last 5 Years',
                                                                   'Average Change Over Last 5 Years (%)'])
            output_dir_path = join(self.root_path, "out",
                                   splitext(f)[0].replace(" ", "_") + "_Annual_Report.csv")
            self.file_utils.write_csv(output_dir_path, output_data_frame)

if __name__ == "__main__":
    YearlyAverageChangeAnalysis().run()
