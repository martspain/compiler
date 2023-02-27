import graphviz

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
  
  def copyAutomaton(self, startIndex=0):
    iterator = startIndex
    stateMapping = {}
    newStates = []
    newTransitions = []

    for state in self.states:
      newState = State(iterator)
      stateMapping[f"{state.label}"] = newState
      newStates.append(newState)
      iterator += 1

    for transition in self.transitions:
      newTrans = Transition(stateMapping[transition.startNode.label], stateMapping[transition.endNode.label], transition.value)
      newTransitions.append(newTrans)
    
    # Return automaton copy and new iterator
    return Automaton(self.expression, self.alphabeat, stateMapping[self.initialState.label], stateMapping[self.acceptanceState.label], newStates, newTransitions), iterator
  
  def show(self, graphComment=''):
    dot = graphviz.Digraph(comment=graphComment if graphComment != '' else self.expression)
    dot.attr(label=self.expression, rankdir='LR', ranksep='1', nodesep='1')
    dot.engine='dot'

    for node in self.states:
      if node == self.acceptanceState:
        dot.node(node.label, shape='doublecircle')
      else:
        dot.node(node.label, shape='circle')

    for trans in self.transitions:
      dot.edge(trans.startNode.label, trans.endNode.label, label=trans.value)

    # Add initial state shape
    dot.node('', shape='point')
    dot.edge('', self.initialState.label)

    dot.render(directory='nfa_output', view=True)
