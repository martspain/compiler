class State:
  def __init__(self, nodeLabel='', transitions=[]):
    self.label = nodeLabel
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

class Automaton:
  def __init__(self):
    self.states = []
    self.entryAlphabeat = ''
    self.initialState = None
    self.transitionFunc = []
    self.acceptanceStates = []