import random, math
def recycle_points(L:list)->list:
	L.append(L[0])
	return L
def create_points()->list:
	result=[]
	for i in range(3):
		result.append((random.random(),random.random()))
	return result
def main():
	Sum=0
	for i in range(99999):
		points=iter(recycle_points(create_points()))
		point1=next(points)
		side=[]
		while True:
			try:
				point2=next(points)
				side.append(math.sqrt((point1[1]-point2[1])**2+(point1[0]-point2[0])**2))
				point1=point2
			except:
				break
		p=(sum(side))/2
		side=iter(side)
		Area=math.sqrt(p*(p-next(side))*(p-next(side))*(p-next(side)))
		Sum+=Area
	dif=Sum/99999-11/144
	print(dif)
	return dif

SUM=0
for i in range(10):
	SUM+=main()
print(SUM)

