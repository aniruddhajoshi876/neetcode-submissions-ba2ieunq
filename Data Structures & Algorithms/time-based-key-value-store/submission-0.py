class TimeMap:

    def __init__(self):
        self.map={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #if key already exists, just add new timestamp
        if key in self.map:
            vals = self.map[key]
            vals.append((timestamp,value))
            return
        #if new key, add it to new list
        self.map[key] = [(timestamp,value)]
        return
    def search_time(self,key, timestamp):
        vals = self.map[key]
        l=0
        r=len(vals)-1
        if vals[l][0] > timestamp:
            return ''

        while l<=r:
            mid = (l+r)//2

            if vals[mid][0] == timestamp:
                return mid
            elif timestamp < vals[mid][0]:
                r = mid-1
            elif timestamp > vals[mid][0]:
                l = mid + 1
        return r


    def get(self, key, timestamp):
        
        if key not in self.map:
            return ''
        value = self.map[key]
        index = self.search_time(key, timestamp)
        if index == '' or index == -1:
            return ''
        res = str(value[index][1])
        return res