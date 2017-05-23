from os import listdir
from os.path import join, isfile

def read_file(a):
    return [f for f in listdir(a) if isfile(join(a, f))]


def write_file(path, data):
    data.to_csv(path, index=False)
    return