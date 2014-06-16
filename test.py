from numpy import *
from matplotlib.pyplot import *
N=10000
xi=random.randn(N)
A=array([xi,ones(N)])
y=random.randn(N)*0.3+xi*2
w=linalg.lstsq(A.T,y)[0]
line=w[0]*xi+w[1]
e=line-y

figure()
subplot(211)
plot(xi,line,'r-',xi,y,'o')
subplot(212)
hist(e,50,normed=1,facecolor='g',alpha=0.75)
grid=(True)
show()

"""
file=open("TestFile.txt","w")
print>>file, y
print>>file, A
print>>file, w
"""

