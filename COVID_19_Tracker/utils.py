import geoplotlib

thedata = geoplotlib.utils.read_csv("result.csv")
geoplotlib.dot(thedata)
geoplotlib.show()
