class Move:

    def __init__(self, fromFieldId, toFieldId):
        assert fromFieldId != None
        assert toFieldId != None

        self.fromFieldId = fromFieldId
        self.toFieldId = toFieldId