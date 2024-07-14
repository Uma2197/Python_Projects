# import csv
# # with open("./weather_data.csv") as data_file:
# #     data = data_file.readlines()
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# # data_dict = data.to_dict()
# # print(data_dict)
# # temp_list = data["temp"].to_list()
# # avg_temp = data["temp"].mean()
# max_temp = data.temp.max()
# # print(max_temp)
#
# print(data[data.temp == max_temp])
#
#
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240406.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



