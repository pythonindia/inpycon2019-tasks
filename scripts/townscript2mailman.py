"""Usage: townscript2mailman LAST_REGID < townscript-file.txt > mailman-format.txt)

The ticket purchase data from townscript is available in CSV
format. The last registration ID that was already added
inpycon-announce needs to be kept track of. This needs to provided as
argument to the script. Only the registration greater than LAST_REGID
will be provided in Mailman format.

NOTE: Mailman gets timedout if more than 100 users are added in
bulk. So do not add more that 100 users at a time to Mailman.

"""
import sys
import csv

email_list = set()
try:
    last_regid = int(sys.argv[1])
except (IndexError, ValueError):
    print("Usage: townscript2mailman.py LAST_REGID")
    exit(1)

reader = csv.reader(sys.stdin)
for i, line in enumerate(reader):
    if i == 0:
        continue

    email = line[2]
    name = line[1]
    regid = int(line[0])

    if email in email_list:
        continue

    if regid <= last_regid:
        continue

    email_list.add(email)

    print("{} <{}>".format(name, email))
        
