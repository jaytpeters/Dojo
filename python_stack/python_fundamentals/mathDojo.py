class MathDojo:
    def __init__(self):
        self.result = 0
        pass
    def add(self,*vals):
        for val in vals:
            self.result += val
        return self
    def subtract(self, *vals):
        for val in vals:
            self.result -= val
        return self