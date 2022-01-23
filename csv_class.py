from functions import convert_csv_to_csv
from functions import convert_csv_to_json


class ConvertCsvFile:
    def __init__(self, csv_input, output_file):
        self.csv_input = csv_input
        self.output_file = output_file

    def convert_file(self):
        # if json file extension is in output name we are calling functions  to convert csv to json
        if ".json" in self.output_file:
            return convert_csv_to_json(self.csv_input, self.output_file)
        # if csv file extension is in output name we are calling functions  to convert csv to json
        elif ".csv" in self.output_file:
            return convert_csv_to_csv(self.csv_input, self.output_file)
