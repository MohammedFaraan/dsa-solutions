class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timemap[key]
        return self.binarySearch(arr, 0, len(arr) - 1, timestamp)

    def binarySearch(self, arr, l, r, t):
        res = ""

        while l <= r:
            m = (l + r) // 2
            val = arr[m]

            if val[0] == t:
                return val[1]
            elif val[0] < t:
                res = val[1]
                l = m + 1
            else:
                r = m - 1

        return res
