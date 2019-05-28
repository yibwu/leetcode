class Solution:
    
    def sum_even_after_queries(self, A, queries):
        res = []
        for q in queries:
            val = q[0]
            i = q[1]
            tmp = A[i]
            A[i] += val
            
            if not res:
                res.append(self.get_sum_of_even(A))
            else:
                if tmp % 2 == 0:
                    if A[i] % 2 == 1:
                        res.append(res[-1] - tmp)
                    else:
                        res.append(res[-1] + val)
                else:
                    if A[i] % 2 == 1:
                        res.append(res[-1])
                    else:
                        res.append(res[-1] + A[i])
        return res
        
    def get_sum_of_even(self, numbers):
        numbers = list(filter(lambda x: x % 2 == 0, numbers))
        return sum(numbers)


if __name__ == '__main__':
    obj = Solution()
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    res = obj.sum_even_after_queries(A, queries)
    print(res)
