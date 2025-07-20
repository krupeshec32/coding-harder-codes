class Node_With_Neighbours:
    def __init__(self,val,neighbours):
        self.val = val
        self.neighbours= neighbours if neighbours is not None else []

