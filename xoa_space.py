
b = ["2","4"]
def xoa_1(x,arr):
	arr.pop(x)
	return arr
def xoa(x,arr):
	dai = len(arr)
	for i in range(x,len(arr)-1):
		arr[i] = arr[i+1]
	dai -= 1
	arr = [arr[i] for i in range(dai)]
	return arr
def index(x,mang):
	for i in range(len(mang)):
		if mang[i] == x:
			return i
def DEL_ARR(b_1,a_1):
	for i in range(len(b_1)):
		a_1 = xoa(index(b_1[i],a_1),a_1)
		
		print(f" xoa lan {i+1} mang moi la {a_1} phan tu xoa la {b_1[i]}")

	return a_1

def sort_asc(arr):
	for i in range(len(arr)-1):
		for j in range(i,len(arr)):
			if a[i] > a[j]:
				t = a[i]
				a[i] = a[j]
				a[j] =t
	return arr
	
def removeDou(a):
	for i in range(len(a)-1):
		for j in range(i+1,len(a)):
			if a[i] == a[j] :
				a = xoa_(j,a)
	return a

def xoa_2(x,arr):
	if x <= len(arr)-1:
		if x == 0:
			return arr[1:]
		elif x == len(arr)-1:
			return arr[0:len(arr)-1]
		else:
			return arr[0:x] +arr[x+1:]
	else:
		return False

a = [1,2,2,4,4,4,6,6,6,6,7,8,8,9]
def removeDoublicate(a):
	i = 0
	while i <  len(a)-1:
		if a[i] == a[i+1]:
			a = xoa_2(i+1,a)
			i = i
		else:
			i+=1
# 	return a
# print(removeDoublicate(a))
a = " 					  123  		  312312 			   123123  							  "
dau = [' ','\n','\t']
def xoa_dau(a):
	i = 0
	while i < len(a) -1:
		if a[i] in dau and a[i+1] not in dau:
			a = xoa_2(i,a)
			break
		elif a[i] in dau and a[i+1] in dau:
			a = xoa_2(i+1,a)
	return a

def xoa_mid(a):
	i = 0 
	while i < len(a) -1:
		if a[i] in dau and a[i+1] in dau:
			a = xoa_2(i+1,a)
			i = i
		else:
			i+=1
	return a

def xoa_cuoi(a):
	i = len(a)-1
	while i > 0:
		if a[i] in dau and a[i-1] not in dau:
			a = xoa_2(i,a)
			break
		elif a[i] in dau and a[i-1] in dau :
			a = xoa_2(i-1,a)
	return a
def string_handled(a):
	return xoa_cuoi(xoa_dau(xoa_mid(a)))
print(f"'{string_handled(a)}'")




	
# print(DEL_ARR(b,a))




