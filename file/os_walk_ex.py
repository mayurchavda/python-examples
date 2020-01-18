import os
for root, dirs, files in os.walk("/tmp", topdown=False):
   for name in files:
      #print(name)
      print(os.path.join(root, name))
   #for name in dirs:
   #   print(os.path.join(root, name))


for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))