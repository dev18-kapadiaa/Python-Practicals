
# def generateParenthesis(N):
#     stack = []
#     result = []
#
#     def recursion(openBrackets, closedBrackets):
#         if openBrackets == closedBrackets == N:
#             result.append("".join(stack))
#             return
#
#         if openBrackets < N:
#             stack.append("(")
#             recursion(openBrackets + 1, closedBrackets)
#             stack.pop()
#
#         if closedBrackets < openBrackets:
#             stack.append(")")
#             recursion(openBrackets, closedBrackets + 1)
#             stack.pop()
#
#
#
#     recursion(0,0)
#     return result
#
#
# try:
#     n = int(input("Enter No. of pair of Brackets:"))
#     if n not in range(1,9):
#         raise ValueError
#     else:
#         answer = generateParenthesis(n)
#         print(answer)
# except ValueError:
#     print("Enter Value from range 1 to 8")

#Alternative-2


def generateParenthesis(n, Open, close, s, ans):

	if(Open == n and close == n):
		ans.append(s)
		return

	if(Open < n):
		generateParenthesis(n, Open+1, close, s+"(", ans)

	if(close < Open):
		generateParenthesis(n, Open, close + 1, s+")", ans)


try:
     n = int(input("Enter No. of pair of Brackets:"))
     if n not in range(1,9):
         raise ValueError
     else:
         ans=[]
         generateParenthesis(n, 0, 0, "", ans)
         print(ans)
except ValueError:
     print("Enter Value from range 1 to 8")











