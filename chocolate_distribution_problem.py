import sys

def solution(chocolate_list, length, students):
    chocolate_list.sort()
    min_diff = sys.maxsize
    for i in range((length-students)+1):
        diff = chocolate_list[i+(students-1)] - chocolate_list[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

def solution1(arr, n, m):
    if (m == 0 or n == 0):
        return 0
    arr.sort()
    if (n < m):
        return -1
    min_diff = arr[n-1] - arr[0]
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
    return min_diff

if __name__ == '__main__':
    A = [3, 4, 1, 9, 56, 7, 9, 12]
    N = 8
    M = 5
    diff = solution(A, N, M)
    print("Minimum difference is", diff)
