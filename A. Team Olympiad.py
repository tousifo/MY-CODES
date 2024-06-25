def form_teams(n, skills):
    from collections import defaultdict
    
    programmers = []
    mathematicians = []
    sportsmen = []
    
    # Classify each child by their skill
    for i in range(n):
        if skills[i] == 1:
            programmers.append(i + 1)
        elif skills[i] == 2:
            mathematicians.append(i + 1)
        elif skills[i] == 3:
            sportsmen.append(i + 1)
    
    num_teams = min(len(programmers), len(mathematicians), len(sportsmen))
    

    print(num_teams)
    
    for i in range(num_teams):
        print(programmers[i], mathematicians[i], sportsmen[i])

n = int(input())
skills = list(map(int, input().split()))

form_teams(n, skills)
