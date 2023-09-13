from abc import abstractmethod

class X:

    def __init__(self, count: int = 5):
        self._count = count

    def print(self, name: str):
        for _ in range(self._count):
            self._print(name)

    @abstractmethod
    def _print(self, name: str):
        pass

class MyX(X):

    def __init__(self, count: int = 5, num_marks: int = 5):
        self._num_marks = num_marks
        super().__init__(count)

    def _print(self, name: str):
        print(f"Hello, {name}{'!' * self._num_marks}")

def test_x():
    # X is abstract, so we shouldn't really be calling it.
    x = X()
    x.print("Chris")

def test_y():
    # there is no Y to test
    pass

def test_x_and_y_together():

    # X and Y must always be tested together.

    from contextlib import redirect_stdout
    from io import StringIO

    my_output = StringIO()

    with redirect_stdout(my_output):
        x = MyX()
        x.print("Chris")

    assert my_output.getvalue() == "Hello, Chris!!!!!\n" * 5