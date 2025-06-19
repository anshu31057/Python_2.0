# dictionary
dict = {'anshu': 28 ,'rahul':34, 'raman':56}
print(dict)
#1
print(dict.get("anshu")) # print 28
#2
print(dict.keys()) # print 28,34,56
#3
print(dict.values()) # print anshu rahul raman
#4
print(dict.items()) # print whole dictionary
#5
dict.update({'sneha':89}) # update/ add this in dict
print(dict.items())
#6
del dict['rahul'] # del rahul from dict
print(dict.items())

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