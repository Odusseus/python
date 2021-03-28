import sys
import Constant
import Config

def test_Config_Default():
    Config.Init()

    assert Config.maxElement == 8
    assert Config.minElement == 1
    assert Config.maxFieldId == 64
    assert Config.minFieldId == 1
    assert Config.random == False
    assert Config.maxPiece == 0

def test_nextPiece():
    Config.Init()

    result = Config.nextPiece()
    assert result == 1
    assert Config.maxPiece == 1

def test_Config_With_Input():
    Config.Init(1, True)

    assert Config.maxElement == 1
    assert Config.random == True