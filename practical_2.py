def generateParenthesis(n, Open, close, s, ans):

    """
    recursive definition of balanced parenthesis for Opening brackets and closing brackets.
    Opening parenthesis can be maximum n and if both closing and opening parenthesis are equal to n then we can get our first combination, likewise run program
    recursively. And opening parenthesis can be maximum equal to n and according to that we need to arrange and generate combination of closing parenthesis.
    """

    if(Open == n and close == n):
        ans.append(s)
        return

    #Add opening parenthesis recursively
    if(Open < n):
        generateParenthesis(n, Open+1, close, s+"(", ans)

    #Add closing parenthesis recursively.
    if(close < Open):
        generateParenthesis(n, Open, close + 1, s+")", ans)


try:
     #generate exception for values entered is above 8 or less than 1 according to specified constraint.
     n = int(input("Enter No. of pair of Brackets:"))
     if n not in range(1,9):
         raise ValueError
     else:
         ans=[]
         generateParenthesis(n, 0, 0, "", ans)
         print(ans)
except ValueError:
     print("Enter Value from range 1 to 8")











