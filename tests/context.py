import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).absolute().parent.parent))

from utils import reformat, get_puzzle, get_solutions, get_solution_script

solutions = get_solutions()

def obtain(index):
    script = get_solution_script(index)
    assert script is not None, "script is none"

    def _obtain(variable):
        var = script(variable)
        assert var is not None, f"{variable} is none"

        return var

    return _obtain
