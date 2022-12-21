with open('input.txt', 'r') as f:
    input_file = f.read()

# Trim off the whitespace at the end, split parings into list tuples
rounds = [g.split(" ") for g in input_file.split("\n")][:-1]

# Value mappings for each shape you can throw
shapescores = { "R": 1,
                "P": 2,
                "S": 3}

# disgusting translator to get into a base form, could just translate to ABC instead but I'm bad
translator = {  'A': 'R',
                'X': 'R',
                'B': 'P',
                'Y': 'P',
                'C': 'S',
                'Z': 'S'}
# better option would've been to use matchloc and matchups to figure out if the winning matchup is adjacent but i'm lazy and that was part 2
winning = { 'R': 'S',
            'S': 'P',
            'P': 'R'}

# returns scores based on round results. checks tie > win > lose
def matchup(p1, p2):
    if p1 == p2:
        return 3
    if winning[p2] == p1:
        return 6
    return 0
# -----------------------------------------------
# location in the matchups list for the given hand, so that we can ignore OOB
matchloc = {'R': 3,
            'S': 4,
            'P': 5 }
# RSPRSPRSP, winning matchup is to the right, losing is to the left. start at 3 so you can always go left or right
matchups = ['R', 'S', 'P'] * 3

# if we know how we want the game to end up, use this to determine which shape from matchups using matchloc + outcomes
outcomes = {"Z": -1,
            "Y": 0,
            "X": 1}

# this is garbage but it works, thank god we don't need performant code yet
score1 = 0
score2 = 0
for r in rounds:
    p1, p2 = r
    t1, t2 = translator[p1], translator[p2]
    o = outcomes[p2]
    v2 = matchups[matchloc[t1] + o]

    score1 += matchup(t1, t2) + shapescores[t2]
    score2 += matchup(t1, v2) + shapescores[v2]
print(f"Part 1: {score1}")
print(f"Part 2: {score2}")


