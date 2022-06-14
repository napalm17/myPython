import csv
from string import ascii_lowercase
from base_conversion import list_to_str, base10_to_N, letters_dict

def execute(input_num, base):
    number_arr = base10_to_N(input_num, base, l=[0])
    for j in range(len(number_arr)):
        number_arr[j] = letters_dict[number_arr[j]] if number_arr[j] >= 10 else number_arr[j]
    output_num = list_to_str(number_arr)
    return output_num

def write_csv():
    csv_file = open("base_convert/table_long.csv","w")
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow([f"base {x}" for x in range(2, 17)])

    for num in range(10000):
        arr = []
        for base in range(2, 17):
            arr.append(execute(num, base))
        csv_writer.writerow(arr)
    csv_file.close()
write_csv()