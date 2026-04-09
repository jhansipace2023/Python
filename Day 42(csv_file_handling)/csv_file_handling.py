#example for w and a without with statement
# import csv
# file=open('pythonE18.csv','w',newline='')
# writer=csv.writer(file)
# writer.writerow(['ename','sal','deptno'])
# writer.writerows([['allen',900,10],['smith',5000,20]])
# file.close()

# example for w and a using with statement
# import csv
# with open('pythonE18.csv','w',newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(['ename','sal','deptno'])
#     writer.writerows([['allen',900,10],['smith',5000,20]])

# # example for r without with statement
# import csv
# file=open('pythonE18.csv','r')
# reader=csv.reader(file)
# for row in reader:
#     print(row)
# file.close()

# # example for r using with statement
# import csv
# with open('pythonE18.csv','r') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)

# example for w+ and a+ without with statement
# import csv
# file=open('pythonE18.csv','w+',newline='')
# writer=csv.writer(file)
# writer.writerow(['ename','sal','deptno'])
# writer.writerow(['allen',900,10])
# file.seek(0)
# reader=csv.reader(file)
# for row in reader:
#     print(row)
# file.close()

# example for w+ and a+ using with statement
# import csv
# with open('pythonE18.csv','w+',newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(['ename','sal','deptno'])
#     writer.writerows([['allen',900,10],['smith',5000,20]])
#     file.seek(0)
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)

#  example for r+ without with statement
# import csv
# file=open('pythonE18.csv','r+')
# reader=csv.reader(file)
# for row in reader:
#     print(row)
# writer=csv.writer(file)
# writer.writerow(['allen',900,20])
# file.close()

# example for r+ using statement
import csv
with open('pythonE18.csv','r+') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
    writer=csv.writer(file)
    writer.writerow(['smith',500,20])