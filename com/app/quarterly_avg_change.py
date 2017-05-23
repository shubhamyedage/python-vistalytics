from os.path import join, expanduser, splitext
import pandas as pd
from com.utils.file_utils import read_file, write_file
from com.utils.math_utils import get_change, percentage_change


root_path = join(expanduser('~'), "PycharmProjects", "python-vistalytics", "com", "src")

path = join(root_path, "in", 'quarter')
file_list = read_file(path)
for f in file_list:
    print(f)
    key_list = []
    change = []
    percent_change = []
    data = pd.read_csv(join(path, f), header=1, index_col=0, na_values=0)
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

    output_data_frame = pd.DataFrame(output_data, columns=['Keys', 'Year Over Year Change',
                                                             'Year Over Year Change (%)'])

    output_dir = join(root_path, 'out', splitext(f)[0].replace(" ", "_") + "_Quarterly_Report.csv")
    write_file(output_dir, output_data_frame)