def is_chars_unique(text):
    seen = {}
    for char in text:
        if char in seen:
            return False
        else:
            seen[char] = True
    return True

from nose.tools import assert_equal

class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(is_chars_unique)

#Trying to implement a memoise fibonacci solution:


memoise = {}
def fib(n):
    if n==2 or n==1:
        return 1
    if n in memoise:
        print(n,'IS MEMOISED')
        return memoise[n]
    else:
        result = fib(n-1)+fib(n-2)
        memoise[n] = result
        print(n,'NOT')
        return result
print(fib(10))
print('NOW 20 NOW 20 NOW 20')
print(fib(20))
