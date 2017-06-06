from os.path import join, expanduser, splitext
import pandas as pd
from main.utils.file_utils import get_files, write_csv_file, read_csv_file
from main.utils.math_utils import average_change, percentage_change


root_path = join(expanduser("~"), "PycharmProjects", "python-vistalytics", "main", "source")


# main code
src_dir_path = join(root_path, "in", "annual")
file_list = get_files(src_dir_path)
for f in file_list:
    print(f)
    key_list = []
    avg_change_3_years_list = []
    percentage_change_3_years_list = []
    avg_change_5_years_list = []
    percentage_change_5_years_list = []
    data = read_csv_file(src_dir_path, f)

    if 'TTM' in data:
        data = data.drop('TTM', 1)

    for i, v in data.iterrows():
        # Prepare columns.
        size_val = len(v)
        change1 = percentage_change(v[size_val - 3], v[size_val - 1])
        change1 = 0 if change1 > 5 else change1
        change2 = percentage_change(v[size_val - 5], v[size_val - 1])
        change2 = 0 if change2 > 5 else change2
        if change2 is not 0 and change1 is not 0:
            key_list.append(i)
            avg_change_3_years_list.append(average_change(v[size_val - 3:]))
            percentage_change_3_years_list.append(change1)
            avg_change_5_years_list.append(average_change(v[size_val - 5:]))
            percentage_change_5_years_list.append(change2)

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
    output_dir_path = join(root_path, "out",
                           splitext(f)[0].replace(" ", "_") + "_i_Annual_Report.csv")
    write_csv_file(output_dir_path, output_data_frame)
