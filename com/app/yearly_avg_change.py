from os.path import join, expanduser, splitext
import pandas as pd
from com.utils.file_utils import read_file, write_file
from com.utils.math_utils import average_change, percentage_change

key_list = []
avg_change_3_years_list = []
percentage_change_3_years_list = []
avg_change_5_years_list = []
percentage_change_5_years_list = []


def process_list(a):
    avg_change_3_years_list.append(average_change(a[2:]))
    percentage_change_3_years_list.append(percentage_change(a[2], a[4]))
    avg_change_5_years_list.append(average_change(a[-5:]))
    percentage_change_5_years_list.append(percentage_change(a[0], a[4]))
    return


# main code
src_dir_path = join(expanduser("~"), "PycharmProjects", "python-vistalytics", "com", "src", "in")
file_list = read_file(src_dir_path)
for f in file_list:
    data = pd.read_csv(join(src_dir_path, f), header=1, index_col=0, na_values=0)
    for i, v in data.iterrows():
        key_list.append(i)
        process_list(v)
    raw_data = {'Keys': key_list,
                'Average Change Over Last 3 Years': avg_change_3_years_list,
                'Average Change Over Last 3 Years (%)': percentage_change_3_years_list,
                'Average Change Over Last 5 Years': avg_change_5_years_list,
                'Average Change Over Last 5 Years (%)': percentage_change_5_years_list}
    data = pd.DataFrame(raw_data, columns=['Keys', 'Average Change Over Last 3 Years',
                                                 'Average Change Over Last 3 Years (%)',
                                                 'Average Change Over Last 5 Years',
                                                 'Average Change Over Last 5 Years (%)'])
    output_dir_path = join(expanduser("~"), "PycharmProjects", "python-vistalytics", "com", "src", "out",
                           splitext(f)[0].replace(" ", "_") + "_Annual_Report.csv")
    write_file(output_dir_path, data)
