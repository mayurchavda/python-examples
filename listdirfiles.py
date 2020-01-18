import os
for root, dirs, files in os.walk("."):
	print(root)
	print(dirs)
	print(files)
print(temp)
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))
