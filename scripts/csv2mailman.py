"""Usage: csv2mailman < csv-file.txt > mailman-format.txt)

Users can register for notifications on a Google form. The form data
can be exported to CSV. This CSV can be converted to a form that
Mailman bulk upload accepts using this script. The fourth column in
the CSV indicates if the user has already been added to the mailing
list, if so that user is skipped.

Once the users have been added to the inpycon-announce mailing list,
the fourth column in the spreadsheet has to be marked with a yes.

NOTE: Mailman gets timedout if more than 100 users are added in
bulk. So do not add more that 100 users at a time to Mailman.
"""
import sys
import csv

email_list = set()

reader = csv.reader(sys.stdin)
for i, (_, name, email, done) in enumerate(reader):
    if i == 0:
        continue

    if email in email_list:
        continue

    email_list.add(email)

    if done.lower() != "yes":
        print("{} <{}>".format(name, email))
        
