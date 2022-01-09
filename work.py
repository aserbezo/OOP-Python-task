import os.path
import json
from datetime import datetime
import csv


def check_time_format(format_check):
    try:
        time = datetime.strptime(format_check, "%Y-%m-%dT%H:%M:%S%z")
    except:
        time = format_check
    return time


def convert_temperatures(temp_check):
    temperatures = temp_check
    if "c" in temperatures:
        numbers = ""
        for i in temperatures:
            if i.isdigit():
                numbers += i
        numbers = int(numbers)
        # celsius to fahrenheit formula
        cover = ((9 / 5) * numbers + 32)
        result = f"{int(cover)}F"
        return result
    elif "f" in temperatures:
        number = ""
        for i in temperatures:
            if i.isdigit():
                number += i
        number = int(number)
        # fahrenheit to celsius formula
        cover_f = (number - 32) * 5 / 9
        result = f"{round(cover_f)}C"
        return result


def convert_time_local(date_input):
    time = check_time_format(date_input)
    old_date = str(time)
    old_date = old_date.split()
    curr_time = datetime.now()
    curr_time = str(curr_time.astimezone())
    new_time = curr_time.split()
    timezone = new_time[1]
    timezone = timezone[-6:]
    curr_time = new_time[1].split(".")
    curr_time = curr_time[0]
    result = old_date[0] + " " + curr_time + timezone
    return result


def convert_json_to_json(input_file, output_file):
    with open(input_file) as f:
        data = json.load(f)
        my_dict = []
        for key in data:
            data_dict = {"city": key['city'], "date": "", "temp": ""}
            date = key["date"]
            # calling function convert_time_local convert datetime
            date_convert = convert_time_local(date)
            data_dict["date"] = date_convert
            temp = str(key['temp'])
            temp = temp.lower()
            # calling function convert_temperatures
            temp_convert = convert_temperatures(temp)
            data_dict['temp'] = temp_convert
            my_dict.append(data_dict)
        f = open(output_file, "a", )
        json.dump(my_dict, f, indent=4)
        f.close()


def convert_json_to_csv(input_file, output_file):
    with open(input_file) as f:
        data = json.load(f)
        for key in data:
            my_lists = []
            my_lists.append(key["city"])
            convert_time = convert_time_local(key["date"])
            my_lists.append(convert_time)
            convert_temp = str(key["temp"]).lower()
            convert_temp = convert_temperatures(convert_temp)
            my_lists.append(convert_temp)
            f = open(output_file, "a")
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(my_lists)
            f.close()


def convert_csv_to_csv(input_file, output_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        for row in reader:
            my_lists = []
            my_lists.append(row[0])
            name = row[1].strip()
            my_lists.append(convert_time_local(name))
            temp = row[2].lower()
            my_lists.append(convert_temperatures(temp))
            f = open(output_file, "a")
            writer = csv.writer(f)
            writer.writerow(my_lists)
            f.close()


def convert_csv_to_json(input_file, output_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        my_list = []
        for row in reader:
            data_dict = {"city": row[0], "date": "", "temp": ""}
            current_time = row[1].strip()
            current_time = convert_time_local(current_time)
            data_dict["date"] = current_time
            temp = row[2].lower()
            temp = convert_temperatures(temp)
            data_dict["temp"] = temp
            my_list.append(data_dict)

        f = open(output_file, "w")
        json.dump(my_list, f, indent=4)
        f.close()


class ConvertText:
    def __init__(self, inputfilename, outputfilename):
        self.inputfilename = inputfilename
        self.outputfilename = outputfilename

    @classmethod
    def get_user_input(self):
        inputfilename = input("Please enter the name of input file: ")
        outputfilename = input("Please enter the name of output file: ")
        if ".json" in inputfilename or ".csv" in inputfilename:
            if os.path.isfile(inputfilename):
                inputfilename = inputfilename
            else:
                print(f"Sorry , there is no file associated with name {inputfilename}")
        else:
            print("Please choose .csv or .json file extension for input file!")

        if ".csv" in outputfilename or ".json" in outputfilename:
            outputfilename = outputfilename
        else:
            print("Please choose .csv or .json file extension for output file!")
        return self(inputfilename, outputfilename)

    def convert_files(self):
        if ".json" in self.inputfilename:
            return ConvertText.convert_json_files(self)
        elif ".csv" in self.inputfilename:
            return ConvertText.convert_csv_files(self)

    def convert_json_files(self):
        input_file = self.inputfilename
        output_file = self.outputfilename
        if ".json" in output_file:
            return convert_json_to_json(input_file, output_file)

        elif '.csv' in output_file:
            return convert_json_to_csv(input_file, output_file)

    def convert_csv_files(self):
        input_file = self.inputfilename
        output_file = self.outputfilename
        if ".csv" in self.outputfilename:
            return convert_csv_to_csv(input_file, output_file)
        elif ".json" in self.outputfilename:
            return convert_csv_to_json(input_file, output_file)


var = ConvertText.get_user_input()
check = ConvertText.convert_files(var)
