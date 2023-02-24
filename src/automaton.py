class State:
  def __init__(self, nodeLabel='', transitions=[], startState=False, acceptance=False):
    self.label = str(nodeLabel)
    self.transitions = transitions
    self.starterNode = startState
    self.acceptanceNode = acceptance
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
  def __init__(self, exp='', alpha=[], initial=None, accept=None, states=[], trans=[]):
    self.expression = exp
    self.alphabeat = alpha
    self.initialState = initial
    self.acceptanceState = accept
    self.states = states
    self.transitions = trans