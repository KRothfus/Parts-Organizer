class Part:
    partTotal = 0
    def __init__(self, description: str, qty: int,quadrant: int,row: int,col: int):
        self.description = description
        self.qty = qty
        self.quadrant = quadrant
        self.row = row
        self.col = col
        self.partDict = {'description':description,'qty': qty,'location': [quadrant, row, col]}
        Part.partTotal += 1
        
    @classmethod
    def partCount(cls):
        print(cls.partTotal)

        