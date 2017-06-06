from os.path import join, expanduser, splitext
import pandas as pd
from main.utils.file_utils import read_csv_file, write_csv_file, get_files
from main.utils.math_utils import get_change, percentage_change


root_path = join(expanduser('~'), "PycharmProjects", "python-vistalytics", "main", "source")

path = join(root_path, "in", 'quarter')
file_list = get_files(path)
for f in file_list:
    print(f)
    key_list = []
    change = []
    percent_change = []
    data = read_csv_file(path, f)

    if 'TTM' in data:
        data = data.drop('TTM', 1)

    for i, v in data.iterrows():
        # Prepare Columns
        key_list.append(i)
        size_val = len(v)
        change.append(get_change(v[size_val - 5], v[size_val - 1]))
        percent_change.append(percentage_change(v[size_val - 5], v[size_val - 1]))

    # Write csv.
    output_data = {'Keys': key_list,
                   'Year Over Year Change': change,
                   'Year Over Year Change (%)': percent_change}

    output_data = pd.DataFrame(output_data, columns=['Keys', 'Year Over Year Change', 'Year Over Year Change (%)'])

    output_dir = join(root_path, 'out', splitext(f)[0].replace(" ", "_") + "_k_Quarterly_Report.csv")
    write_csv_file(output_dir, output_data)
