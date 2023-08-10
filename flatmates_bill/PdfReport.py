import webbrowser
import os
from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    Creates a Pdf report file that contains data about the flatmates such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("files/house.jpg", w=30, h=30)

        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate1.pays(bill)), border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate2.pays(bill)), border=0, ln=1)

        os.chdir("files")

        pdf.output(self.filename)

        webbrowser.open(self.filename)

class FileSharer:

    def __init__(self, filepath, api_key="Acf5ay8PdTnW8Ck8d2Piaz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath = self.filepath)
        return new_filelink.url
