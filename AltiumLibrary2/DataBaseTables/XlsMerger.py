


def console_friendly(text):
    import sys
    return text.encode('utf8').decode(sys.stdout.encoding)

print("XlsMerger")
print()

import pip
pip.main(['install', "xlrd"])
pip.main(['install', "xlwt"])



import os
import xlrd
# https://xlrd.readthedocs.io/en/latest/api.html """
import xlwt


write_book = xlwt.Workbook()
write_file_name = "db.xls"

read_file_count = 0
read_sheet_count = 0


for read_file_name in os.listdir(os.getcwd()):

    if read_file_name.endswith(".xls") and not read_file_name == write_file_name:

        print()
        print("info:", "reading file \'{0}\'".format(console_friendly(read_file_name)))

        read_file_count += 1
        read_book = xlrd.open_workbook(read_file_name,formatting_info=True)

        for sheet_index in range(len(read_book.sheets())):

            read_sheet = read_book.sheet_by_index(sheet_index)
            read_sheet_count += 1
            read_sheet_name = read_sheet.name

            print("info:", "reading sheet \'{0}\' ({1} rows)".format(console_friendly(read_sheet_name), read_sheet.nrows))

            write_sheet = write_book.add_sheet(read_file_name.split(".xls")[0] + " - " + read_sheet_name)
            

            print("info:", "cells per row = ", [len(read_sheet.row_values(row)) for row in range(read_sheet.nrows)])

            for row_index in range(read_sheet.nrows):
                for col_index, read_value in zip(range(len(read_sheet.row_values(row_index))), read_sheet.row_values(row_index)):
                    write_sheet.write(row_index, col_index, read_value)

            pass
        pass
    pass
pass



write_book.save(write_file_name)

print()
print("info:", "total", read_file_count, "files were read")
print("info:", "total", read_sheet_count, "sheets were read")

print()
input("press ENTER to quit")

