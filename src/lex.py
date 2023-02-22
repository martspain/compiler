from utils import infixToPostfix
from automaton import Transition, State

operators = ['|', '.', '?', '+', '*', '^']

# The entry must be postfix
def AFN_from_RegEx(regexPostFix):
  stack = []
  counter = 1

  for c in regexPostFix:
    if c == '|': # Unify
      # a union b
      b = stack.pop()
      a = stack.pop()

      start1 = a.startNode
      start2 = b.startNode

      end1 = a.endNode
      end2 = b.endNode

      newStart = State(counter, [a, b])
      counter += 1
      newEnd = State(counter, [a, b])
      counter += 1

      stack.append(Transition(newStart, start1, 'ε'))
      stack.append(Transition(newStart, start2, 'ε'))
      stack.append(Transition(end1, newEnd, 'ε'))
      stack.append(Transition(end2, newEnd, 'ε'))

    elif c == '.': # Concat
      # a concat b
      pass
    elif c == '?': # Lambda
      # previous character union epsilon
      pass
    elif c == '*': # Kleene
      # loop on previous
      pass
    else:
      stack.append(Transition(State(str(counter)), State(counter+1), c))
      counter += 2
  
  for item in stack:
    if len(item.startNode.transitions) > 0:
      for elem in item.startNode.transitions:
        print(elem)
    print(item)    

regexTest = '(a|b)*abb'
AFN_from_RegEx(infixToPostfix(regexTest))

