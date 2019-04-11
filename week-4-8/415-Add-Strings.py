class Solution(object):
    def addStrings(self, num1, num2):
        i, j, carry, res = 0, 0, 0, []

        while i < len(num1) or j < len(num2) or carry:
            if i < len(num1):                       # get the value and move on
                carry, i = carry+ord(num1[::-1][i])-48, i+1
            if j < len(num2):
                carry, j = carry+ord(num2[::-1][j])-48, j+1
            res += carry%10,
            carry //= 10                            # carry to next digit

        return "".join([chr(c+48) for c in res[::-1]])       
