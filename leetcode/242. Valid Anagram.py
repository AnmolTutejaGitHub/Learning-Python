#I WAS USING POP TO REMOVE I,J BUT STRINGS ARE IMMUTABLE SO TAKEN HELP TO CREATE REMOVE_CHAR FUNCTION 

class Solution(object):

    def isAnagram(self, s, t):
        def remove_char(input_string, char_to_remove):
            return input_string.replace(char_to_remove, '',1) #1 to replace only first occurence 
        if(len(s) != len(t)):
            return False
        for i in s:
            ans = False
            for j in t:
                ans = False
                #print(i, j)
                if(i == j):
                    ans = True
                    t = remove_char(t, i)  # to keep track of  TEST CASE : "ccac" "aacc"
                    break
                # print(ans)
                ans = False
                s = remove_char(s, j)
            if(ans == False):
                return False
        return True
