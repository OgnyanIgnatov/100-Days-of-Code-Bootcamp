import csv, pandas

# with open("./Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv("./Day25/weather_data.csv")

# temps = data["temp"].to_list()
# average_temp = 0
# for temp in temps:
#     average_temp += temp
# average_temp/=len(temps)
# print(f"{average_temp:.2f}")

# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])
# print(max_temp)

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
print(monday_temp*9/5 +32)