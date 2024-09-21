# Problem : https://www.algoexpert.io/questions/tournament-winner

def tournamentWinner(competitions, results):
    """
    Determines the winner of a tournament based on the results of competitions.

    Thought Process:
    1. Initialize a dictionary (`hmap`) to keep track of the points for each team.
    2. Initialize variables to track the team with the maximum points.
    3. Iterate through the list of competitions and their results:
       - For each competition, identify the home and away teams.
       - Determine the winning team based on the result (0 for away team, 1 for home team).
       - Award 3 points to the winning team in the `hmap`. Use the `get` method to handle teams not already in the dictionary.
       - Check if the winning team has the maximum points and update the maximum if necessary.
    4. Return the name of the team with the highest points.

    This approach maintains a time complexity of O(n) and space complexity of O(m), optimizing the maximum team determination within the main loop.
    """
    hmap = {}
    max_team = ""
    max_points = 0

    for idx in range(len(competitions)):
        home_team = competitions[idx][0]
        away_team = competitions[idx][1]
        won_team = results[idx]
        if won_team == 0:
            hmap[away_team] = hmap.get(away_team, 0) + 3
            points = hmap[away_team]
        else:
            hmap[home_team] = hmap.get(home_team, 0) + 3
            points = hmap[home_team]

        if points > max_points:
            max_points = points
            max_team = home_team if won_team == 1 else away_team

    return max_team