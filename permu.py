class Fenwick:
    def __init__(self, n):
        sz = 1
        while sz <= n:
            sz *= 2
        self.size = sz
        self.data = [0] * sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i

class Solution2(object):
    def processQueries(self, queries, n):
        fenw = Fenwick(2 * n)
        vimap = {}
        for i in range(1, n + 1):
            fenw.add(i + n, 1)
            vimap[i] = i + n
        cur = n
        #print(vimap)
        #print(fenw)
        ans = []
        for q in queries:
            i = vimap.pop(q)
            rank = fenw.sum(i-1)
            #print(f"{i} ----- {rank}")
            ans.append(rank)
            
            vimap[q] = cur
            fenw.add(i, -1)
            fenw.add(cur, 1)
            cur -= 1
        return ans


s = Solution2()
queries = [3,1,2,1]
#queries = [7,5,5,8,3]
#m = 8
m=5
print(s.processQueries(queries,m))




# class BIT:
#     """Implementation of a Binary Indexed Tree (Fennwick Tree)"""
    
#     #def __init__(self, list):
#     #    """Initialize BIT with list in O(n*log(n))"""
#     #    self.array = [0] * (len(list) + 1)
#     #    for idx, val in enumerate(list):
#     #        self.update(idx, val)

#     def __init__(self, list):
#         """"Initialize BIT with list in O(n)"""
#         self.array = [0] + list
#         for idx in range(1, len(self.array)):
#             idx2 = idx + (idx & -idx)
#             if idx2 < len(self.array):
#                 self.array[idx2] += self.array[idx]

#     def prefix_query(self, idx):
#         """Computes prefix sum of up to including the idx-th element"""
#         idx += 1
#         result = 0
#         while idx:
#             result += self.array[idx]
#             idx -= idx & -idx
#         return result

#     def range_query(self, from_idx, to_idx):
#         """Computes the range sum between two indices (both inclusive)"""
#         return self.prefix_query(to_idx) - self.prefix_query(from_idx - 1)

#     def update(self, idx, add):
#         """Add a value to the idx-th element"""
#         idx += 1
#         while idx < len(self.array):
#             self.array[idx] += add
#             idx += idx & -idx


# if __name__ == '__main__':
#     array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
#     bit = BIT(array)
#     print('Array: [{}]'.format(', '.join(map(str, array))))
#     print()

#     print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_query(12)))
#     print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_query(6)))
#     print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_query(1, 5)))
#     print()
    
#     bit.update(4, 2)
#     print('Add {} to element at pos {}'.format(2, 4))
#     new_array = [bit.range_query(idx, idx) for idx in range(len(array))]
#     print('Array: [{}]'.format(', '.join(map(str, new_array))))
#     print()

#     print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_query(12)))
#     print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_query(6)))
#     print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_query(1, 5)))
#     print()

