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

def hello(c):
	c.drawString(100,100,"Hello World")
	c.drawString(100,200,"More tests")

def gridtest(c):
	c.setLineWidth(3)
	c.grid([offset,w/2,w-offset],[offset,h-offset])
	c.setLineWidth(1)
	c.setFont('DejaBd',fs)
	c.drawString(w/2+offset,h-offset*4+1, 'Names:')
	c.setFont('Deja',fs)
	c.drawString(w/2+9*offset,h-offset*4+1, names)
	c.setFont('DejaBd',fs)
	c.drawString(w/2+offset,h-offset*7.5,'General Approach:')
	c.setFont('Deja',fs)
	c.setFillColor(red)
	c.drawString(11*w/16+2*offset,h-offset*7.5,'Strong Club (1'+cl+' forcing)')
	c.setFillColor(black)
	# NT
	c.setFont('DejaBd',fs)
	c.drawCentredString(3*w/4,h-offset*11.5,'Notrump Opening Bids')
	c.setFont('Deja',fs)
	c.grid([w/2,w-offset],[offset,h/2+20*offset,h-offset*9,h-offset*5,h-offset])
	#c.line(w/2,h-offset*6,w-offset,h-offset*6)
	

	
	
c = canvas.Canvas("hello.pdf",pagesize=(w,h))  # inch = 72 points

c.setFont('Deja',fs)
#hello(c)
gridtest(c)
c.showPage()
c.save()
