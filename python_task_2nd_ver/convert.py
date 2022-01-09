from all_functions import *

print("At beginning you can select between sample.csv and sample.json file")
inputFilename = input("Please enter the name of input file: ")
outputFilename = input("Please enter the name of output file: ")

# we use two help variables to save valid results
input_file = ""
output_file = ""
# we use statements and calling functions to check valid input and output
if check_input_file(inputFilename):
    # if is valid we check the existence of the file with function "file_existence".
    if file_existence(inputFilename):
        input_file = inputFilename
    else:
        print(f"Sorry , there is no file associated with name {inputFilename}")
else:
    print("Please choose .csv or .json file extension for input file!")
if check_output_name(outputFilename):
    output_file = outputFilename
else:
    print("Please choose .csv or .json file extension for output file!")


class ConvertText:
    def __init__(self, input_file_name, output_file_name):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    # method for converting the files depends on from user input and output
    def convert_files(self):
        if ".json" in self.input_file_name:

            if ".json" in self.output_file_name:

                return convert_json_to_json(self.input_file_name, self.output_file_name)

            elif ".csv" in self.output_file_name:

                return convert_json_to_csv(self.input_file_name, self.output_file_name)

        elif ".csv" in self.input_file_name:
            if ".json" in self.output_file_name:

                return convert_csv_to_json(self.input_file_name, self.output_file_name)

            elif ".csv" in self.output_file_name:

                return convert_csv_to_csv(self.input_file_name, self.output_file_name)


obj = ConvertText(input_file, output_file)

ConvertText.convert_files(obj)
