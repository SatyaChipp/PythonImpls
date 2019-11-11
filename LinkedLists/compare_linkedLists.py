def compare(headA, headB):
        nodeA = headA
        nodeB = headB
        while True:
            if not nodeA and not nodeB:
                return True
            elif (nodeA and nodeB) and (nodeA.data == nodeB.data):
                nodeA = nodeA.get_next()
                nodeB= nodeB.get_next()
            else:
                return False
