from utils import infixToPostfix

# regex = '(a|b)*abb'
regex = '(x|t)+((a|m)?)+'

print(infixToPostfix(regex))