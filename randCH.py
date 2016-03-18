#!/usr/bin/python

from graham import graham

g = graham()

g.incrementalMode = False

g.setPointSet(graham.genRandPts(200))
#pts = [[0,0],[5,0],[6,3],[2,5],[-3,2]]
#g.setPointSet(pts)

g.computeHull()
g.setupPlot()
g.showPlot()
