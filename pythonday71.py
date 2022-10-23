
mylist = [10, 40, 758, "ks jaryal", 'himanshu sharma' "yash kalbande"]
print(mylist[4])
print(mylist[3])
print(mylist[-2])
print(mylist[-1])
print(mylist[4])
print(mylist[2])
print(mylist[2+1])
print(mylist[0+2])
print(mylist[0+3])
print(mylist)
mylist[0:4] = ["manoj k jayan", 'doremon']
print(mylist)
mylist[1:4] = [67, 789, 987, 'milley johonson', 'mickey mouse', 'whyyyy']
print(mylist)
mylist = [10, 40, 758, "eren yeger", 'captian levi', "bikasu"]
mylist1 = [56, 777, 90, "galadriel", 'sauron', "durin"]
mylist1.extend(mylist)
print(mylist)
print(mylist1)
# yhj
mylist = ["ff8fufhh", "koloindinia", "koijkl"]
print(mylist)
mylist.clear()
print(mylist)
print(10+20)
print(20-12)
print(30*5)
print(30**5)
print(40/5)
print(40//2)
print(56 % 2)
a = 27
print(a)
a += 3
print(a)
a -= 8
print(a)
a = a*5
print(a)
a = a/9
print(a)
a = a//9
print(a)
a = a % 3
print(a)
print(78999 == 7668)
print(67345 != 7)
print(67908 <= 798)
print(679809 >= 718)
print(679823 < 658)
print(67 > 759608)
# logical operatirs
x = 6
print(x < 4 and x > 0)
print(x < 2 and x > 9)
print(x < 9 and x > 57)
print(x < 1 and x > 2)
print(x > 3) and (x > 1)
print(x > 3) and (x > 5)
print(not (x > 2 or x > 3))
# identify operator
a = [10, 20]
b = [10, 20]
c = a
print(a is c)
print(b is a)
print(a == b)
print(a is not b)
print(a != b)
# membership operator
a = [1, 2, 3, 4, 5, 6, 7]
print(6 in a)
print(5 in a)
print(2 in a)
print(1 in a)
print(0 in a)
print(7 in a)
print(9 in a)
