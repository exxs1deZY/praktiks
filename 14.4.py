import openpyxl

nums = (28, -144, 50, 831, 72, 140, 90, 120)

max_num = 0

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet["A1"] = f"Самое большое число, кратное 5, в кортеже: {max_num}"
workbook.save("output.xlsx")

workbook = openpyxl.load_workbook("output.xlsx")
sheet = workbook.active
content = sheet["A1"].value
print(content)
