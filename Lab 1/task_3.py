myList1 = ['Vineeth','Sirisha','Nikhitha','Raheshwari','Abhilash']
myList2 = ['Vineeth','Sirisha','Teja','Geetha','Avinash']

# myList1 = []
# myList2 = []
#
# count1 = input("\nEnter number of Student names to be enterted in Python\t-")
# stuPython = int(count1)
#
# print("Enter the Student names in Pyhton Class-")
# for i in range(stuPython):
#     name = input("\n")
#     myList1.append(name)
#
# count2 = input("\nEnter number of Student names to be enterted in Web\t-")
# stuWeb = int(count2)
#
# print("Enter the Student names in Web Class-")
# for i in range(stuWeb):
#     name = input("\n")
#     myList2.append(name)

#print(myList)

set1 = set(myList1)
set2 = set(myList2)
common = set1.intersection(set2)
union = set1.union(set2)

notCommon = union - common

print("In common with both class- {0}".format(common))
print("Not in Common with both classes- {0}".format(notCommon))














