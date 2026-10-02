class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        # could set both in hashtable with key being the letter and the number is the value then compare each one?
       # set the word aplha
        s = "".join(sorted(s))
        t= "".join(sorted(t)) 
        if len(s)!= len(t):
            return False
        i=0
        while i < len(s):
            if (s[i]==t[i]):
                i+=1
                continue
            else :
                return False
        return True

    
