import csv
import os.path


def write_to_csv(csv_file, merged_dictionary):
    headers = False
    if not os.path.exists(csv_file):  # Create csv file
        headers = True
    with open(csv_file, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=merged_dictionary.keys())
        if headers:
            writer.writeheader()
        writer.writerow(merged_dictionary)  # Write values into csv
