from .context import get_puzzle, solutions

index = 0
solution = solutions[index]

def test_utils():
    puzzle = get_puzzle(index)
    result = solution(puzzle)
    assert result is not None, "result is none"
    a, b = result

    assert a == "a", "a is not 'a'"
    assert b == "b", "b is not 'b'"
