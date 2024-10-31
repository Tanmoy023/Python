set1 = {1,3,2,4,7,5}
set2 = {2,4,6,8,7,}
print(set1,set2)

set_Union = set1.union(set2) # union mean total of two set
print(set_Union)
set_Intersection = set1.intersection(set2) # intersection mean common of two set
print(set_Intersection)
set_symmetric = set1.symmetric_difference(set2) # symmetric_difference mean uncommon element from set's
print(set_symmetric)
set_difference = set1.difference(set2) # difference mean which element set1 hav but set2 can't have
print(set_difference)
set_isdisjoint = set1.isdisjoint(set2) # if two set are completely different so isdisjoint return false
print(set_isdisjoint)
set_superset = set1.issuperset(set2) # set2's all element are not present in set1 so issuperset return false
print(set_superset)

# set1.update(set2)
# print(set1)