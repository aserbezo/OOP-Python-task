from functions import convert_json_to_json
from functions import convert_json_to_csv




class ConvertJsonsFile:
    def __init__(self, json_input, output_file):
        self.json_input = json_input
        self.output_file = output_file

    def convert_file(self):
        # if output file is with json extension we are calling functions to convert json to json
        if ".json" in self.output_file:
            return convert_json_to_json(self.json_input, self.output_file)
        # if output file is with csv extension we are calling the functions to convert json to csv
        elif ".csv" in self.output_file:
            return convert_json_to_csv(self.json_input, self.output_file)
