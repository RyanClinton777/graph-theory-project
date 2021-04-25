import ShuntingYard_RE
import ThompsonConstruct

if __name__ == "__main__":
    # List of ["Regular Expression", ["Strings"...]]
    # (Infix Regular Expressions)
    tests = [
                ["(a.b|b*)",   ["ab", "b", "bb", "a"]],
                ["a.(b.b)*.a", ["aa", "abba", "aba"]],
                ["1.(0.0)*.1", ["11", "100001", "11001"]]
    ]

    #For each test
    for test in tests:
        # Infix
        infix = test[0]
        print(f"infix:    {infix}")
        # Postfix
        postfix = ShuntingYard_RE.toPostfix(infix)
        print(f"postfix:  {postfix}")
        # NFA
        nfa = ThompsonConstruct.toNFA(postfix)
        print(f"thompson: {nfa}")
        # For each string for this test:
        for s in test[1]:
            # Match?
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
        # Newline
        print()