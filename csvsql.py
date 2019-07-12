from __future__ import print_function
import pymysql
import xlrd
import re
import os
import csv

print("------------------------------------------")
print("-   Welcome Export From CSV  MySQL Using Python")
print("-   Version 1.0                        -")
print("-   Powered By Azam                       -")
print("------------------------------------------")
print("Enter  File  To Be Export")
#path = "F:/sepadu2015/Call billing/December"
#path = "F:/family matter/tune wisma/staff tune"
# dirs = os.listdir( path )
# This would print all the files and directories
# for file in dirs:
with open('products.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['OEM'], row['BRAND'], row['MODEL'], row['PRICE'], row['TITLE'], row['IMAGE URL'], row['PRODUCT TYPE'], row['PRODUCT URL'])
        # insert

        conn = pymysql.connect(host='localhost', user='antoncharles', passwd='', db='test')
        sql_statement = "INSERT INTO `test`.`product_table` (`oem` ,`brand`,`model`,`price`,`title`," \
                        "`image url`,`product type`,`product url`)VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
        print(sql_statement)
        cur = conn.cursor()

        cur.executemany(sql_statement, [(row['OEM'], row['BRAND'], row['MODEL'], row['PRICE'], row['TITLE'], row['IMAGE URL'], row['PRODUCT TYPE'], row['PRODUCT URL'])])
        conn.escape_string(sql_statement)
        conn.commit()
#
# host = 'https://antoncharlesgroup.com:2083/'
# user = 'antoncha_anton'
# password = 'acgtshout951753'
