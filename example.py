def add(a, b):
    return a + b


def divide(a, b):
    return a / b

def test_add_integers():
    assert add(2, 3) == 5
def test_add_numbers():
    assert add(2.24, 3.16) == 5.40
def test_add_string():
    assert add('space', 'ship') == 'spaceship'
def test_divide_integers():
    assert (divide(2,3) - 0.6666 ) < 1e-4

