import math
import random
import pylab

class Location(object):
	def __init__(self,x,y): 
		self.x = float(x)
		self.y = float(y)
	def move(self, xc, yc):
		return Location(self.x + float(xc), self.y +float(yc))
	def getCoords(self):
		return self.x, self.y
	def getDist(self, other):
		ox, oy = other.getCoords()
		xDist = self.x - ox
		yDist = self.y - oy
		return math.sqrt(xDist**2 + yDist**2)

class CompassPt(object):
	possible = ('N', 'S', 'W', 'E')
	def __init__(self, pt):
		if pt in self.possible: self.pt = pt
		else: raise ValueError('in CompassPt __ini')
	def move(self, dist):
		if self.pt == 'N': return (0, dist)
		elif self.pt == 'S': return (0, -dist)
		elif self.pt == 'E': return (dist, 0)
		elif self.pt == 'W': return (-dist, 0)
		else: raise ValueError('in CompassPt move')

class Field(object):
	def __init__(self, drunk, loc):
		self.drunk = drunk
		self.loc = loc
	def move(self, cp, dist):
		oldLoc = self.loc
		xc, yc = cp.move(dist)
		self.loc = oldLoc.move(xc, yc)
	def getLoc(self):
		return self.loc
	def getDrunk(self):
		return self.drunk

class Drunk(object):
	def __init__(self, name):
		self.name = name
	def move(self, field, time = 1):
		if field.getDrunk() != self:
			raise ValueError('Drunk.move calleds with drunk not in field')
		for i in range(time):
			pt = CompassPt(random.choice(CompassPt.possible))
			field.move(pt, 1)


def performTrial(time, f):
	start = f.getLoc()
	distances = [0.0]
	for t in range(1, time + 1):
		f.getDrunk().move(f)
		newLoc = f.getLoc()
		distance = newLoc.getDist(start)
		distances.append(distance)
	return distances

drunk = Drunk('Smith')
for i in range(3):
	f = Field(drunk, Location(0, 0))
	distances = performTrial(500, f)
	pylab.plot(distances)
pylab.title('Random Walk')
pylab.xlabel('time')
pylab.ylabel('distance')

pylab.show()
