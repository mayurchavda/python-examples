words1 = set(open("some1.txt").read().split())
words2 = set(open("some2.txt").read().split())

print(words1)
print(words2)

duplicates = words1.intersection(words2)
uniques = words1.difference(words2)

print("Duplicates(%d) : %s"%(len(duplicates),duplicates))
print("\nUniques(%d) : %s"%(len(uniques),uniques))
print( words2.difference(words1))
print( words2.symmetric_difference(words1))
print( words2.union(words1))

