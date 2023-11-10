class TimeMap(object):

    def __init__(self):
        self.hash_map = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        hash_map[foo] = {'4': bar,
                         '5': bar1,
                         '6': bar2,
                         }
        hash_map[6] = {'foo': bar2,
                         }
        hash_map[5] = {'foo': bar1,
                         }
        hash_map[4] = {'foo': bar,
                         }
        hash_map[foo] = 6 # points to the TOT

                     GET            SET
        New          O(1)          O(1)
        Del          O(1)          O(1)
        Not in       O(1) + O(1)
        """
        if timestamp not in self.hash_map:
            self.hash_map[timestamp] = {}
        self.hash_map[timestamp][key] = value
        self.hash_map[key] = timestamp
        print(self.hash_map)


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if timestamp in self.hash_map:
            if key in self.hash_map[timestamp]:
                print(f"found {self.hash_map[timestamp][key]}")
                return self.hash_map[timestamp][key]
            else:
                print(f"not found")
                return ""
        elif key in self.hash_map:
            if timestamp < self.hash_map[key]:
                print(f"not found")
                return ""
            print(f" found {self.hash_map[self.hash_map[key]][key]}")
            return self.hash_map[self.hash_map[key]][key]
        else:
            print(f"not found")
            return ""
        return self.hash_map[key]

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",5)
print(f"{obj.get('foo',4)}")