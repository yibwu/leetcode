class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        self.add_counter_to_people(people)
        sorted_arr, unsorted_arr = [], people
        self.iter_recur(sorted_arr, unsorted_arr)
        return sorted_arr

    def iter_recur(self, sorted_arr, unsorted_arr):
        if unsorted_arr:
            i = self.find_first_person(unsorted_arr)
            tmp_arr = unsorted_arr[i][:2]
            import copy
            sorted_arr.append(copy.deepcopy(tmp_arr))
            unsorted_arr.pop(i)
            for p in unsorted_arr:
                if p[0] <= tmp_arr[0]:
                    p[2] -= 1
            self.iter_recur(sorted_arr, unsorted_arr)

    def add_counter_to_people(self, people):
        for p in people:
            p.append(p[1])

    def find_first_person(self, people):
        first_person = people[0]
        index, i = 0, 1

        while i < len(people):
            p = people[i]
            if p[2] < first_person[2]:
                first_person = p
                index = i
            elif p[2] == first_person[2] and p[0] < first_person[0]:
                first_person = p
                index = i
            else:
                pass
            i += 1
        return index


if __name__ == '__main__':
    o = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ret = o.reconstructQueue(people)
    print(ret)
