import math
import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
x=(math.sqrt(a*b)/(math.exp(a)*b))+(a*math.pow(math.e,(2*a/b)))
print(x)