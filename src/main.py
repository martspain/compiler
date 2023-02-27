from utils import infixToPostfix
from lex import AFN_from_RegEx

# regex = '(a|b)*abb'
# regex = '(x|t)+((a|m)?)+'
regex = '0?(1?)?0*'
postfix = infixToPostfix(regex)
print(postfix)
AFN_from_RegEx(postfix)
