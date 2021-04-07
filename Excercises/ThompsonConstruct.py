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

    def match(s):
        """ Return true if s is accepted by this NFA """
        # ...


def toNFA(postfix):
    """ Takes a postfix RE and converts it to an NFA """
    # NFA stack
    stack = []
    
    # Loop through characters
    for c in postfix:
        # Kleene star * --- Accept if 0 or more strings matching pattern are present
        if c == "*":
            # Pop top NFA from stack
            nfa1 = stack[-1]
            stack = stack[:-1]

            # Create new start and states
            start = State(None, [], False)
            end = State(None, [], True)

            # New start state points at old start state, and the new end state
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa1.end)

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
            nfa1.end.arrows = [nfa2.start]
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
            start = State(c, [nfa1.start, nfa2.start], False)

            # End states of both NFAs no longer accept states
            nfa1.end.isAccept = False
            nfa2.end.isAccept = False

            # Original end states now point to new end state
            nfa1.end.arrows = [end]
            nfa2.end.arrows = [end]

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
        print(f"ERROR: Stack > 1 ({len(stack)})")
        return None
    else : 
        return stack[0]

# Tests
if (__name__ == "__main__"):
    for postfix in {"abb.*.a.", "100.*.1."}:
        print(f"postfix:   {postfix}")
        print(f"NFA:       {toNFA(postfix)}")

# Note: shift+tab in VS code to shift code indentation left