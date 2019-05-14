'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
def solution(A):
    if A is None:
        return 1
    for index, value in enumerate(A):
        if len(A) < value <= 0:
            continue
        while index + 1 != A[index] and 0 < A[index] <= len(A):
            v = A[index]
            A[index], A[v - 1] = A[v - 1], A[index]
            A[v - 1] = v

            # Don't create infinite loops
            if A[index] == A[v - 1]:
                break

    for index, value in enumerate(A, 1):
        if value != index:
            return index
    return len(A) + 1

lst = list(range(1, 40000))
a = solution(lst)
print(a)
