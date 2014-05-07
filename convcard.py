from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, black, red

# global vars (constants)
w,h = (8*inch,8.5*inch)
offset = 4
fs = 2*offset # font size
sp = u'\u2660'
he = u'\u2661'
di = u'\u2662'
cl = u'\u2663'
box = u'\u25a1'
selbox = u'\u25a8'

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
	
	#2NT Box
	c.rect(470,h-13*offset,w-470-2*offset,-100)
	
def addbluetext(c):
	c.setFillColorRGB(0,0.5,1)
	textobj = c.beginText()
	textobj.setTextOrigin(w/2+offset, h-offset*18)
	textobj.moveCursor(25,0)
	textobj.textOut('1NT')
	textobj.moveCursor(-25,3*offset)
	textobj.textLine('_______ to _______')
	textobj.textOut('_______ to _______')
	textobj.moveCursor(w/3-offset,0)
	textobj.textLine('Jacoby'+box+'   Texas'+box)
	textobj.moveCursor(20+offset-w/3,12*offset)
	textobj.textOut('Transfer to '+he+box)
	textobj.moveCursor(80,0)
	textobj.textLine('4'+di+', 4'+he+' Transfer'+box)
	textobj.moveCursor(-80,3*offset)
	textobj.textLine('Transfer to '+sp+box)
	
	# Need to include boxes outside 1NT, however I need other colors for spacing guidelines.
	
	c.drawText(textobj)
	
def add2level(c):
	c.setFillColor(black)
	textobj = c.beginText()
	textobj.setFont('Deja', 2*fs)
	textobj.setTextOrigin(w/2+offset,54*offset)
	textobj.textLine('2'+cl)
	textobj.setTextOrigin(w/2+offset,44*offset)
	textobj.textLine('2'+di)
	textobj.setTextOrigin(w/2+offset,34*offset)
	textobj.textLine('2'+he)
	textobj.setTextOrigin(w/2+offset,24*offset)
	textobj.textLine('2'+sp)
	c.drawText(textobj)

def addBold(c):
		c.setFillColor(black)
		textobj = c.beginText()
		textobj.setFont('DejaBd', fs)
		textobj.setTextOrigin(w/2+offset,h-4*offset)
		textobj.textLine('Names:')
		textobj.moveCursor(0,offset)
		textobj.textLine('General Approach:')
		textobj.moveCursor(0,offset)
		textobj.textLine('Very Light:')
	
		textobj.setTextOrigin(360,h-offset*15)
		textobj.textLine('NoTrump Openings')
		c.drawText(textobj)
	
c = canvas.Canvas("precision-cc.pdf",pagesize=(w,h))  # inch = 72 points

c.setFont('Deja',fs)


makegrid(c)
addbluetext(c)
add2level(c)
addBold(c)
c.showPage()
c.save()
