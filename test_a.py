from abc import abstractmethod, ABC

class Y(ABC): # Y is totally abstract, so it can be ignored except for design purposes.

    @abstractmethod
    def print(self, name: str):
        pass

class X: # Any Y can be injected in to X's constructor, making it a top-level class rather than a base class

    def __init__(self, handler: Y, count: int = 1):
        self._count = count
        self._handler = handler

    def print(self, name: str):
        for _ in range(self._count):
            self._handler.print(name)

class MyY(Y): # MyY doesn't inherit any functionality, so it's simple to understand.

    def __init__(self, num_marks: int = 1):
        self._num_marks = num_marks

    def print(self, name: str):
        print(f"Hello, {name}{'!' * self._num_marks}")

class MyX(X): # think of this as a named preset for `X(MyY(5), 5)`
    def __init__(self):
        y = MyY(num_marks=5)
        super().__init__(y, count=5)

def test_x():

    # we could use a mocking framework for simplicity, but we don't need the injection techniques

    class MockY:
        def __init__(self):
            self.num_calls = 0
            self.names = []
        def print(self, name: str):
            self.num_calls += 1
            self.names.append(name)


    y = MockY()
    x = X(y, 5) # can test X independently from any specific Y implementation
    x.print("something")

    assert y.num_calls == 5

    for idx in range(5):
        assert y.names[idx] == "something"

def test_y():

    # we can test Y implementations independantly from X, narrowing down bugs.

    from contextlib import redirect_stdout
    from io import StringIO

    my_output = StringIO()

    with redirect_stdout(my_output):
        y = MyY(5)
        y.print("Chris")

    assert my_output.getvalue() == "Hello, Chris!!!!!\n"

def test_x_and_y_together():

    from contextlib import redirect_stdout
    from io import StringIO

    my_output = StringIO()

    with redirect_stdout(my_output):
        x = MyX()
        x.print("Chris")

    assert my_output.getvalue() == "Hello, Chris!!!!!\n" * 5

