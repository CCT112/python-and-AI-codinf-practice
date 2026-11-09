from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "財務分析"

ws["A1"] = "公司"
ws["B1"] = "ROE"

ws.append(["公司A", 0.08])
ws.append(["公司B", 0.12])
ws.append(["公司C", 0.06])

wb.save("financial_analysis.xlsx")

print("Excel 建立完成！")