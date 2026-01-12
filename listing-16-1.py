def test_add_two_numbers():
    assert add(2, 3) == 5 

# The above will fail because the code does not exist
# Now write the minimum code that will succeed, and run the tests again
def add(a, b):
    return a + b

# Now you can make adjustments to the code, and use the test to assert it is functioning
# correctly, or add tests to test edge cases of the function
def add(a, b):
    if a < 0 or b < 0:
        return false
    return a + b
