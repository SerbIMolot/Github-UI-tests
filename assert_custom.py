
import sys
import traceback

class AssertFailed(Exception):

    def __init__(self, message="Test failed"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Test failed on: {self.message}'

def AssertTrue(result, msg= False):
    try:
            assert result == True
    except AssertionError:
        if msg: 
            print("Message: " + msg)
        print("Assert True failed")
        try:
            print("     Got: " + result)
        except:
            print("");
        raise AssertFailed(msg)
        return False

def AssertTest(exp_str, result, expect_to_fail, msg= False):

    try:
        if(expect_to_fail):
            assert exp_str != result
        else:
            assert exp_str == result
    except AssertionError:
        if msg: 
            print("Message: " + msg)

        print("Test with" + exp_str + " failed")
        print("     Got: " + result)
        raise AssertFailed(msg)
        return False

    print("Search test " + exp_str + " passed")
    return True
    