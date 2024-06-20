class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])
        print(self.map)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        res = ""
        datas = self.map[key]
        l, r = 0, len(datas) - 1

        while l <= r:
            m = (l + r) // 2
            if datas[m][1] <= timestamp:
                res = datas[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        # # last_time = timestamp
        # for l in range(timestamp, -1, -1):
        #     print(f"{l}")
        #     for data in datas:
        #         print(data)
        #         if data[1] == l:
        #             return data[0]
        # return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
