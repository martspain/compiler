from exceptions import *

# Shunting yard algorithm and several functions to format a regular expression and parse it to postfix
def getPrecedence(char):
  prec = 6

  if char == '(':
    prec = 1
  elif char == '|':
    prec = 2
  elif char == '.':
    prec = 3
  elif char == '?':
    prec = 4
  elif char == '*':
    prec = 4
  elif char == '+':
    prec = 4
  elif char == '^':
    prec = 5
  
  return prec

def formatRegEx(regex):
  allOperators = ['|', '?', '+', '*', '^']
  binaryOperators = ['^', '|']

  res = ''
  c1 = ''

  for i in range(len(regex)):
    c1 = regex[i]

    # Maintain within boundaries
    if i+1 < len(regex):
      c2 = regex[i+1]

      res += c1

      if c1 != '(' and c2 != ')' and c2 not in allOperators and c1 not in binaryOperators:
        res += '.'
      
  res += c1

  return res

def infixToPostfix(regex):
  openingParenthesisCount = regex.count('(')
  closingParenthesisCount = regex.count(')')

  if openingParenthesisCount != closingParenthesisCount:
    raise UnbanlancedParenthesis(regex, openingParenthesisCount, closingParenthesisCount)

  postfix = '' # Store the postfix result
  stack = []
  formattedRegEx = formatRegEx(regex)
  
  for c in formattedRegEx:
    if c == '(':
      stack.append(c)
    elif c == ')':
      while stack[len(stack) - 1] != '(': # Peek las element
        postfix += stack.pop()
      
      # Free the stack
      stack.pop()
    else:
      while len(stack) > 0:
        peekedChar = stack[len(stack) - 1]
        peekedCharPrecedence = getPrecedence(peekedChar)
        currentCharPrecedence = getPrecedence(c)

        if peekedCharPrecedence >= currentCharPrecedence:
          postfix += stack.pop()
        else:
          break
      stack.append(c)
  
  while len(stack) > 0:
    postfix += stack.pop()

  return postfix





