class ListNode(object):
    def __init__(self,val,pointer):
        self.value = val
        self.pointer = pointer

nodeD = ListNode(31,None)
nodeC = ListNode(37,nodeD)
nodeB = ListNode(62,nodeC)
nodeA = ListNode(23,nodeB)

HeadNode = nodeA

#################### Simple Print ####################
def PrintNodes():
    print(nodeA.value ," -> ",nodeB.value ," -> ",nodeC.value ," -> ",nodeD.value ," -> NULL")

PrintNodes()


def CreateEmptyList():
    global HeadNode
    HeadNode = None


def PrintNodesWithLoopAndCount():
    global HeadNode
    Current = HeadNode
    CountNodes = 0
    if(Current != None):
        while(Current.pointer != None):
            print(Current.value)
            Current = Current.pointer
            CountNodes = CountNodes + 1

        CountNodes = CountNodes + 1
        print(Current.value)
        print ("Count: ", CountNodes)
    else:
        print("Empty list")

#PrintNodesWithLoopAndCount()

def InsertANode(Pos, N):
    global HeadNode
    Current = HeadNode
    PositionCounter = 1

    NodeX = ListNode(N, None)

    if(Pos == 0):
        HeadNode = NodeX
        NodeX.pointer = Current
    else:
        while(Pos > PositionCounter):
            Current = Current.pointer
            PositionCounter += 1

        NodeX.pointer = Current.pointer
        Current.pointer = NodeX


InsertANode(2,12345)
#InsertANode(1,55555)
PrintNodesWithLoopAndCount()

def FindANode(N):
    global HeadNode
    Current = HeadNode
    while((Current.pointer != None) and (Current.value != N)):
        Current = Current.pointer

    if ((Current.pointer == None) and (Current.value != N)):
        print (N," is not in the list")
    else:
        print("Found value:",Current.value)

FindANode(1111)
FindANode(31)

def DeleteANode(N):
    global HeadNode
    Previous = None
    Current = HeadNode

    if Current.value == N:
        HeadNode = Current.pointer
    else:
        while((Current.pointer != None) and (Current.value != N)):
            Previous = Current
            Current = Current.pointer
        Previous.pointer = Current.pointer

DeleteANode(12345)
PrintNodesWithLoopAndCount()