import sys
from random import randrange, uniform

#generate file with 10000 runs and 20000 genes
row=20000
col=10000
header="Name"
for i in range(col):
	header=header+'\t'+"SRR"+str(i)
print header
for i in range(row):
	temp="gene"+str(i)
	for j in range(col):
		temp=temp+'\t'+str(uniform(0, 10))
	print temp



