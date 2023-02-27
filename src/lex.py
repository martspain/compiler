from utils import infixToPostfix
from automaton import Transition, State, Automaton

operators = ['|', '.', '?', '+', '*', '^']
epsilonChar = 'ε'

# The entry must be postfix
def AFN_from_RegEx(regexPostFix):
  nodes = []
  transitions = []
  stack = []
  counter = 1

  for c in regexPostFix:
    if c == '|': # Unify
      # a union b
      b = stack.pop()
      a = stack.pop()

      start1 = a.initialState
      start2 = b.initialState

      end1 = a.acceptanceState
      end2 = b.acceptanceState

      newStart = State(counter)
      counter += 1
      newEnd = State(counter)
      counter += 1

      t1 = Transition(newStart, start1, epsilonChar)
      t2 = Transition(newStart, start2, epsilonChar)
      t3 = Transition(end1, newEnd, epsilonChar)
      t4 = Transition(end2, newEnd, epsilonChar)

      automaton = Automaton(
        f"({a.expression}|{b.expression})", # Expression
        a.alphabeat + b.alphabeat, # Alphabeat
        newStart, # Initial State
        newEnd, # Acceptance State
        a.states + b.states + [newStart, newEnd], # States
        a.transitions + b.transitions + [t1,t2,t3,t4] # Transitions
      )

      stack.append(automaton)

    elif c == '.': # Concat
      # a concat b
      b = stack.pop()
      a = stack.pop()

      aEndNode = a.acceptanceState
      bStartNode = b.initialState

      t1 = Transition(aEndNode, bStartNode, epsilonChar)

      automaton = Automaton(
        a.expression + b.expression,
        a.alphabeat + b.alphabeat,
        a.initialState,
        b.acceptanceState,
        a.states + b.states,
        a.transitions + b.transitions + [t1]
      )

      stack.append(automaton)

    elif c == '?': # Lambda
      # previous character union epsilon
      a = stack.pop()

      start1 = a.initialState
      end1 = a.acceptanceState

      newStart = State(counter)
      counter += 1
      newEnd = State(counter)
      counter += 1

      t1 = Transition(newStart, start1, epsilonChar)
      t2 = Transition(end1, newEnd, epsilonChar)
      epsiTran = Transition(newStart, newEnd, epsilonChar)

      automaton = Automaton(
        f"({a.expression})?",
        a.alphabeat,
        newStart,
        newEnd,
        a.states + [newStart, newEnd],
        a.transitions + [t1, t2, epsiTran]
      )

      stack.append(automaton)

    elif c == '*': # Kleene
      # loop on previous
      a = stack.pop()

      start = a.initialState
      end = a.acceptanceState

      newStart = State(counter)
      counter += 1
      newEnd = State(counter)
      counter += 1

      t1 = Transition(newStart, start, epsilonChar)
      t2 = Transition(newStart, newEnd, epsilonChar)
      t3 = Transition(end, start, epsilonChar)
      t4 = Transition(end, newEnd, epsilonChar)

      automaton = Automaton(
        f"({a.expression})*",
        a.alphabeat,
        newStart,
        newEnd,
        a.states + [newStart, newEnd],
        a.transitions + [t1, t2, t3, t4]
      )

      stack.append(automaton)

    elif c == '+':
      # loop on previous with 1 char guraranteed
      a = stack.pop()
      aCopy, newIter = a.copyAutomaton(counter)

      counter = newIter

      start = a.initialState
      end = a.acceptanceState

      preStart = aCopy.initialState
      preEnd = aCopy.acceptanceState

      newEnd = State(counter)
      counter += 1

      t1 = Transition(preEnd, start, epsilonChar)
      t2 = Transition(preEnd, newEnd, epsilonChar)
      t3 = Transition(end, start, epsilonChar)
      t4 = Transition(end, newEnd, epsilonChar)

      automaton = Automaton(
        f"({a.expression})+",
        a.alphabeat,
        preStart,
        newEnd,
        a.states + aCopy.states + [newEnd],
        a.transitions + aCopy.transitions + [t1, t2, t3, t4]
      )

      stack.append(automaton)

    else:
      a = State(counter)
      counter += 1
      b = State(counter)
      counter += 1

      t1 = Transition(a, b, c)

      automaton = Automaton(c, [c], a, b, [a,b], [t1])

      stack.append(automaton)

  # showAFN(nodes, transitions)
  # print(f"expr: {stack[0].expression}")
  stack[0].show()



# TEST TODO ELIMINATE THIS CODE
# for item in stack:
#   if len(item.startNode.transitions) > 0:
#     for elem in item.startNode.transitions:
#       print(elem)
#   print(item)

# regexTest = '(a|b)*abb'
# regexTest = 'a+'
# regexTest = '(x|t)+((a|m)?)+'

# postfix = infixToPostfix(regexTest)
# print('Postfix: ' + postfix)
# AFN_from_RegEx(postfix)

