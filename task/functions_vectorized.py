def prod_non_zero_diag_np(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Vectorized implementation.
    """
    bro = np.diagonal(x)
    zxc = bro[bro != 0]
    return np.prod(zxc)
    
    pass


def are_multisets_equal_np(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    x = np.sort(x)
    y = np.sort(y)
    
    return np.array_equal(x, y)
    
    pass


def max_after_zero_np(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    bro = x == 0

    bro = np.roll(bro, 1)
    bro[0] = False
    ans = np.max(x, where=bro, initial=0)

    return ans

    pass


def convert_image_np(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """
    
    return np.dot(img, coefs)

    pass


def run_length_encoding_np(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Vectorized implementation.
    """
    x = np.append(x, x[-1] + 1) #добавляем фиктивный чтобы не пропустить последний элемент
    d = np.diff(x)
    tmp = [-1] #добавляем фиктивный чтобы не пропустить первый элемент
    zxc = np.nonzero(d) #первые вхождения всех уникальных
    tmp = np.append(tmp, zxc)
    a = x[zxc] #все уникальные
    b = np.diff(tmp) #считаем кол-во вхождений
    return (a, b)

    pass


def pairwise_distance_np(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    n = len(x)
    m = len(y)
    tmp = np.reshape(y, (1, m, 2))
    bro1 = np.repeat(tmp, n, axis=0)



    bro2 = np.repeat(x, m, axis=0)

    bro1 = np.reshape(bro1, (n * m, 2))
    bro2 = np.reshape(bro2, (n * m, 2))

    res = bro1 - bro2
    res = res ** 2
    res = np.reshape(res, (2 * n * m))
    emp = np.arange(2 * n * m)
    #print(res)
    xs = res[emp % 2 == 0]
    ys = res[emp % 2 != 0]
    #print(xs)
    #print(ys)

    ans = (xs + ys) ** 0.5

    return ans
    pass