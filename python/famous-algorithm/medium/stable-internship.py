# https://www.algoexpert.io/questions/stable-internships

def stableInternships(interns, teams):
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentInternChoices = [0] * len(interns)

    teamMaps = []
    for team in teams:
        rank = {}
        for i, internNum in enumerate(team):
            rank[internNum] = i
        teamMaps.append(rank)

    while freeInterns:
        currentInternNum = freeInterns.pop()
        currentIntern = interns[currentInternNum]
        currentInternTeamPreference = currentIntern[currentInternChoices[currentInternNum]]
        currentInternChoices[currentInternNum] += 1

        if currentInternTeamPreference not in chosenInterns:
            chosenInterns[currentInternTeamPreference] = currentInternNum
            continue

        previousInternNumWithSameTeamPreference = chosenInterns[currentInternTeamPreference]

        previousInternRank = teamMaps[currentInternTeamPreference][previousInternNumWithSameTeamPreference]
        currentInternRank = teamMaps[currentInternTeamPreference][currentInternNum]

        if currentInternRank < previousInternRank:
            freeInterns.append(previousInternNumWithSameTeamPreference)
            chosenInterns[currentInternTeamPreference] = currentInternNum
        else:
            freeInterns.append(currentInternNum)

    return [[internNum, teamNum] for teamNum, internNum in chosenInterns.items()]