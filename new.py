# -*- coding: utf-8 -*-
import numpy
STOCK_PRICES = [100, 113, 110, 85, 105, 102, 86, 63, 81,
                101, 94, 106, 101, 79, 94, 90, 97]
STOCK_PRICE_CHANGES = [13, -3, -25, 20, -3, -16, -23, 18,
                       20, -7, 12, -5, -22, 15, -4, 7]


def find_maximum_subarray_brute(A, low=0, high=-1):
    maxSum = float("-inf")
    Sum = 0
    flag = 0
    if high == -1:
        high = len(A)-1
    if high == low:
        return (low, high, A[low])
    for i in range(high):
        for j in range(i+1, high+1):
            if A[i] > 0:
                flag = 1
            if(j-i == 1):
                Sum = A[i]+A[j]
            else:
                Sum += A[j]
            if (Sum > maxSum):
                maxSum = Sum
                startIndex = i
                endIndex = j
    if flag == 0:
        return (A.index(min(A)), A.index(min(A)), min(A))
    else:
        return (startIndex, endIndex, maxSum)


      
def find_maximum_crossing_subarray(A, low, mid, high):
    """
    Find the maximum subarray that crosses mid
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    """
    l_sum = float("-inf")
    this_sum = 0
    for i in range(mid, low-1, -1):
        this_sum += A[i]
        if this_sum > l_sum:
            l_sum = this_sum
            l_index = i
    this_sum = 0
    r_sum = float("-inf")
    for j in range(mid+1, high+1):
        this_sum += A[j]
        if this_sum > r_sum:
            r_sum = this_sum
            r_index = j
    return (l_index, r_index, l_sum+r_sum)


def find_maximum_subarray_recursive(A, low, high):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Recursive method from chapter 4
    """
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low+high) // 2
        l_low, l_high, l_sum = find_maximum_subarray_recursive(A, low, mid)
        r_low, r_high, r_sum = find_maximum_subarray_recursive(A, mid+1, high)
        c_low, c_high, c_sum = find_maximum_crossing_subarray(A, low, mid,
                                                              high)
        if l_sum >= r_sum and l_sum >= c_sum:
            return (l_low, l_high, l_sum)
        elif r_sum >= l_sum and r_sum >= c_sum:
            return (r_low, r_high, r_sum)
        else:
            return (c_low, c_high, c_sum)


def find_maximum_subarray_iterative(A, low, high):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Do problem 4.1-5 from the book.
    """
    max_so_far = 0
    max_ending_here = 0
    flag = 0
    for i in range(high):
        if A[i] > 0:
            flag = 1
        max_ending_here += A[i]
        if max_ending_here < 0:
            max_ending_here = 0
            start_index = i+1
            end_index = i+1
        if max_so_far < max_ending_here:
            if max_so_far == 0:
                start_index = i
                end_index = i
            else:
                end_index = i
            max_so_far = max_ending_here
    if flag == 0:
        return (A.index(min(A)), A.index(min(A)), min(A))
    else:
        return (start_index, end_index, max_so_far)


def square_matrix_multiply(A, B):
    """
    Return the product AB of matrix multiplication.
    """
    A = numpy.asarray(A)
    B = numpy.asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    C = [[0 for row in range(cols_B)]for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def add_matrices(A, B):
    n = len(A)
    C = [[0 for row in range(n)]for col in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j]+B[i][j]
    return C


def subtract_matrices(A, B):
    n = len(A)
    C = [[0 for row in range(n)]for col in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j]-B[i][j]
    return C


def split_matrix(A):
    n = len(A)
    a, b, c, d = A[:n//2, :n//2], A[:n//2, n//2:], A[n//2:, :n//2], A[n//2:,
                                                                      n//2:]
    return a, b, c, d


def square_matrix_multiply_strassens(A, B):
    """
    Return the product AB of matrix multiplication.
    Assume len(A) is a power of 2
    """
    A = numpy.asarray(A)
    B = numpy.asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    assert (len(A) & (len(A) - 1)) == 0, "A is not a power of 2"
    n = len(A)
    if n == 1:
        return square_matrix_multiply(A, B)
    else:
        a11, a12, a21, a22 = split_matrix(A)
        b11, b12, b21, b22 = split_matrix(B)
        s1 = subtract_matrices(b12, b22)
        s2 = add_matrices(a11, a12)
        s3 = add_matrices(a21, a22)
        s4 = subtract_matrices(b21, b11)
        s5 = add_matrices(a11, a22)
        s6 = add_matrices(b11, b22)
        s7 = subtract_matrices(a12, a22)
        s8 = add_matrices(b21, b22)
        s9 = subtract_matrices(a11, a21)
        s10 = add_matrices(b11, b12)
        p1 = square_matrix_multiply_strassens(a11, s1)
        p2 = square_matrix_multiply_strassens(s2, b22)
        p3 = square_matrix_multiply_strassens(s3, b11)
        p4 = square_matrix_multiply_strassens(a22, s4)
        p5 = square_matrix_multiply_strassens(s5, s6)
        p6 = square_matrix_multiply_strassens(s7, s8)
        p7 = square_matrix_multiply_strassens(s9, s10)
        temp_1 = add_matrices(p5, p4)
        temp_2 = add_matrices(temp_1, p6)
        c11 = subtract_matrices(temp_2, p2)
        c12 = add_matrices(p1, p2)
        c21 = add_matrices(p3, p4)
        temp_1 = add_matrices(p5, p1)
        temp_2 = add_matrices(p3, p7)
        c22 = subtract_matrices(temp_1, temp_2)
        temp_1 = numpy.hstack((c11, c12))
        temp_2 = numpy.hstack((c21, c22))
        c = numpy.vstack((temp_1, temp_2))
        return c
        pass


def test():
    print(find_maximum_subarray_brute(STOCK_PRICE_CHANGES,
                                      0, -1))
    print(find_maximum_subarray_recursive(STOCK_PRICE_CHANGES,
                                          0, len(STOCK_PRICE_CHANGES)-1))
    print(find_maximum_subarray_iterative(STOCK_PRICE_CHANGES,
                                          0, len(STOCK_PRICE_CHANGES)-1))
    A = numpy.matrix(numpy.arange(64).reshape(8,8))
    B = numpy.matrix(numpy.ones((8,8), dtype=numpy.int))
    print(square_matrix_multiply(A, B))
    print(square_matrix_multiply_strassens(A, B))
    pass


if __name__ == '__main__':
    test()
