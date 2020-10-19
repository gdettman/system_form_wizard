class NotPositive(Exception):
    def __init__(self, message):
        self.message = message
    
class ExcessBlocks(Exception):
    def __init__(self, message):
        self.message = message

class EmptyFields(Exception):
    def __init__(self, message):
        self.message = message
 
def not_positive(*args):
    for arg in args:
        if arg > 0 and float(arg).is_integer():
            pass
        else:
            raise NotPositive("Not Positive")

def excess_blocks(model, systems, strings, blocks):
    if model == "LX" and systems * (strings * blocks) > 512:
        raise ExcessBlocks("Excess Blocks (max. 512 for LX)")
    elif model == "MX" and systems * (strings * blocks) > 200:
        raise ExcessBlocks("Excess Blocks (max. 200 for MX")