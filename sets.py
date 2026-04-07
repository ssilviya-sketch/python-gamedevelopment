#sets are an unorderd(no index) collection of unique elements 
# they are mutable that means you can add or remove elements after creation
#in python sets ar ecreated using curly brackets they can also be created using set function
s1 = {1,2,3,4,5}
print(s1)
s2 = set([1,2,3,4,4,5])
print(s2)
s3 = {5,1,3}
print(s3)
s3.add(33)
s3.remove(5)
print(s3)
fruits = {"apple","banana","pear"}
print(fruits)
s2.discard(6)
# if you try to remove something from a set that is not there then if yo use the discard function in not give you a error but if you use the romove eroor it will
#operations on sets
#union , it means addition of sets
print(s1.union(s2))
print(s1.union(s3))
#intersection , it means the common elements between two sets
print(s1.intersection(s3))
# difference of two sets is the elements that exist in set1 but not in set 2
print(s1.difference(s3))
#symmetric difference is union of sets-intersection of sets
print(s1.symmetric_difference(s3))