from utils import infixToPostfix
from automaton import Transition, State
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

operators = ['|', '.', '?', '+', '*', '^']

def findInStack(elem, stack):
  result = False
  for obj in stack:
    if obj == elem:
      result = True
  
  return result

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

      start1 = a.startNode
      start2 = b.startNode

      start1.starterNode = False
      start2.starterNode = False

      end1 = a.endNode
      end2 = b.endNode

      end1.acceptanceNode = False
      end2.acceptanceNode = False

      newStart = State(counter, [a, b], True)
      if newStart not in nodes: nodes.append(newStart)
      counter += 1
      newEnd = State(counter, [a, b], False, True)
      if newEnd not in nodes: nodes.append(newEnd)
      counter += 1

      t1 = Transition(newStart, start1, 'ε')
      t2 = Transition(newStart, start2, 'ε')
      t3 = Transition(end1, newEnd, 'ε')
      t4 = Transition(end2, newEnd, 'ε')

      if t1 not in stack: stack.append(t1)
      if t2 not in stack: stack.append(t2)
      if t3 not in stack: stack.append(t3)
      if t4 not in stack: stack.append(t4)

      if t1 not in transitions: transitions.append(t1)
      if t2 not in transitions: transitions.append(t2)
      if t3 not in transitions: transitions.append(t3)
      if t4 not in transitions: transitions.append(t4)

    elif c == '.': # Concat
      # a concat b
      b = stack.pop()
      a = stack.pop()

      aEndNode = a.endNode
      bStartNode = b.startNode

      t1 = Transition(aEndNode, bStartNode, 'ε')

      if t1 not in stack: stack.append(t1)
      if t1 not in transitions: transitions.append(t1)

    elif c == '?': # Lambda
      # previous character union epsilon
      a = stack.pop()

      start1 = a.startNode
      end1 = a.endNode

      start1.starterNode = False
      end1.acceptanceNode = False

      newStart = State(counter, [a], True)
      if newStart not in nodes: nodes.append(newStart)
      counter += 1
      newEnd = State(counter, [a], False, True)
      if newEnd not in nodes: nodes.append(newEnd)
      counter += 1

      t1 = Transition(newStart, start1, 'ε')
      t2 = Transition(end1, newEnd, 'ε')
      epsiTran = Transition(newStart, newEnd, 'ε')

      if t1 not in stack: stack.append(t1)
      if t2 not in stack: stack.append(t2)
      if epsiTran not in stack: stack.append(epsiTran)

      if t1 not in transitions: transitions.append(t1)
      if t2 not in transitions: transitions.append(t2)
      if epsiTran not in transitions: transitions.append(epsiTran)

    elif c == '*': # Kleene
      # loop on previous
      a = stack.pop()

      start = a.startNode
      end = a.endNode

      start.starterNode = False
      end.acceptanceNode = False

      newStart = State(counter, [a], True)
      if newStart not in nodes: nodes.append(newStart)
      counter += 1
      newEnd = State(counter, [a], False, True)
      if newEnd not in nodes: nodes.append(newEnd)
      counter += 1

      t1 = Transition(newStart, start, 'ε')
      t2 = Transition(newStart, newEnd, 'ε')
      t3 = Transition(end, start, 'ε')
      t4 = Transition(end, newEnd, 'ε')

      if t1 not in stack: stack.append(t1)
      if t2 not in stack: stack.append(t2)
      if t3 not in stack: stack.append(t3)
      if t4 not in stack: stack.append(t4)

      if t1 not in transitions: transitions.append(t1)
      if t2 not in transitions: transitions.append(t2)
      if t3 not in transitions: transitions.append(t3)
      if t4 not in transitions: transitions.append(t4)

    elif c == '+':
      pass
    else:
      a = State(counter)
      counter += 1
      b = State(counter)
      counter += 2

      t1 = Transition(a, b, c)

      if t1 not in stack:
        stack.append(t1)
        if a not in nodes: nodes.append(a)
        if b not in nodes: nodes.append(b)

      if t1 not in transitions:
        transitions.append(t1)
  showAFN(nodes, transitions)

def showAFN(nodes=[], transitions=[]):
  dot = graphviz.Digraph()

  for nod in nodes:
    if nod.acceptanceNode:
      dot.node(nod.label, shape='doublecircle')
    else:
      dot.node(nod.label)

  for edge in transitions:
    dot.edge(edge.startNode.label, edge.endNode.label, constraint='false', label=edge.value)

  for item in transitions:
    if item.startNode.starterNode or item.endNode.acceptanceNode:
      print(item)
      print(str(item.startNode.starterNode) + '-' + str(item.endNode.acceptanceNode))
    print(item)


# TEST TODO ELIMINATE THIS CODE
# for item in stack:
#   if len(item.startNode.transitions) > 0:
#     for elem in item.startNode.transitions:
#       print(elem)
#   print(item)

regexTest = '(a|b)*abb'
# regexTest = 'a?'
AFN_from_RegEx(infixToPostfix(regexTest))

