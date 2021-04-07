""" DFA Automata Implementation """

class State:
    """ Nodes/States in an automaton """
    def __init__(self, isAccept, arrows):
        # Boolean, wether or not this state is an accept state
        self.isAccept = isAccept
        # dictionary of keys/labels:Other states
        self.arrows = arrows

class DFA:
    """ A DFA """
    def __init__(self, start):
        # Starting state
        self.start = start

    def match(self, s):
        """ check and return wether or not string s is accepted by our automaton """
        # Current state we are in
        currentState = self.start

        # Loop through characters in state
        for c in s:
            # Set current state as one pointed to by key of c
            currentState = currentState.arrows[c]
        # Return wether or not current state is an accept state
        return currentState.isAccept


def compile():
    """ Create our automaton """
    # Creating an DFA with two states; 0 points to themselves, and 1 points to the other. (checking for even parity) 
    # Compile is standard terminoligy for creating something like this

    # Create start state
    start = State(True, {})
    # Other state
    other = State(False, {})

    # The states point to themselves for 0
    start.arrows['0'] = start
    other.arrows['0'] = other

    # They point to eachother for 1
    start.arrows['1'] = other
    other.arrows['1'] = start

    a = DFA(start)

    return a

# Create automaton instance
myAuto = compile()
# tests
for s in ['1100', '11111', '', '1', '0']:
    result = myAuto.match(s)
    print(f"{s} accepted? {result}")

for s in ['000', '001', '010', '011', '100', '101', '110', '111']:
    result = myAuto.match(s)
    print(f"{s} accepted? {result}")