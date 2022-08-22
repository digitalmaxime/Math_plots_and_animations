import cmath


#idea taken from 3Blue 1 brown's "Simpler quadratic formula"
def quadratic(a, b, c): # (a * x^2) + (b * x) + c
    # (x-r)(x-s) = x^2 -(r+s)x + r*s 
    r = None # first root
    s = None # second root
    m = (b/a)/2 # mean of the two root (middle point)
    print("mean between the 2 roots = " + str(m))
    try:
        d = cmath.sqrt((m**2) - c/a) # c = r*s = (m+d)(m-d) = m^2 - d^2
        print("standard deviation from the mean = " + str(d))
        r = m + d
        s = m - d
    except ValueError:
        print("oups.. something went wrong!")
    
    return (r, s) # return tuple with both answer

if __name__ == "__main__":
    res = quadratic(1, 0, -4) # x^2 + 6x + 10
    print(res)

