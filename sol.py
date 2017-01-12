def Binary_Search(arr, to_find):
    """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: arr (a list ordered from least to greatest)
             to_find (the item to find in arr)
     returns: index (int), x, s.t. arr[x] == to_find
              None(none-type) if for all x, arr[x] != to_find
    """
    x = len(arr) / 2
    i = 1
    found = True
    while arr[x] != to_find:

        if len(arr) == 1 and arr[x] != to_find:
            found = False
            break
        else:
            if to_find > arr[x]:
                arr = arr[x:]
            elif to_find < arr[x]:
                arr = arr[:x]
            else:
                return x
            x = len(arr) / 2
    if not found:
        return None


def Bisection(func, left_side, right_side, tol=1e-5):
    """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: func (a function)
             left_side (a value for the function to take on, it should have opposite sign from `right_side`)
             right_side (a value for the function to take on, it should have opposite sign from `left_side`)
             tol (a value for which the function should return once a value at least that distance from zero is found)
     returns: root (float), x, s.t. abs(func(x))<tol
              None(none-type) if func(left_side), func(right_side) < 0 or func(left_side), func(right_side) > 0
    """
    print 'hello world'
