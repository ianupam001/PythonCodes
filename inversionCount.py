class Solution:

    def inversionCount(self, arr, n):
        l = 0
        r = n-1
        count = self.countInversion(arr, l, r)
        return count

    def countInversion(self,arr, l, r):
        res = 0
        if l < r:
            m = l+(r-l)//2
            res +=self. countInversion(arr, l, m)
            res +=self. countInversion(arr, m+1, r)
            res +=self. countAndMerge(arr, l, m, r)
        return res

    def countAndMerge(self, arr, l, m, r):
        n1, n2 = m-l+1, r-m
        left =[]
        right =[]

        for i in range(0, n1):
            left[i] = arr[l+i]
        for i in range(0, n2):
            right[i] = arr[m+1+i]

        i, j, res = 0, 0, 0
        k = l

        while(i < n1 and j < n2):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                res += (n1-i)
                j += 1
            k += 1
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        return res

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a, n))
