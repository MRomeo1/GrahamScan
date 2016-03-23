# GrahamScan #
Graham scan programming project for computational geometry

### Overview ###
Graham Scan is an O(n log n) algorithm for computing convex hulls.

### Implementation Details ###
This implementation of the Graham Scan algorithm uses Python to compute the comvex hull and MatPlotLib to display the results and allow the user to interact with the plot.

### Usage ###
To display the interactive plot, run the file showPlot.py.  To generate a random set of points and compute their Convex Hull, run randCH.py.  These simple source files will initialize the graham class (contained in graham.py) and show its plot.

To add a point the plot, use the left mouse button.  To compute the convex hull using the Graham Scan algorithm, use the right mouse button.  If incremental mode is enabled (a boolean flag that can be toggled on or off in graham.py), the algorithm will execute one step at a time and show the results as it executes.  To advance to the next iteration in the execution, click the mouse button.
