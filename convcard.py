from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, black, cyan, red

# global vars (constants)
w,h = (8*inch,8.5*inch)
offset = 4
fs = 2*offset # font size
sp = u'\u2660'
he = u'\u2661'
di = u'\u2662'
cl = u'\u2663'

# register fonts
pdfmetrics.registerFont(TTFont('Deja', 'dejavusans.ttf'))
pdfmetrics.registerFont(TTFont('DejaBd', 'dejavusans-bold.ttf'))

# testing vars
#names = "   Tom & Jenni Carmichael   "
names = ''

def makegrid(c):
	# Lines are approximate at best for now, can be tweaked as needed later.
	
	c.setLineWidth(4)
	c.grid([offset,w/2,w-offset],[offset,h-offset])
	c.setLineWidth(2)
	
	#Verticle Left
	c.line(w/4,h-offset,w/4,h-88*offset)  
	
	#Horizontal Left
	c.line(offset,h-23*offset,w/4,h-23*offset)
	c.line(w/4,h-20*offset,w/2,h-20*offset)
	
	c.line(offset,h-45*offset,w/4,h-45*offset)
	c.line(w/4,h-48*offset,w/2,h-48*offset)
	
	c.line(offset,h-55*offset,w/4,h-55*offset)
	c.line(offset,h-68*offset,w/4,h-68*offset)
	c.line(w/4,h-73*offset,w/2,h-73*offset)
	
	c.line(offset,h-88*offset,w/2,h-88*offset)
	c.line(offset,h-101*offset,w/2,h-101*offset)
	#Lead seperator
	c.setLineWidth(1)
	c.line(w/6,h-105*offset,w/6,h-129*offset)
	c.line(w/3,h-101*offset,w/3,7*offset)
	c.line(offset,14*offset,w/3,14*offset)
	
	#Right
	c.setLineWidth(2)
	c.line(w/2,h-offset*5,w-offset,h-offset*5)
	c.line(w/2,h-offset*12,w-offset,h-offset*12)
	
	c.line(w/2,h-offset*49,w-offset,h-offset*49)
	c.line(w/2,h-offset*95,w-offset,h-offset*95)
	
	c.line(408,h-offset*49,408,h-offset*95)  # 408 is halfway between 2/3 and 3/4, i.e. 17/24ths.
	c.line(408,h-offset*72,w-offset,h-offset*72)
	
	c.line(w/2,18*offset,w-offset,18*offset)
	
	c.setLineWidth(1)
	c.line(w/2,28*offset,w-offset,28*offset)
	c.line(w/2,38*offset,w-offset,38*offset)
	c.line(w/2,48*offset,w-offset,48*offset)
	


	
c = canvas.Canvas("precision-cc.pdf",pagesize=(w,h))  # inch = 72 points

c.setFont('Deja',fs)


makegrid(c)
c.showPage()
c.save()
