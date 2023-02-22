import pyqrcode
q=pyqrcode.create("https://www.careercompiler.com/")
p=pyqrcode.create("https://www.sarkariresult.info/")
if p=='sar':
    q.svg("Career.svg", scale=10)
else:
    p.svg("sarkari.svg", scale=10)

