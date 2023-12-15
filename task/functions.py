def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """
    ans = 1
    n = len(x)
    m = len(x[0])
    
    i = 0
    j = 0
    while i < n and j < m:
        if x[i][j] != 0:
            ans *= x[i][j]
        i += 1
        j += 1

    return ans
    

    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    x.sort()
    y.sort()
    
    n = len(x)
    m = len(y)
    
    if n != m:
        return False
    for i in range(n):
        if x[i] != y[i]:
            return False
    return True

    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    
    ans = 0
    
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            ans = max(ans, x[i])
            
    return ans

    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    n = len(img)
    m = len(img[0])
    for i in range(n):
        for j in range(m):
            img[i][j][0] *= coefs[0]
            img[i][j][1] *= coefs[1]
            img[i][j][2] *= coefs[2]
    return img
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    a = []
    b = []
    c = 0

    prev = x[0]
    for el in x:
        if el == prev:
            c += 1
        else:
            a.append(prev)
            b.append(c)
            c = 1
        prev = el
    a.append(prev)
    b.append(c)

    return (a, b)
    pass

def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    res = []

    for fem in x:
        for boy in y:
            dx = fem[0] - boy[0]
            dy = fem[1] - boy[1]
            dist = (dx * dx + dy * dy) ** 0.5
            res.append(dist)
    return res
    pass
