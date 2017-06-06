# This module lists average change and percentage change over time period.
# It reads quarterly data from  csv file.

from os.path import join, expanduser, splitext
import pandas as pd
from utils.file_utils import FileUtils
from utils.math_utils import MathUtils


class QuarterlyAverageChangeAnalysis(object):
    def __init__(self):
        self.root_path = join(expanduser('~'), "PycharmProjects", "python-vistalytics", "source")
        self.math_utils = MathUtils()
        self.file_utils = FileUtils()

    def run(self):
        path = join(self.root_path, "in", 'quarter')
        file_list = self.file_utils.get_files(path)
        for f in file_list:
            key_list = []
            change = []
            percent_change = []
            data = self.file_utils.read_csv(path, f)

            if 'TTM' in data:
                data = data.drop('TTM', 1)

            for i, v in data.iterrows():
                # Prepare Columns
                key_list.append(i)
                size_val = len(v)
                change.append(self.math_utils.get_change(v[size_val - 5], v[size_val - 1]))
                percent_change.append(self.math_utils.percentage_change(v[size_val - 5], v[size_val - 1]))

            # Write csv.
            output_data = {'Keys': key_list,
                           'Year Over Year Change': change,
                           'Year Over Year Change (%)': percent_change}

            output_data = pd.DataFrame(output_data, columns=['Keys', 'Year Over Year Change',
                                                             'Year Over Year Change (%)'])

            output_dir = join(self.root_path, 'out', splitext(f)[0].replace(" ", "_") + "_Quarterly_Report.csv")
            self.file_utils.write_csv(output_dir, output_data)

if __name__ == '__main__':
    QuarterlyAverageChangeAnalysis().run()