# def DAC_Max(a, l, r):
#     mx = -1
#
#     if (l >= r - 2):
#         if (a[l] > a[l + 1]):
#             return a[l]
#         else:
#             return a[l + 1]
#
#     # Logic to find the Maximum element
#     # in the given array.
#     mx = DAC_Max(a, l + 1, r)
#
#     if (a[l] > mx):
#         return a[l]
#     else:
#         return mx
#
#
# mn, mx = 0, -1
#
# # Initializing the array
# a = [70, 250, 50, 80, 140, 12, 14]
#
# # Recursion - DAC_Max function called
# print(DAC_Max(a, 0, 7))


def getTotalNumberOfSequences(m, n):
    # A special sequence cannot exist if length
    # n is more than the maximum value m.
    if m < n:
        return 0

    # If n is 0, found an empty special sequence
    if n == 0:
        return 1

    # There can be two possibilities : (1) Reduce
    # last element value (2) Consider last element
    # as m and reduce number of terms
    res = (getTotalNumberOfSequences(m - 1, n) + getTotalNumberOfSequences(m // 2, n - 1))

    return res

print(getTotalNumberOfSequences(10,4))