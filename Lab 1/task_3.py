myList1 = ['Vineeth','Sirisha','Nikhitha','Raheshwari','Abhilash']
myList2 = ['Vineeth','Sirisha','Teja','Geetha','Avinash']

#print(myList)

set1 = set(myList1)
set2 = set(myList2)
common = set1.intersection(set2)
union = set1.union(set2)

notCommon = union - common

print("In common with both class- {0}".format(common))
print("Not in Common with both classes- {0}".format(notCommon))














