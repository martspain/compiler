import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

class State:
  def __init__(self, nodeLabel='', transitions=[]):
    self.label = str(nodeLabel)
    self.transitions = transitions

  def __repr__(self):
    return str(self.label)

class Transition:
  def __init__(self, fromNode, toNode, tranValue):
    self.startNode = fromNode
    self.endNode = toNode
    self.value = tranValue
  def __repr__(self):
    return f"Transition {self.startNode} - {self.value} -> {self.endNode}"
  def __eq__(self, other):
    return (self.startNode == other.startNode and self.endNode == other.endNode and self.value == other.value)

class Automaton:
  def __init__(self, expression='', alphabeat=[], initialState=None, acceptanceState=None, states=[], transitions=[]):
    self.expression = expression
    self.alphabeat = alphabeat
    self.initialState = initialState
    self.acceptanceState = acceptanceState
    self.states = states
    self.transitions = transitions
  
  def show(self):
    dot = graphviz.Digraph(comment=self.expression)

    for node in self.states:
      if node == self.acceptanceState:
        dot.node(node.label, shape='doublecircle')
      else:
        dot.node(node.label, shape='circle')

    for trans in self.transitions:
      dot.edge(trans.startNode.label, trans.endNode.label, constraint='false', label=trans.value)

    dot.node('', shape='point')
    dot.edge('', self.initialState.label, constraint='false')

    dot.render(directory='doctest-output', view=True)
