from graphshw import WeightedGraph
import math
import sys

# Student Name: <Andrew Decker>
#
# Programming Assignment 2
#
# What to Submit: Submit the following two files once you complete
# the assignment: (1) graphfileparser.py, which is the only python file
# you are modifying in this assignment; and (2) one highway graph
# file that you used when you tested your code.  I will test your code
# with additional, but I want to have a specific test case that you used.
#
# First note that you are not allowed to change the names, parameters,
# etc of functions you are implementing.  You are also not allowed to
# change names of any .py files included with the assignment.
# You are allowed, if you want, to implement additional helper
# functions if you find it useful.  The naming convention for helper
# functions is to start name with an _ to let other programmers know
# that you intend it to be private.
#
# Second, note that this is the only Python file you need to change
# in this assignment.  You are not allowed to modify the other Python
# files.  You are using the WeightedGraph class that is in the
# graphshw.py file, which I have imported for you at the top.
# The hw in the filename is just short for homework (it is slightly
# modified from the version used in the Graph videos).
# 
# You will probably need additional import statemments, such as the
# math module.  So just add those at the top.
#
#
# 1) Implement the haversine function based on its docstring
# to compute the haversine distance between two points on the Earth.  
#
# You can find the relevant equation for haversine distance
# at this link (and others):
# https://www.movable-type.co.uk/scripts/latlong.html
# That link also includes javascript for computing haversine distance.
# It should be straightforward to either implement based directly
# on the formula on that page or to translate the javascript at that
# link to Python.  Don't use symbols in your variable names (e.g., the
# javascript at that link uses some symbols for variable names---you will
# lose points if you do the same in your Python program).
# Note the constant R in the equation controls the units of measure,
# and make sure you set it appropriately for meters as indicated in the
# docstring below.
#
# See documentation of Python's math functions for any needed trig
# functions as well as degree to radian conversion:
# https://docs.python.org/3/library/math.html
#
# DO NOT have any print statements in this function.
#
#
#
# 2) Implement the parseHighwayGraphFile function.  
#
# Specifically, it should be able to parse a file of the format
# from this set of graphs: http://tm.teresco.org/graphs/ or
# https://travelmapping.net/graphs/
# 
# Details of the format itself can be found here:
# http://courses.teresco.org/metal/graph-formats.shtml
#
# Only worry about the "simple" format (and NOT the "collapsed" format).
# You might start by looking at one of the smaller graphs to see what
# the format looks like, such as Andora.
# First line of all files is: TMG 1.0 simple
# Second line tells you number of vertices and number of edges: V E
# The next V lines provide one vertex per line of
# the form: StringID  latitude  longitude
# You only really need the latitude and longitude values,
# and simply use 0 to V-1 as the vertex ids instead of the given strings.
# The next E lines provide the edges, one per line,
# of the form: from to aStringValueYouDontNeedForThisAssignment.
# You only need the from and to values, and not the 3rd value on the line.
# The from and to tell you the endpoints of an edge (0 based
# indices into the list of vertices).
# For each edge in this list add an edge to a WeightedGraph object.
# The WeightedGraph class is an undirected graph, so we're assuming that
# the roads in the highway graph data can be traversed in both directions.
# The weight for the edge should be the haversine distance
# (which you implemented a function to compute in Step 1).
#
# HINTS (for parsing input file):
# Among the Python videos within Blackboard, I have some videos that
# are especially useful for this assignment, including getting
# input from a file.  You can find additional Python file IO examples
# here: https://docs.python.org/3/tutorial/inputoutput.html
# Scroll to 7.2 and look at examples of open. Specifically, see example
# that uses "with" which has the advantage that Python will
# automatically close the file for you at the end of the with block, as
# I demonstrated in the Python videos within Blackboard.
#
# The read() method reads the entire file at once as a String.
# You will find it useful, however, to instead iterate over the lines
# of the file.  You can either use the readline() 
# method directly for this.  Or, see the example on that same page, and
# in the examples I did in the videos, that uses a loop of the form:
# for line in f (each iteration of this loop will automatically call
# readline() to get the next line of the file and loop will iterate
# over entire file).  However, you will probably find it more useful to
# explicitly call readline() directly since you will probably have a
# loop to get the vertex latitudes and longitudes, and then a second
# loop to get the edge data, rather than a single loop for the entire file.
#
# Useful methods for parsing the input graph file:
# The split method for Strings (which I also demonstrated in a video):
# https://docs.python.org/3/library/stdtypes.html#string-methods
#
# Converting String that is a number to a number type:
# float(s) will convert a string s that contains a floating-point
# number to a floating point number.
# For example, 
# s = "101.25"  # s is a string that happens to look like a floating-point number.
# v = float(s)  # v will now have the floating-point value 101.25
# Likewise, int(s) will do the same but for integer values.
# These are also demonstrated in my videos in Blackboard.
#
# DO NOT have any print statements in this function.
#
#
#
# 3) Implement the if __name__ == "__main__" : block at the bottom
# of this file to do the following:
#
# 3a) The if main block at the bottom should get the name of the
# highway graph file from the command line arguments.  See the video
# in Python that explains how to get command line arguments.
#
# 3b) Call your parseHighwayGraphFile function to parse that file,
# and to construct a WeightedGraph object from it.
#
# 3c) Write some code that outputs (with print statements) the degee
# of each vertex.  You can have one vertex per line, indicating its
# id (just its 0-based index) followed by its degree.  IMPORTANT:
# Your parseHighwayGraphFile function should NOT produce any output.
# You will have code in your if main block that will have the print
# statements.  The WeightedGraph class has a degree method, inherited from
# Graph that will return to you the degree of a vertex.
#
# 3d) Write some code to demonstrate that your haversine function works
# correctly.  This does not need to involve your graph.  You can simply
# pass some latitude longitude pairs and output results, but also make
# sure you do something to confirm they are correct (e.g., you can
# use the same lat/long values on the web-based calculator on the
# page linked to earlier and verify that your function computes the same).
#
#



def haversine(lat1, lng1, lat2, lng2) :
    """Computes haversine distance between two points in latitude, longitude.

    Keyword Arguments:
    lat1 -- latitude of point 1
    lng1 -- longitude of point 1
    lat2 -- latitude of point 2
    lng2 -- longitude of point 2

    Returns haversine distance in meters.
    """
    RConstant = 6371000

    latDiff = math.radians(lat2 - lat1)
    lngDiff = math.radians(lng2 - lng1)

    a = math.pow(math.sin(latDiff/2), 2) + ( math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.pow(math.sin(lngDiff/2), 2) )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = RConstant * c
    return d


def parseHighwayGraphFile(filename) :
    """Parses a highway graph file and return a WeightedGraph
    representing a highway graph.

    Keyword arguments:
    filename -- The name of the file containing the highway
    graph data relative to the current working directory.
    """
    # Hint 1: There are a couple different ways of structuring your code.
    # Here is one way:
    # - You could parse the file first, generating
    #   a list of the edges as tuples, and a list of the weights.
    # - Once you have that you can then do something like:
    #   g = WeightedGraph(v, edges, weights)
    #   assuming that v is the number of vertices, edges is a Python
    #   list of ordered-pairs (tuples with 2 components), and weights
    #   is a list of the edge weights in the same order as the edges list.
    #
    # Hint 2: Here is a different way of structuring this:
    # - You could parse the first couple lines to get the number of
    #   vertices v.
    # - The construct an initial graph with: g = WeightedGraph(v)
    # - And then continue parsing the file calling addEdge once for each
    #   edge.
    #
    #
    # Obviously replace this return statement with what is needed
    # to return the WeightedGraph object after you've constructed one.
    # So just replace None below with whatever you named your graph variable.
    with open(filename) as f:
        f.readline() #skip first line
        VEvals = f.readline().split()
        numVerts = int(VEvals[0])
        numEdges = int(VEvals[1])

        verts = []
        edges = []
        weights = []

        for v in range(0, numVerts):
            temp = f.readline().split()
            verts.append( (float(temp[1]), float(temp[2])) )
        for e in range(0, numEdges):
            temp = f.readline().split()
            start = int(temp[0])
            end = int(temp[1])
            edges.append( (start, end) )
            weights.append( haversine(verts[start][0], verts[start][1], verts[end][0], verts[end][1]) )
        
        g = WeightedGraph(numVerts, edges, weights)
    return g


if __name__ == "__main__" :
    #a
    file = sys.argv[1]
    #b
    g = parseHighwayGraphFile(file)
    #c
    numVerts = g.numVertices()
    for i in range(0, numVerts):
        print( str(i) + ", " + str(g.degree(i)) )
    #d
    dist = round(haversine(36.52, 42.333, 89.999, 3.003), 2)
    print(str(dist) + " m")
