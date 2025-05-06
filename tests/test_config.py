import pytest

class rangeError(Exception):
    def __init(self,message = "value not in range"):
        self.message = message
        super().__init__(self.message)
        
        
        
def test_generic():
    a = 2
    with pytest.raises(rangeError):
        if a not in range(3,10):
            raise rangeError
        
