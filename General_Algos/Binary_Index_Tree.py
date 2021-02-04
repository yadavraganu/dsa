
def updateBIT(BIT,n,v,len):
	while len>=n:
		BIT[n-1]+=v
		n+=n&(-n)

def createBIT(Arr):
	BIT=[0]*len(Arr)
	for i in range(1,len(Arr)+1):
		updateBIT(BIT,i,Arr[i-1],len(Arr))
	return BIT

def getSum(BIT,i,len):
	s=0
	while i>0 and i<=len:
		s+=BIT[i-1]
		i-=i&(-i)
	return s

Arr=[1,2,3,6,7]
#[1,3,3,11,7]
BIT=createBIT(Arr)
print(getSum(BIT,6,len(BIT)))
