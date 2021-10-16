#!/usr/bin/python

"""
Python Functions and Recursions
"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""

def generateParenthesis(n):
    def paranthesis(string,left,right):
     if(right==n):
        print(string)
        return
     if(left<n):
        paranthesis(string+'(', left+1, right)
     if(right<left):
            paranthesis(string+')', left, right+1)
    paranthesis('',0,0)
            
n = 3
string = [""] * 2 * n
generateParenthesis(n)



"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""

def isPalindrome(s):
            length=len(s)
            left=0
            right=length-1
            s=s.lower()
            while(left<=right):
                if (not s[left]>='a' and s[left]<='n'):
                    left=left+1
                if (not s[right]>='a' and s[right]<='n'):
                    right=right-1
                    if(s[left]==s[right]):
                        left +=1
                        right -=1
                    else:
                            return False
                    return True





