myDNA="ATTATTATTGC"
x= "Has a sticky end"
z= myDNA.count("T")
a= len(myDNA)

if myDNA.endswith("GC"):
	print(x+" "+str(z)+" "+str(a))


