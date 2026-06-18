class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position[i] is the position of the ith car (in miles)
        speed[i] is the speed of the ith cart (in miles per hour)

        target: is the destination is at position (miles)

        rules: 
        1) car can not pass another car ahead of it (can only catch up and drive the same speed)
        2) car fleet is non-empty set of cars, 1 car is a fleet
        3) If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
        
        ex: target = 10, position = [1, 4], speed = [3, 2] ans = 1
        0 ---- 5 ---- 10 ---- 15 ---- 20
car 1(3)  1  4.  
car 2(2)     4. 6
        
        
        """
        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        for p, s in pairs:
            x = (target - p) / s

            stack.append(x)

            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)