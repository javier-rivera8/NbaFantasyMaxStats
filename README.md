# NbaFantasyMaxStats
Python script that reads data from a file containing fantasy basketball statistics for various teams, processes the data to find the teams with the highest values for specific statistical categories, and then generates an image with the results.
# Import Statements:

The script starts by importing the necessary modules: Team (which seems to be a custom class), and the Image, ImageFont, and ImageDraw classes from the Pillow (PIL) library.
# Data Preparation:

The script opens a file named 'scores/week4.txt' for reading.
It defines a list of team names (teams) and their abbreviations (abrv), as well as a list of statistical categories (statName).
It initializes empty lists (teamsObj, maxTeam, and maxNames) to store Team objects, maximum statistical values, and corresponding team names.
# Data Processing:

The script iterates through each line in the file.
When it encounters a team name from the teams list, it creates a new Team object and appends it to the teamsObj list.
When it encounters a line matching an abbreviation from the abrv list, it sets a flag (stat) to indicate that statistical values will follow.
It then processes the subsequent lines, populating the statistical values for each team using the abbreviations as a marker.
After processing all statistical values for a team, it increments the teamsCounter to move to the next team.
# Finding Maximum Statistics:

The script goes through the teamsObj list and compares each team's statistical values against the current maximum values stored in the maxTeam dictionary.
If a team's value is greater than the current maximum, it updates the maxTeam dictionary and the corresponding team's name in the maxNames dictionary.
# Generating Image:

The script opens an image named "stats.jpeg" using Pillow.
It uses the ImageFont class to load fonts for the title and statistics.
It adds the title "Fantasy Stats" to the image using the provided font and positioning.
It then iterates through each statistical category, adding the corresponding team name and value to the image.
# Saving Image:

The final image is saved as "results/result.jpg".
<div align="center">
  <img src="https://github.com/javier-rivera8/NbaFantasyMaxStats/assets/112108705/66f2bbf3-c7e3-401b-931f-7ae9608456e8" alt="Fantasy Stats" width="670">
</div>
