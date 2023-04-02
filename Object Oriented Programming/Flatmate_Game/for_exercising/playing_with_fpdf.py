from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt' ,format='A4')
pdf.add_page()

pdf.set_font(family='Times', size=24 , style='B')
pdf.cell(w=200,h=80, txt='Flatmates Bill' , border = 1 , align='C' , ln=1)      # ln=1 add a line after this line of code
pdf.cell(w=100,h=60, txt='Period' , border=1)
pdf.cell(w=200,h=60, txt='    March 2021' , border=1 , ln=1)

pdf.set_font(family='Times', size=20)

pdf.cell(w=100,h=80, txt='Flatmate1' , border=0)
pdf.cell(w=100,h=80, txt='Flatmate1.Pay' , border=0 , ln=1)

pdf.cell(w=100,h=80, txt='Flatmate2' , border=0)
pdf.cell(w=100,h=80, txt='Flatmate2.Pay' , border=0 , ln=1)


pdf.output('billtest.pdf')

