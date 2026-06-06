class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        n cars traveling on a one lane highway

        position[i] = where the ith car is in miles
        speed[i] = how fast ith car is going

        target = destinatin in miles

        target = 10, position = [1,4], speed = [3,2]

        0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10
                                                c
                                                x
        """
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) # in order to get the cars further ahead given you can't over take cars
        stack = []

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()


        return len(stack)