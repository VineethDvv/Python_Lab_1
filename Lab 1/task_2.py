def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


tp1 = ('John', ('Physics', 80))
tp2 = ('Daniel', ('Science', 90))
tp4 = ('John', ('Chemistry', 60))

count = input("\nEnter number of tuples to be enterted\t-")
noTup = int(count)

lt = []

lt = [tp1, tp2, tp4]
print(lt)

dictionary = {}
print(Convert(lt,dictionary))

for i in range(noTup):
    name = input("\nEnter the name\t-")
    subject = input("\nEnter the subject\t-")
    marks = input("\nEnter the marks\t-")
    tp = (name, (subject), int(marks))
    lt.append(tp)





