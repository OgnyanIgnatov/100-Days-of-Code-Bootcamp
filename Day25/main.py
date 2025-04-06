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
print(data["temp"])