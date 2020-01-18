from fabric.operations import local
result = local('ls -l', capture=True)
print("Content:\n%s" % (result, ))
def hello():
    print("Hello world!")
