from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, black, red, green



# global vars (constants)
w,h = (8*inch,8.5*inch)
offset = 4
fs = 2*offset # font size
sp = u'\u2660'
he = u'\u2661'
di = u'\u2662'
cl = u'\u2663'
box = u'\u2610'
selbox = u'\u2611'
blue=Color(0,0.5,1)

# register fonts
pdfmetrics.registerFont(TTFont('Deja', 'dejavusans.ttf'))
pdfmetrics.registerFont(TTFont('DejaBd', 'dejavusans-bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaThin', 'dejavusanscondensed.ttf'))

# testing vars
#names = "   Tom & Jenni Carmichael   "
names = ''

def centerText(textobj,text,font='DejaBd',fontsize=fs):
#  textobjects do not have the equivalent of drawCentredString
#  created my own To use, set the origin point before calling the function, then send
#  both the textobject and the string to center.  Defaults to Deja Bold, default fontsize but can override if wanted.

	textwidth = pdfmetrics.stringWidth(text,font,fontsize)
	textobj.moveCursor(-textwidth/2,0)
	textobj.textOut(text)
	
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
	c.line(w/6,h-108*offset,w/6,h-125*offset)
	c.line(w/3,h-101*offset,w/3,offset)
	c.line(offset,13*offset,w/3,13*offset)
	
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
	
	#3NT Box
	c.rect(470,h-13*offset,w-470-2*offset,-64)
	
def addbluetext(c):
	
	c.setFillColor(blue)
	textobj = c.beginText()
	# Experiment
	textobj.setLeading(12)
	textobj.setTextOrigin(w/2+offset, h-offset*18)
	textobj.moveCursor(25,0)
	textobj.textOut('1NT')
	textobj.moveCursor(-25,3*offset)
	textobj.textLine('_______ to _______')
	textobj.textOut('_______ to _______')
	textobj.moveCursor(w/3-offset,-2*offset)
	textobj.textLine('Jacoby'+box+'   Texas'+box)
	textobj.moveCursor(13+offset-w/3,44)
	textobj.textOut('Transfer to '+he+box)
	textobj.moveCursor(90,0)
	textobj.textLine('4'+di+',4'+he+' Transfer'+box)
	textobj.moveCursor(-90,0)
	textobj.setFillColor(red)
	textobj.textLine('Forcing Stayman'+box)
	textobj.setFillColor(blue)
	textobj.textLine('Transfer to '+sp+box)
	
	textobj.setTextOrigin(412,h-offset*78)
	textobj.setFillColor(black)
	textobj.textOut('Min Length:    4'+box+'  3'+box)
	textobj.setFillColor(blue)
	textobj.textOut('  2'+box+'  1'+box+'  0'+box)
	# Need to include boxes outside 1NT, however I need other colors for spacing guidelines.
	
	textobj.setTextOrigin(412,h-offset*55)
	textobj.textLine(' '*31+'2+ '+cl+box)
	
	c.drawText(textobj)
	
def add2level(c):
	c.setFillColor(black)
	textobj = c.beginText()
	textobj.setFont('Deja', 1.8*fs)
	textobj.setTextOrigin(w/2+offset,54.5*offset)
	textobj.textLine('2'+cl)
	textobj.setTextOrigin(w/2+offset,44.5*offset)
	textobj.textLine('2'+di)
	textobj.setTextOrigin(w/2+offset,34.5*offset)
	textobj.textLine('2'+he)
	textobj.setTextOrigin(w/2+offset,24.5*offset)
	textobj.textLine('2'+sp)
	c.drawText(textobj)


def addBold(c):
	c.setFillColor(black)
	textobj = c.beginText()
	textobj.setFont('DejaBd', fs)
	textobj.setTextOrigin(w/2+offset,h-4*offset+1)
	textobj.textLine('Names:')
	textobj.moveCursor(0,offset)
	textobj.textLine('General Approach:')
	textobj.moveCursor(0,offset)
	textobj.textLine('Very Light:')
	
	textobj.setTextOrigin(w/2+91,h-offset*15+1)
	centerText(textobj,'NoTrump Openings')
		
		
	textobj.setTextOrigin(w/2+60,h-offset*52+1)
	centerText(textobj,'Major Openings')
	textobj.setTextOrigin(490,h-offset*52+1)
	centerText(textobj,'1'+cl+' Opening')
	textobj.setTextOrigin(490,h-offset*75+1)
	centerText(textobj,'1'+di+' Opening')
		
	textobj.setTextOrigin(3*w/4,15*offset+1)
	centerText(textobj,'Other Conventional Calls')
		
	textobj.setTextOrigin(w/8,h-4*offset+1)
	centerText(textobj,'Special Doubles')
	
	textobj.setTextOrigin(3*w/8,h-4*offset+1)
	centerText(textobj,'NoTrump Overcalls')
		
	textobj.setTextOrigin(w/8,h-26*offset+1)
	centerText(textobj,'Simple Overcalls')
	
	textobj.setTextOrigin(w/8,h-34*offset+1)
	centerText(textobj,'Responses')
		
	textobj.setTextOrigin(3*w/8,h-23*offset+1)
	centerText(textobj,'Defense vs. NoTrump')
		
	textobj.setTextOrigin(w/8,h-48*offset+1)
	centerText(textobj,'Jump Overcalls')
		
	textobj.setTextOrigin(3*w/8,h-51*offset+1)
	centerText(textobj,"Over Opp's T/O Dbl")
		
	textobj.setTextOrigin(w/8,h-58*offset+1)
	centerText(textobj,'Opening Preempts')
		
	textobj.setTextOrigin(w/8,h-71*offset+1)
	centerText(textobj,'Direct Cuebid')
		
	textobj.setTextOrigin(3*w/8,h-76*offset+1)
	centerText(textobj,"Vs. Opening Preempts Dbl is")
		
	textobj.setTextOrigin(w/4,h-91*offset)
	centerText(textobj,'Slam Conventions')
		
	textobj.setTextOrigin(w/6,h-104*offset)
	centerText(textobj, 'Leads')
		
	textobj.setTextOrigin(5*w/12,h-104*offset)
	centerText(textobj, 'Carding')
		
	textobj.setTextOrigin(w/12,h-107*offset)
	textobj.setFont('Deja',fs)
	centerText(textobj, 'Vs. Suits', font='Deja')
	textobj.setTextOrigin(3*w/12,h-107*offset)
	centerText(textobj, 'Vs. NoTrump', font='Deja')
		
		# Opening Lead selection
		# Going line by line to get the bolding/coloring right
		# Tedious compared to textLines(), but I don't know of a way to change font midstring.
		
	textobj.setTextOrigin(offset*3,h-110*offset)
		# Line 1
	textobj.setFont('DejaBd',fs)
	textobj.textOut('x ')
	textobj.setFont('Deja',fs)
	textobj.setFillColor(red)
	textobj.textOut('x')
	textobj.setFillColor(black)
	textobj.moveCursor(10*offset,0)
	textobj.textOut('x x x ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('x')
	textobj.moveCursor(w/6-10*offset,0)
	textobj.textOut('x ')
	textobj.setFont('Deja',fs)
	textobj.setFillColor(red)
	textobj.textOut('x')
	textobj.setFillColor(black)
	textobj.moveCursor(10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('x ')
	textobj.setFont('Deja',fs)
	textobj.textLine('x x x')
		
		# Line 2
	textobj.moveCursor(-w/6-10*offset,0)
	textobj.textOut('x x ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('x ')
	textobj.setFont('Deja',fs)
	
	textobj.moveCursor(10*offset,0)
	textobj.textOut('x x x ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('x ')
	textobj.setFont('Deja',fs)
	textobj.textOut('x')
	textobj.moveCursor(w/6-10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('x ')
	textobj.setFont('Deja',fs)
	textobj.textOut('x x')
	textobj.moveCursor(10*offset,0)
	textobj.textOut('x x x ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('x ')
	textobj.setFont('Deja',fs)
	textobj.textLine('x')
		
		# Line 3
	textobj.moveCursor(-w/6-10*offset,0)
	textobj.textOut('A K x')
	textobj.moveCursor(10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('T ')
	textobj.setFont('Deja',fs)
	textobj.textOut('9 x')
	textobj.moveCursor(w/6-10*offset,0)
	textobj.textOut('A ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('K ')
	textobj.setFont('Deja',fs)
	textobj.textOut('J x')
	textobj.moveCursor(10*offset,0)
	textobj.textOut('A ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('Q ')
	textobj.setFont('Deja',fs)
	textobj.textLine('J x')
		
		# Line 4 
	textobj.moveCursor(-w/6-10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('K ')
	textobj.setFont('Deja',fs)
	textobj.textOut('Q x')
	textobj.moveCursor(10*offset,0)
	textobj.textOut('K ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('J ')
	textobj.setFont('Deja',fs)
	textobj.textOut('T x')
	textobj.moveCursor(w/6-10*offset,0)
	textobj.textOut('A ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('J ')
	textobj.setFont('Deja',fs)
	textobj.textOut('T 9')
	textobj.moveCursor(10*offset,0)
	textobj.textOut('A ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('T ')
	textobj.setFont('Deja',fs)
	textobj.textLine('9 x')

		# Line 5
	textobj.moveCursor(-w/6-10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('Q ')
	textobj.setFont('Deja',fs)
	textobj.textOut('J x')
	textobj.moveCursor(10*offset,0)
	textobj.textOut('K ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('T ')
	textobj.setFont('Deja',fs)
	textobj.textOut('9 x')
	textobj.moveCursor(w/6-10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('K ')
	textobj.setFont('Deja',fs)
	textobj.textOut('Q J x')
	textobj.moveCursor(10*offset,0)
	textobj.textOut('K ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('Q ')
	textobj.setFont('Deja',fs)
	textobj.textLine('T 9')

		# Line 6
	textobj.moveCursor(-w/6-10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('J ')
	textobj.setFont('Deja',fs)
	textobj.textOut('T 9')
	textobj.moveCursor(10*offset,0)
	textobj.textOut('Q ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('T ')
	textobj.setFont('Deja',fs)
	textobj.textOut('9 x')
	textobj.moveCursor(w/6-10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('Q ')
	textobj.setFont('Deja',fs)
	textobj.textOut('J T x')
	textobj.moveCursor(10*offset,0)
	textobj.textOut('Q ')
	textobj.setFont('DejaBd',fs)
	textobj.textOut('T ')
	textobj.setFont('Deja',fs)
	textobj.textLine('9 x')

		# Line 7 (final)
	textobj.moveCursor(-w/6-10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('K ')
	textobj.setFont('Deja',fs)
	textobj.textOut('Q T 9')
	textobj.moveCursor(w/6,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('J ')
	textobj.setFont('Deja',fs)
	textobj.textOut('T 9 x')
	textobj.moveCursor(10*offset,0)
	textobj.setFont('DejaBd',fs)
	textobj.textOut('T ')
	textobj.setFont('Deja',fs)
	textobj.textLine('9 x x')
	
	c.drawText(textobj)

def addblacktext(c):
	textobj = c.beginText()
	textobj.setFont('Deja',fs)
	textobj.setFillColor(black) # probably redundant

	# I was just working on the leads/carding section and want to finish it, so starting there
	
	vsString = 'vs. Suits'+box+'   vs. NT'+box
	textobj.setTextOrigin(10*offset,h-128*offset)
	textobj.textLines(['4th Best','3rd/Low','Attitude'])
	textobj.setTextOrigin(w/6,h-128*offset)
	textobj.textLines([vsString,vsString,vsString])
	
	textobj.setTextOrigin(2*offset,17*offset)
	textobj.textLines(["Primary signal to partner's leads:",'Attitude'+box+'   Count'+box+'   Suit Preference'+box])
	
	textobj.setTextOrigin(5*w/12+2*offset,h-107*offset)
	boxStr = '   '+box+'    '+box
	bl= '_____________________'
	textobj.textLines(['Suits NT',boxStr,'','','','',boxStr,boxStr,'',boxStr,boxStr,boxStr,'','',
	                 boxStr,'   '+box,boxStr])
	
	textobj.setTextOrigin(w/3+offset,h-107*offset)
	textobj.textLines(['','Standard:','    Except '+box,bl,'','Upside Down','   Count','   Attitude',
	                  'First Discard','   Odd-Even','   Lavinthal','  __________','','Other Carding','  Smith Echo','  Trump S/P','  Foster Echo'])
	
	# General Approach
	textobj.setTextOrigin(w/2+15*offset,h-10.5*offset)
	textobj.textOut('Openings'+box+'   3rd Hand'+box+'   Overcalls'+box+'   Preempts'+box)
	
	# NT Box
	# setLeading experimental - changes the height between lines.  Things were a little tight and I had extra space, so trying it out.
	
	textobj.setLeading(12)
	
	textobj.setTextOrigin(w/2+offset,h-27*offset)
	textobj.textLines(['5-Card Major common'+box,'System on over _______','2'+cl+' Stayman'+box+' Puppet'+box,
	                  '2'+di,'','2'+he,'2'+sp,'2NT'])
							
	textobj.setTextOrigin(w/2+106,h-21*offset)
	textobj.textLines(['3'+cl,'3'+di,'3'+he,'3'+sp,'','','','','Neg. Dbl'+box+' ________'])
	
	textobj.setTextOrigin(470+offset,h-16*offset)
	textobj.textLine('2NT   _____ to _____')
	textobj.setTextOrigin(5*w/6,h-19*offset)
	textobj.textLines(['Puppet Stayman'+box,'','3'+sp,''])
	
	textobj.setTextOrigin(470+offset, h-31*offset)
	textobj.textLine('3NT   _____ to _____')
	
	# Major Box
	tmpbox = box+'    '+box
	textobj.setTextOrigin(w/2+offset,h-55*offset)
	textobj.textLines(['Min Length','1st/2nd','3rd/4th'])
	textobj.setTextOrigin(370,h-55*offset)
	textobj.textLines(['4     5',tmpbox,tmpbox])
	
	# Dashed separator
#	c.setDash(1,3)
#	c.line(w/2,h-62*offset,408,h-62*offset)
#	c.setDash(1)
	
	textobj.setTextOrigin(w/2+offset,h-64*offset)
	textobj.textLine('Direct Dbl Raise:')
	textobj.textOut('     Limit'+box)
	textobj.setFillColor(red)
	textobj.textLine(' Mixed'+box+' Weak'+box)
	textobj.setFillColor(black)
	textobj.textLine('After Overcall Dbl Raise:')
	textobj.textLine('     Limit'+box+' Mixed'+box+' Weak'+box)
	textobj.textOut('Art Raise: ')
	textobj.setFillColor(red)
	textobj.textLine('2NT'+box+' 3NT'+box+' Spl'+box)
	textobj.textLine('Other ______________________')
	textobj.setFillColor(blue)
	textobj.textLine('1NT Forcing'+box+'   Semi-Forc'+box)
	textobj.setFillColor(black)
	textobj.textLines(['2NT _____ to _____ GF'+box+' Inv'+box,'3NT _____ to _____'])
	textobj.setFillColor(red)
	textobj.textLines(['Drury'+box+' Reverse'+box+' 2-way'+box,'Other ______________________'])
	
	# 1C Box
	textobj.setFillColor(black)
	textobj.setTextOrigin(412,h-offset*55)
	textobj.textLine(' '*44+'3+ '+cl+box)
	
	# 1D Box
	
	textobj.setFillColor(black)
	textobj.setTextOrigin(412,h-offset*78)
	textobj.textLine('')
	textobj.textOut('Dbl Raise: GF'+box+' Limit'+box)
	textobj.setFillColor(red)
	textobj.textLine(' Mixed'+box+' Weak'+box)
	textobj.setFillColor(black)
	textobj.textLine('After Overcall: Limit'+box+' Mixed'+box+' Weak'+box)
	textobj.textOut('Forc. Raise:  ')
	textobj.setFillColor(red)
	textobj.textLine('2'+di+box+'  Other______________')
	textobj.setFillColor(black)
	textobj.textLine('2NT _____ to _____    3NT _____ to _____')
	textobj.setFillColor(red)
	textobj.textLine('Other_________________________________')
	
	# 2C box  55*off
	
	textobj.setFillColor(black)
	textobj.setTextOrigin(w/2+8*offset, 55*offset)
	textobj.textLines(['_____ to _____ HCP','','Str'+box])
	textobj.setFillColor(red)
	textobj.setTextOrigin(w/2+8*offset, 55*offset)
	textobj.textLines(['','6+'+cl+box+'  5'+cl+' 4 Maj'+box,'         Other________'])
	textobj.setTextOrigin(w/2+offset, 55*offset)
	textobj.setFillColor(red)
	textobj.textLines(['','Nat:'])
	textobj.setFillColor(black)
	textobj.textLine('Art:')
	
	textobj.setTextOrigin(408, 55*offset)
	textobj.setFillColor(red)
	textobj.textLine('2'+di+' Ask'+box+'  Other:_______________________')
	textobj.setFillColor(black)
	textobj.textOut('2 Maj: Forc'+box)
	textobj.setFillColor(red)
	textobj.textLine(' NF Nat'+box+' Other'+box+' _________')
	textobj.textLine('Other Resp: ___________________________')
	
	# 2D Box   45*off
	
	textobj.setFillColor(black)
	textobj.setTextOrigin(w/2+8*offset, 45*offset)
	textobj.textLine('_____ to _____ HCP')
	textobj.textOut('Weak'+box)
	textobj.setFillColor(red)
	textobj.textLine('  Inter'+box+' Str'+box)
	textobj.textLine('Short '+di+box+'  Other'+box)
	textobj.setTextOrigin(w/2+offset, 45*offset)
	textobj.setFillColor(black)
	textobj.textLines(['','Nat:'])
	textobj.setFillColor(red)
	textobj.textLine('Art:')
	
	textobj.setTextOrigin(408,45*offset)
	blankline='________________________________________'
	textobj.textLines(['Desc: __________________________________',
	                 'Resp: __________________________________',
						    blankline])
	# 2H Box   35*off
	
	textobj.setFillColor(black)
	textobj.setTextOrigin(w/2+8*offset, 35*offset)
	textobj.textLine('_____ to _____ HCP')
	textobj.textOut('Weak'+box)
	textobj.setFillColor(red)
	textobj.textLine('  Inter'+box+' Str'+box)
	textobj.textLine('Other'+box)
	textobj.setTextOrigin(w/2+offset, 35*offset)
	textobj.setFillColor(black)
	textobj.textLines(['','Nat:'])
	textobj.setFillColor(red)
	textobj.textLine('Art:')

	textobj.setTextOrigin(408,35*offset)
	textobj.textLines(['Desc: __________________________________',
	                   'Resp: __________________________________',
	                 blankline])	
	# 2S Box   25*off
	textobj.setFillColor(black)
	textobj.setTextOrigin(w/2+8*offset, 25*offset)
	textobj.textLine('_____ to _____ HCP')
	textobj.textOut('Weak'+box)
	textobj.setFillColor(red)
	textobj.textLine('  Inter'+box+' Str'+box)
	textobj.textLine('Other'+box)
	textobj.setTextOrigin(w/2+offset, 25*offset)
	textobj.setFillColor(black)
	textobj.textLines(['','Nat:'])
	textobj.setFillColor(red)
	textobj.textLine('Art:')

	textobj.setTextOrigin(408,25*offset)
	textobj.textLines(['Desc: __________________________________',
	                   'Resp: __________________________________',
	                   blankline])	
	# Special Doubles
	textobj.setFillColor(black)
	textobj.setTextOrigin(offset*2,h-6*offset)
	textobj.textLines(['After Overcall:','Negative'+box+' thru '+'_'*16,'Resp.'+box+' thru '+'_'*9+' Maximal'+box,
	'','Cards'+box+'  Min. Offshape T/O'+box])
	
	
	# NT Overcalls
	textobj.setTextOrigin(w/4+offset,h-6*offset)
	textobj.textLines(['Direct: ____ to ____  Systems on'+box,'','Balancing: ____ to ____',
	'Jump to 2NT: Minors'+box+' 2 Lowest'+box])
	
	# Simple Overcall
	textobj.setTextOrigin(offset*2, h-28*offset)
	textobj.textLines(['1 level ____ to ____ HCP (usually)','often 4 cards'+box+' very light style'+box,
	'','New Suit: Forc'+box+' NFConst'+box+' NF'+box,'Jump Raise: Forc'+box+' Inv'+box+' Weak'+box])
	
	# Def vs NT
	textobj.setTextOrigin(w/4+offset,h-25*offset)
	textobj.textLines(['vs:','2'+cl,'2'+di,'2'+he,'2'+sp,'Dbl'])

	# Jump OC
	textobj.setTextOrigin(offset*2, h-51*offset)
	textobj.textLines([' '*38+'Weak'+box])
	
	# Opening Preempts
	textobj.setTextOrigin(offset*2, h-60*offset)
	textobj.textLines(['3/4 bids:', '  Sound'+box+'   Light'+box+'   Very Light'+box])
	
	# Over T/O X
	textobj.setTextOrigin(w/4+offset, h-54*offset)
	textobj.textLines(['New Suit Forc: 1-level'+box+' 2-level'+box,'Jump Shift: Forcing'+box+' Inv'+box+' Weak'+box,
	'Redouble Implies no fit'+box])
	
	# Direct Cuebid
	textobj.setTextOrigin(offset*2, h-74*offset)
	textobj.textLines([' '*10+'Over:   Minor       Major','Natural','Strong T/O','Michaels'])
	textobj.setTextOrigin(offset*18, h-74*offset)
	textobj.textLines(['','',box+' '*13+box,box+' '*13+box])
	
	# vs preempts
	textobj.setTextOrigin(w/4+offset, h-78*offset)
	textobj.textLine('Takeout'+box+' thru ______')
	
	# slam
	textobj.setTextOrigin(2*offset,h-93*offset)
	textobj.textLines(['Gerber'+box+'    Blackwood'+box+'    RKC'+box+'    1430'+box+'    Kickback'+box+'    Redwood'+box,
	'_'*70,'vs Interference: D0P1'+box+'  DEPO'+box+'  Level:  ____________________  R0P1'+box])

	c.drawText(textobj)

def addocc(c):
	blankline='_'*int(w/8-3)
	textobj = c.beginText()
	textobj.setFont('Deja',fs)
	textobj.setFillColor(red)
	
	textobj.setTextOrigin(w/2+offset,13*offset)
	textobj.textLines([blankline,blankline,blankline,blankline,blankline])
	c.drawText(textobj)
	
def drawLogo(c):
	# Testing!!!
	c.setFillColor(black)
	c.drawImage('forcingclub-logo.png',13*offset,5.3*offset,width=92,height=30)
	c.setFont('Deja',12)
	c.drawCentredString(w/6, 3*offset,'http://forcing.club/')

def addredtext(c):
	c.setFillColor(red)
	textobj = c.beginText()
	textobj.setFont('Deja',fs)
	textobj.setFillColor(red)
	textobj.setLeading(12)
	
	# 3 level lines in NT box
	textobj.setTextOrigin(w/2+120,h-21*offset)
	textobj.textLines(['______________']*4)
	
	textobj.setTextOrigin(w/2+106,h-33*offset)
	textobj.textLines([' _________________','','Smolen'+box,'Lebensohl'+box+' _______________________________',
	' '*33+'Other ________________','_'*43])
	
	
	# 2S and 2NT in NT box
	textobj.setTextOrigin(w/2+offset+16, h-27*offset)
	textobj.textLines(['','','','','','','___________________','___________________'])
	
	# 2NT opener box
	textobj.setTextOrigin(470+offset,h-16*offset)
	textobj.textLines(['','','',' '*9+'_'*17,'_'*23,'','_'*22,'_'*22])
	
	# 1C opener
	textobj.setTextOrigin(412,h-offset*55)
	textobj.textLines(['Forcing'+box+' Strong'+box,'Desc: '+'_'*32,'1'+di+' Resp: Neg'+box+' Other '+'_'*16,
	'Other: '+'_'*32,'_'*39,'_'*39])

	# Special Doubles
	textobj.setTextOrigin(offset*2,h-6*offset)
	textobj.textLines([' '*24+'Penalty'+box+' '+'_'*7,'','','Support: Dbl'+box+' thru _____ Redbl'+box,'','_'*33])
	
	# NT Overcalls
	textobj.setTextOrigin(w/4+offset,h-6*offset)
	textobj.textLines(['','Conv'+box+' '+'_'*26,'','','Conv'+box+' '+'_'*26])

	# Simple Overcall
	textobj.setTextOrigin(offset*2, h-28*offset)
	textobj.textLines(['','','','','','_'*33])
	
	# Def vs NT
	textobj.setTextOrigin(w/4+offset,h-25*offset)
	textobj.textLines([' '*8+'_'*14+' '+'_'*14]*6+['Other '+'_'*27,'_'*34])
	
	# Jump OC
	textobj.setTextOrigin(offset*2, h-51*offset)
	textobj.textLines(['Strong'+box+' Intermediate'+box,'_'*33])

	# Opening Preempts
	textobj.setTextOrigin(offset*2, h-60*offset)
	textobj.textLines(['','','Conv/Resp '+'_'*21])
	
	# Over T/O X
	textobj.setTextOrigin(w/4+offset, h-54*offset)
	textobj.textLines(['','','','2NT Over     Limit+   Limit   Weak','Majors',
	'Minors','Other '+'_'*27])	
	textobj.setTextOrigin(w/4+offset*16, h-54*offset)
	textobj.textLines(['','','','',box+' '*9+box+' '*9+box,box+' '*9+box+' '*9+box])
	
	# Direct Cuebid
	textobj.setTextOrigin(offset*2, h-74*offset)
	textobj.textLines(['','','','','_'*33])
	textobj.setTextOrigin(offset*18, h-74*offset)
	textobj.textLines(['',box+' '*13+box])
	
	# vs preempts
	textobj.setTextOrigin(w/4+offset, h-78*offset)
	textobj.textLines([' '*35+'Penalty'+box,'Conv. Takeout '+'_'*18,'Lebensohl 2NT Response'+box,'Other: '+'_'*26])
	
	c.drawText(textobj)
	
		
c = canvas.Canvas("precision-cc.pdf",pagesize=(w,h))  # inch = 72 points

c.setFont('Deja',fs)


makegrid(c)
addbluetext(c)
add2level(c)
addBold(c)
addblacktext(c)
addredtext(c)
drawLogo(c)
addocc(c)
c.showPage()
c.save()
