


print("XlsMerger")
print()

import pip
pip.main(['install', "xlrd"])
pip.main(['install', "xlwt"])



import os
import xlrd
# https://xlrd.readthedocs.io/en/latest/api.html """
import xlwt

print()

write_book = xlwt.Workbook()
write_file_name = "db.xls"
partnumber_file_name = "pn.list"

read_file_count = 0
read_sheet_count = 0

pn_values = []

with open("XlsMerger.txt", "w") as text_file:


    for read_file_name in os.listdir(os.getcwd()):

        if read_file_name.endswith(".xls") and not read_file_name == write_file_name:

            text_file.write("\n")
            text_file.write("info: reading file \'{0}\'\n".format(read_file_name))

            read_file_count += 1
            read_book = xlrd.open_workbook(read_file_name,formatting_info=True)

            for sheet_index in range(len(read_book.sheets())):

                read_sheet = read_book.sheet_by_index(sheet_index)
                read_sheet_count += 1
                read_sheet_name = read_sheet.name

                text_file.write("info: reading sheet \'{0}\' ({1} rows)\n".format(read_sheet_name, read_sheet.nrows))

                write_sheet_name = read_file_name.split(".xls")[0] + " - " + read_sheet_name

                text_file.write("info: writing sheet \'{0}\'\n".format(write_sheet_name))

                try:
                    write_sheet = write_book.add_sheet(write_sheet_name)
                except Exception:
                    print("FATAL: invalid sheet name", write_sheet_name)
                    input("press ENTER to quit")
                    quit()
                

                text_file.write("info: cells per row = {0}\n".format([len(read_sheet.row_values(row)) for row in range(read_sheet.nrows)]))

                for row_index in range(read_sheet.nrows):
                    for col_index, read_value in zip(range(len(read_sheet.row_values(row_index))), read_sheet.row_values(row_index)):
                        write_sheet.write(row_index, col_index, read_value)

                    pn_value = read_sheet.row_values(row_index)[0]
                    if row_index != 0 and pn_value != "":
                        pn_values.append(pn_value)


                pass
            pass
        pass
    pass

    partnumber_file = open(partnumber_file_name, "w")
    pn_values_sorted = sorted(pn_values)
    partnumber_file.write("(total "+str(len(pn_values_sorted))+" parts)"+"\n\n")
    for pn_value in pn_values_sorted:
        partnumber_file.write(pn_value + "\n")
    partnumber_file.close()
pass

try:
    write_book.save(write_file_name)
except PermissionError:
    print("FATAL: Permission Error, unable to write to ", write_file_name)
    input("press ENTER to quit")
    quit()

print()
print("info:", "total", read_file_count, "files were read")
print("info:", "total", read_sheet_count, "sheets were read")

print()
input("press ENTER to quit")

