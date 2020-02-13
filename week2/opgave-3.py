import csv
import platform
import argparse

parser = argparse.ArgumentParser(
    description="print content from csv file in terminal or copy to another file")

parser.add_argument('-i', '--input-file', type=str,
                    required=True, help="file with content to copy")
parser.add_argument('-f', '--file-name', type=str,
                    required=False, help="name of the target file")


def read_csv(input_file, file_name=None):
    file_list = []
    with open(input_file) as file:
        reader = csv.reader(file)
        for row in reader:
            file_list.append(row)
    if file_name == None:
        print(file_list)
    else:
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            for line in file_list:
                writer.writerow(line)


arguments = parser.parse_args()
read_csv(arguments.input_file, arguments.file_name)
