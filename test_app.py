from app import add, subtract

def test_add():
    assert add(2, 3) == 5
    print("✅ test_add passed!")

def test_subtract():
    assert subtract(5, 2) == 3
    print("✅ test_subtract passed!")

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("✅ All tests passed!")
