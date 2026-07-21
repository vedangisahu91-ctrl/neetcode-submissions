class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        wsum = 0
        count = 0
        left = 0
        right = len(people)-1
        while left <= right:
            wsum =  people[left] + people[right]
            if wsum > limit:
                count += 1
                right -= 1
                wsum = wsum-limit
            elif wsum <= limit:
                count += 1
                left += 1
                right -= 1
                wsum = 0
        # if wsum > limit:
        #     count += 1
        return count

12233