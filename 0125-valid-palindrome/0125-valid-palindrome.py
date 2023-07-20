class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls=list(s)
        
        ll=''
        for i in ls:
            if i.isalnum():
                ll=ll+i.lower()
        if ll!=ll[::-1]:
            return False
        return True
        