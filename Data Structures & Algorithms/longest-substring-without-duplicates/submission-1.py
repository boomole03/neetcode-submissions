class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        sub_set = set()
        stack = []
        for i in s: 
            print('\n')
            print('i: ', i, ' sub_set: ', sub_set, ' stack: ', stack)
            if i in sub_set: 
                print('Inside for: ', i )
                m = max(m, len(stack))
                print('Lenght is: ', m)
                x = stack.pop(0)
                print('Stack: ', stack, 'Pop: ', x)
                sub_set.remove(x)
                print('Subset: ', sub_set)
                while x != i:
                    print('While loop x:', x)
                    x = stack.pop(0)
                    sub_set.remove(x)
            sub_set.add(i)
            stack.append(i)
            print('i: ', i, ' sub_set: ', sub_set, ' stack: ', stack, ' lenght: ', m)
        return max(m, len(stack))