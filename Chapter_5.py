# dictionary
anshu = {'anshu': 28 ,'rahul':34, 'raman':56}
print(anshu)
#1
print(anshu.get("anshu")) # print 28
#2
print(anshu.keys()) # print 28,34,56
#3
print(anshu.values()) # print anshu rahul raman
#4
print(anshu.items()) # print whole dictionary
#5
anshu.update({'sneha':89}) # update/ add this in dict
print(anshu.items())
#6
del anshu['rahul'] # del rahul from dict
print(anshu.items())

# SETS
ab = {1,3,5,66,77,66,8,34}
ad = {2,3,55,76,45,33,23}
ab.add(46)
ab.remove(34)
c = ab.union(ad)
d = ab.intersection(ad)
e = ab.difference(ad)
print(c)
print(d)
print(e)