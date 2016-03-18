import random
import matplotlib.pyplot as plt
import numpy as np

class graham:
	def __init__(self):
		self.pSet = []
		self.hullPts = []

		self.incrementalMode = True
		self.computing = False

		cid = plt.figure(1).canvas.mpl_connect('button_press_event', self.onClick)



	@staticmethod
	def genRandPts(n):
		pts = []
		for i in range(n):
			pt = [random.randint(-100,100),random.randint(-1000,1000)]
			while (pt in pts): #guarantee unique points
				pt = [random.randint(-1000,1000),random.randint(-1000,1000)]

			pts.append([random.randint(-1000,1000),random.randint(-1000,1000)])

		return pts


	def setPointSet(self, p):
		self.pSet = p

	def addPoint(self, p):
		self.pSet.append(p)

	def onClick(self, event):
		if self.computing:
			return
		if (event.xdata is None) or (event.ydata is None):
			return
		if event.button == 1:
			self.pSet.append([event.xdata,event.ydata])
			plt.plot(event.xdata, event.ydata, 'bo')
			plt.figure(1).canvas.draw()
		if event.button == 3:
			self.computeHull()
			self.setupPlot()
			plt.figure(1).canvas.draw()



	def computeHull(self):
		self.computing = True

		if len(self.pSet) == 0:
			return

		# find the lowest point of the set - right wins ties
		lowIdx = self.findStartPoint()

		# put the bottom right point at the start of the pointSet
		self.pSet[0], self.pSet[lowIdx] = self.pSet[lowIdx], self.pSet[0]

		#used by the comparator
		self.lowPt = self.pSet[0]

		#sort by theta
		self.pSet = sorted(self.pSet[1:], cmp=self.thetaCompare)
		self.pSet.insert(0,self.lowPt)

		#initialize the hullStack with the lowest point and min theta point
		self.hullStack = []
		self.hullStack.append(0)
		self.hullStack.append(1)

		#iterate over the theta list and find the CH
		p = 2
		while p < len(self.pSet):
			#incremental mode
			if self.incrementalMode:
				self.hullPts[:] = []
				for h in self.hullStack:
					self.hullPts.append(self.pSet[h])
				self.setupPlot()
				plt.figure(1).canvas.draw()
				plt.waitforbuttonpress()

			hsSize = len(self.hullStack)
			if graham.isLeftTurn( self.pSet[self.hullStack[hsSize-2]], self.pSet[self.hullStack[hsSize-1]], self.pSet[p] ):
				self.hullStack.append(p)
			else:
				self.hullStack.pop()
				continue
			p+=1

		self.hullStack.append(0)


		self.hullPts[:] = []
		for h in self.hullStack:
			self.hullPts.append(self.pSet[h])

		self.computing = False


	def findStartPoint(self):
		lowIdx = 0
		min = self.pSet[0][1]
		for p in range(len(self.pSet)):
			if (self.pSet[p][1] < min):
				lowIdx = p
				min = self.pSet[p][1]
			if (self.pSet[p][1] == min):
				if (self.pSet[p][0] > self.pSet[lowIdx][0]):
					lowIdx = p

		return lowIdx


	def thetaCompare(self,a,b):
		lt = self.isLeftTurn(self.lowPt, a, b)

		if lt:
			return -1
		if not lt:
			return 1
		if lt is none: #collinear
			distA = sqrt(pow((a[0]-lowPt[0]),2) + pow((a[1]-lowPt[1]),2))
			distB = sqrt(pow((b[0]-lowPt[0]),2) + pow((b[1]-lowPt[1]),2))
			if (distA<distB):
				return -1
			else:
				return 1


	@staticmethod
	def isLeftTurn(a,b,c):
		d = graham.det( list(np.array(c)-np.array(a)), list(np.array(b)-np.array(a)) )
		if (d > 0):
			return False
		if (d < 0):
			return True
		return None


	@staticmethod
	def det(a,b):
		return ((a[0]*b[1])-(b[0]*a[1]))


	def setupPlot(self):
		plt.clf()
		x = []
		y = []

		if len(self.pSet) == 0:
			plt.plot(0,0)
			minX = -1
			minY = -1
			maxX = 1
			maxY = 1
			plt.axis([minX, maxX, minY, maxY])
			return
		for n in range(len(self.pSet)):
			x.append(self.pSet[n][0])
			y.append(self.pSet[n][1])


		hx = []
		hy = []
		for n in range(len(self.hullPts)):
			hx.append(self.hullPts[n][0])
			hy.append(self.hullPts[n][1])

		#minX = min(x) - 20
		#minY = min(y) - 20
		#maxX = max(x) + 20
		#maxY = max(y) + 20


		plt.plot(x,y,'bo')
		plt.plot(hx,hy,'b-')
		plt.plot(hx,hy,'ro')

		#plt.axis([minX, maxX, minY, maxY])


	def showPlot(self):
		plt.show()

	def refreshPlot(self):
		plt.figure(1).canvas.draw()

