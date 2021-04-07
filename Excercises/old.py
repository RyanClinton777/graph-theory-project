# --- Attempt 1
# Loop through characters in states
        for c in s:
            #print(f"---Character {c}")
            # Go through NFA node-by-node, following arrows if they match s, or moving immediately if it is an empty state.
            # We are in multiple states at once, so we do this in each state we are currently in

            # For each state
            for state in currentStates:
                print(f"States Occupied: {len(currentStates)}, arrows: {len(state.arrows)}")
                #stateBuffer = currentStates
                
                # If state label matches our character
                if state.label == c:
                    # Current states becomes all states with arrows to them, since this algorithm ensures that they will all have the same label.
                    currentStates = [state]

                    for morestate in state.arrows:
                        if morestate.label == None:
                            print("\tEmpty arrow found")
                            currentStates.append(morestate)
                
                else: currentStates.remove(state)

# --- Attempt 2
# Keep track of current states. Initalise with start state
currentStates = [self.start]
# State buffer - states we will be on in the next iteration
nextStates = []

    # Loop through string (e.g. abba) one char at a time
for c in s:
    print(f"For letter {c}")

    # Store current states
    currentStates = nextStates
    # Reset buffer
    nextStates = []

    # Loop through current states - (for loop was running twice and converting the element from a state to a list the second time, no idea why so I switched to a range loop)
    for i in range(len(currentStates)):
        print(f"\tType: {type(currentStates[i])}, len: {len(currentStates)}")
        # If current state has a label matching the current character
        if currentStates[i].label == c:

            # ---
            # Move to all connected states. 
            for arrow in currentStates[i].arrows:
                # Add to state buffer
                nextStates.append(arrow)

                # If empty arrows, immediately go to them and add them as well
                if arrow.label == None:
                    # Add every e arrow linked state (conscutive e arrows possible? Ignoring for now)
                    for eArrow in arrow.arrows:
                        nextStates.append(eArrow)
            # ---

#Finally check if any of our states are accept states
for state in currentStates:
    if state.isAccept == True:
        # Return true if any found
        return True
# No accept states if code reaches this point, return false
return False