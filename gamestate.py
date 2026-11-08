class GameState:
    def __init__(self, surface, clock, highscore):
        self.screen = surface
        self.clock = clock
        self.highscore = highscore
        self.gamemodes = {}

    def getScreen(self):
        return self.screen

    def getClock(self):
        return self.clock

    # Add GameMode
    def addGameMode(self, gamemode_name, gamemode):
        self.gamemodes[gamemode_name] = gamemode

    # Return GameMode by name
    def getGameMode(self, gamemode_name):
        if gamemode_name in self.gamemodes:
            return self.gamemodes[gamemode_name]
        else:
            print("No GameMode found for GameMode " + gamemode_name)
            return None

    # Return if any GameMode is still activ
    def getStillRunning(self):
        for gamemode in self.gamemodes:
            if self.gamemodes[gamemode].getRunning():
                return True
        return False