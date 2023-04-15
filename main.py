from Team import Team
from PIL import Image, ImageFont, ImageDraw 

file = open('scores/week4.txt', 'r')
teams = [
  "Washington Washulfios", "Zzzz A mimil...casi", "San Diego Vegas",
  "El Prado Los PUPI", "Konoha Los mapaches", "Aibonito goats",
  "Hormigueros Oso Hormigueros", "Skull town Los Kabadis",
  "Alaska Los Talibanes", "Los Angeles Demons", "Pr Cabras locas",
  "Indiana Naptown"
]

abrv = ["WASh","PUTO","VEGA","PUPi","KOH","HOLa","OHDH","KBDI","YALa","MID","CL","INDy"]

statName = ["FG%","FT%","3PM","REB","AST","STL","BLK", "PTS"]
teamsObj = []

teamsCounter = 0
counter = 0
currentKey = ""
add = False
stat = False

for line in file.readlines():
  line = line.strip()
  if add:
    adding = Team(currentKey, line)
    teamsObj.append(adding)
    add = False

  if (line in teams):
    currentKey = line
    add = True
    
  if stat:
    if counter <= 7:
      teamsObj[teamsCounter].setStat(statName[counter], float(line))
      counter += 1
    else:
      counter = 0
      stat = False
      teamsCounter += 1
  
  if line in abrv:
    stat = True

file.close()

maxTeam = {"FG%": 0, "FT%": 0, "3PM": 0, "REB": 0, "AST": 0, "STL": 0, "BLK": 0, "PTS": 0}

maxNames = {"FG%": "", "FT%": "", "3PM": "", "REB": "", "AST": "", "STL": "", "BLK": "", "PTS": ""}

print("MaxStats")
print(" ")
for team in teamsObj:
  for key in statName:
    if team.getStat(key) > maxTeam[key]:
      maxTeam[key] = team.getStat(key)
      maxNames[key] = team.getName()

for i in range(len(statName)):
  print("Best " + statName[i] + " is " + maxNames[statName[i]] + " = " + str(maxTeam[statName[i]]))


my_image = Image.open("stats.jpeg")
title_font = ImageFont.truetype('ubuntu/Ubuntu-Bold.ttf', 150)

title_text = "Fantasy Stats"
image_editable = ImageDraw.Draw(my_image)
image_editable.text((1170/12,60), title_text, (255, 255, 255), font=title_font, align="center")

position = 0
title_font = ImageFont.truetype('ubuntu/Ubuntu-Bold.ttf', 40)

for index in range(len(statName)):
  title_text = maxNames[statName[index]]
  image_editable = ImageDraw.Draw(my_image)
  image_editable.text((1170/18,425 + position), title_text, (255, 255, 255), font=title_font, align="center")
  position += 140

position = 0

for index in range(len(statName)):
  title_text = str(maxTeam[statName[index]])
  image_editable = ImageDraw.Draw(my_image)
  image_editable.text((1170/2 + 250,425 + position), title_text, (255, 255, 255), font=title_font, align="center")
  position += 140

my_image.save("results/result.jpg")
