""" Thompsons Construct algorithm - Converts a postfix regular expression to an NFA"""

class State:
    """ Nodes/States in an automaton 
        \nlabel = Label associated with state, since all arrows from it will have the same label. None = empty
        \narrows = list of arrows leading from this state
        \nisAccept = wether or not this is an accept state
    """
    def __init__(self, label, arrows, isAccept):
        # All arrows coming from a state will have the same label. None = empty
        self.label = label
        # States after this one
        self.arrows = arrows
        # Boolean, wether or not this state is an accept state
        self.isAccept = isAccept

class NFA:
    """ Non-deterministic Finite Automaton """
    def __init__(self, start, end):
        # Every NFA should have a clean start and end state to facilitate easy operations between them.
        # Start state
        self.start = start
        # End state
        self.end = end

    # Note: “takes 1 positional argument but 2 were given” error happens when you forget to put self as an arg in a class method
    def match(self, s):
        """ Return true if s is accepted by this NFA """
        
        # Keep track of current states. Initalise with start state
        # Loop through string (e.g. abba) one char at a time
        # States have one label. If current state has label of c, move to all connected states. 
        # If any states we land in have an empty arrow, immediately move to those, as well as staying in the original.
        # Now no longer in the first state,
        # If we end up in a state without a matching label, we are no longer in that state.
        
        # Note: I spent hours trying to figure this out (see old.py) but eventually found your old video from 2020, 
        #       I'm adapting from that because I couldn't figure it out myself (missed the recursion I think), hope that's ok.

        # Keep track of current states. Initalise with start state
        currentStates = []
        # Previous states
        previousStates = []

        # Start with start state. This adds the given state to the given list if it isn't already there, and looks for empty arrows, callings itself for those if any are found.
        self.addAndExploreState(self.start, currentStates)

        # Loop through characters in string
        for c in s:
            #print(f"For letter {c}") #DEBUG
            # Store previous states
            previousStates = currentStates
            # Reset current states
            currentStates = []

            # Loop through current states
            for state in previousStates:
                # If not None (redundent?)
                if state.label != None:
                    # If current state has a label matching the current character
                    if state.label == c:
                        self.addAndExploreState(state.arrows[0], currentStates)

        #Finally check if any of our states are accept states
        for state in currentStates:
            if state.isAccept == True:
                # Return true if any found
                return True
        # No accept states if code reaches this point, return false
        return False

    def addAndExploreState(self, state, stateList):
        """ This adds the given state to the given list if it isn't already there, and looks for empty (None) arrows, callings itself recursively for those if any are found.
            (I tried to figure this out on my own before the video came out but failed, see Old.py for attempts)
        """
        #print(f"STATE: isAccept: {state.isAccept}")
        # If state not already in stateList
        if state not in stateList:
            # Add it
            stateList.append(state)
            #If state label is empty/epsilon/None
            if state.label == None:
                # Loop through arrows of this state, calling this method again on those.
                for nextState in state.arrows:
                    self.addAndExploreState(nextState, stateList)



# (Not a class method)
def toNFA(postfix):
    """ Takes a postfix RE and converts it to an NFA """
    # NFA stack
    stack = []
    
    # Loop through characters
    for c in postfix:
        # Kleene star * --- Accept if 0 or more strings matching pattern are present (E.G. (a.b.)* would accept "" "ab", "abab" etc...)
        if c == "*":
            # Pop top NFA from stack
            nfa1 = stack[-1]
            stack = stack[:-1]

            # Create new start and states
            start = State(None, [], False)
            end = State(None, [], True)

            # New start state points at old start state, and the new end state
            start.arrows.append(nfa1.start)
            start.arrows.append(end)

            # Old end state no longer accepts
            nfa1.end.isAccept = False
            # Old end state now points to the new end state
            nfa1.end.arrows.append(end)
            # Old end state now points to old start state.
            nfa1.end.arrows.append(nfa1.start)

            # Create new NFA and append to stack
            nfa = NFA(start, end)
            stack.append(nfa)
        # Concatinate . --- Accept if both are true
        elif c == ".":
            # Pop last two NFAs from stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            nfa1 = stack[-1]
            stack = stack[:-1]

            # NFA1 end state no longer accept
            nfa1.end.isAccept = False
            # Make end state of 1 point to start of 2
            nfa1.end.arrows.append(nfa2.start)
            # Create a new NFA with start from 1 and end from 2
            nfa = NFA(nfa1.start, nfa2.end)

            # Put new NFA on the stack
            stack.append(nfa)
        # OR | --- Accept if either is true.
        elif c == "|":
            # Pop last two NFAs from stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            nfa1 = stack[-1]
            stack = stack[:-1]

            # Create end state
            end = State(None, [], True)
            # Create start state with arrows to the start states of both NFAs
            start = State(None, [nfa1.start, nfa2.start], False)

            # End states of both NFAs no longer accept states
            nfa1.end.isAccept = False
            nfa2.end.isAccept = False

            # Original end states now point to new end state
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)

            # Create new NFA and append to stack
            nfa = NFA(start, end)
            stack.append(nfa)
        # Non-special characters
        else:
            # Create standard NFA
            # Create end state
            end = State(None, [], True)
            # Create start state with label c, points to end state
            start = State(c, [end], False)
            # Create NFA from these states
            nfa = NFA(start, end)
            # Add to stack
            stack.append(nfa)
    
    # Ultimately there will only be one NFA, return it
    # Return None to indicate error if stack > 0
    if len(stack) > 1:
        return None
    else : 
        return stack[0]

# Tests # {"abba", "abbbba", "aba", "abb", "bba", "babba", "aa", ""}
if (__name__ == "__main__"):
    for postfix in {"abb.*.a."}:
        nfa = toNFA(postfix)

        print(f"---postfix:   {postfix}")
        print(f"---NFA:       {nfa}")
        for test in {"abba"}:
            print(f"{test}\taccepted by NFA?: {nfa.match(postfix)}")

# Note: shift+tab in VS code to shift code indentation left