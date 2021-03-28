import Config
import Constant
import sys
from Color import Color

Config.Init()


def test_Color_return_a_Color():
    Config.Init()
    color = Color(Constant.WHITE)
    assert color.id == Constant.WHITE
    assert color.name == Constant.WHITENAME


def test_GetOpposite_Return_Oposite_Color():
    Config.Init()
    color = Color(Constant.WHITE)
    opposite = color.getOpposite()

    assert opposite.id == Constant.BLACK
    assert opposite.name == Constant.BLACKNAME

    oppositeTwice = opposite.getOpposite()
    assert oppositeTwice.id == Constant.WHITE
    assert oppositeTwice.name == Constant.WHITENAME

def test_Color_Raise_A_Error_When_Color_Is_UnKnown():
    Config.Init()

    try:
      Color(3)
    except Exception as err:
      assert err.args[0] == 'Color 3 is not found.'
