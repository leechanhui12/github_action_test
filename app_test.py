from app import add

def test_add():
    assertadd([2, 3]) == 5
    assertadd([-1, 1]) == 0
    assertadd([0, 0]) == 0  

    assertadd([2, 3, 1]) == 6
    assertadd([-1, 1, 1]) == 1
    assertadd([0, 0, 0]) == 0

test_add()