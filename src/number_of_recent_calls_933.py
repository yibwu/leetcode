class RecentCounter:

    def __init__(self):
        self.i = 0          # start index
        self.expect = None
        self.nums = []

    def ping(self, t):
        self.nums.append(t)
        if self.expect is None:
            self.expect = t + 3000
            
        if t < self.expect:
            return len(self.nums) - self.i
        elif t == self.expect:
            self.i += 1
            self.expect = self.nums[self.i] + 3000
            return len(self.nums) - self.i + 1
        else:
            while self.nums[self.i] + 3000 < t:
                self.i += 1
            self.expect = self.nums[self.i] + 3000
            return len(self.nums) - self.i


if __name__ == '__main__':
    obj = RecentCounter()
    inputs = [1, 100, 3001, 3002]
    for t in inputs:
        print(obj.ping(t))
