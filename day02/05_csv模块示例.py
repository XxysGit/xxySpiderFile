import csv

with open("test.csv","a",newline="",encoding="gb18030") as f:
    # 创建写入对象
    writer = csv.writer(f)
    # 写入对象的writerow()写入csv文件
    writer.writerow(["旭哥",38])
    writer.writerow(["超哥哥",29])










