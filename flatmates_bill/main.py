from PdfReport import PdfReport
from bill import Bill
from PdfReport import FileSharer

from flatmate import Flatmate

amount = float(input("Hello beloved user. Enter the bill amount please "))
period = input("During which period did that bill occur ? E.g November 2019 ")

name_of_flatmate1 = input("What is the name of the first flatmate ? ")
number_of_days_flatmate1_stayed = int(input(f"How many days did {name_of_flatmate1} stay ? "))

name_of_flatmate2 = input("What is the name of the second flatmate ? ")
number_of_days_flatmate2_stayed = int(input(f"How many days did {name_of_flatmate2} stay ? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name_of_flatmate1, number_of_days_flatmate1_stayed)
flatmate2 = Flatmate(name_of_flatmate2, number_of_days_flatmate2_stayed)

pdf_report = PdfReport(filename=f"{period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)

our_file_sharer = FileSharer(pdf_report.filename)
print(our_file_sharer.share())