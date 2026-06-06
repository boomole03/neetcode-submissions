class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0 
        right = len(s) -1 

        while(left < right):
            #check if the not alphanumeric:
            print('left: ', left, ' right: ', right)
            if(not s[left].isalnum()):
                print('in here for left')
                left +=1 
                continue

            if(not s[right].isalnum()):
                print('in here for right')
                right -=1 
                continue
            print('left letter: ', s[left], ' right letter: ', s[right])
            if (s[left].upper() == s[right].upper()):
                left += 1
                right -=1
            else:
                return False
        print('Break')
        return True
            
