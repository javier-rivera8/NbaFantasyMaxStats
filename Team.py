class Team:

  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.stats = {"FG%": 0, "FT%": 0, "3PM": 0, "REB": 0, "AST": 0, "STL": 0, "BLK": 0, "PTS": 0}

  def getName(self):
    return self.name

  def getPosition(self):
    return self.position

  def getStats(self):
    for key in self.stats.keys():
      print(key + " = " + str(self.stats[key]))

  def setStat(self, key, value):
    self.stats[key] = value

  def getStat(self, key):
    return self.stats[key]

# washulfio = Team("Washulfios", "(12-7-1, 3rd in West Division)")

# print(washulfio.getName())
# print(washulfio.getPosition())
# washulfio.setStat("FG%", 0.500)
# washulfio.getStats()


