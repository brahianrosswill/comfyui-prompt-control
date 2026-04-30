import pytest

from prompt_control.macros import expand_macros


@pytest.mark.parametrize(
    "text, result",
    [
        ("DEF(X(a;b)=$1 $2 $3 d)X(A) X(A;B;C)", "A b $3 d A B C d"),
        (
            "DEF(MACRO()=[empty:$1:$2])MACRO MACRO(;) MACRO(;0.5) MACRO(a;0.5)",
            "[empty::$2] [empty::] [empty::0.5] [empty:a:0.5]",
        ),
        ("DEF(X=$1)DEF(Y()=$1)[X Y][X() Y()][X(1) Y(1)]", "[$1 ][ ][1 1]"),
    ],
)
def test_basic_macro(text, result):
    assert expand_macros(text) == result


def test_macro_recursion():
    with pytest.raises(ValueError) as c:
        expand_macros("DEF(X=recurse Y) DEF(Y=recurse X) X")
    assert "Unable to resolve DEFs" in str(c.value)
