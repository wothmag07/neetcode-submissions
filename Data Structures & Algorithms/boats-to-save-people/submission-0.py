class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        count = 0
        lptr, rptr = 0, len(people)-1
        while lptr <= rptr:
            if people[lptr] + people[rptr] <= limit:
                count += 1
                lptr += 1
                rptr -= 1
            else:
                count += 1
                rptr -= 1
        return count


        