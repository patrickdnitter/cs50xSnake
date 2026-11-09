class GameState:
    def __init__(self, surface, clock, highscore):
        self.screen = surface
        self.clock = clock
        self.highscore = highscore
        self.gamemodes = {}

    # Getter
    def getScreen(self):
        return self.screen
    def getClock(self):
        return self.clock
    def getHighscore(self):
        return self.highscore

    # Most Used Derivatives
    def getScreenSize(self):
        return self.screen.get_size()
    def blitScreen(self, surface, pos):
        self.screen.blit(surface, pos)
    def fillScreen(self, color):
        self.screen.fill(color)

    def getScores(self):
        return self.highscore.getScores()
    def addScore(self, name, score):
        self.highscore.addScore(name, score)
    def saveHighscore(self):
        self.highscore.save()

    def tick(self, value):
        self.clock.tick(60)

    # GameMde
    def getGameMode(self, name):
        if name in self.gamemodes:
            return self.gamemodes[name]
        else:
            print("No GameMode found for GameMode " + name)
            return None

    def addGameMode(self, name, gamemode):
        self.gamemodes[name] = gamemode

    # Return True if any GameMode is still activ
    def isRunning(self):
        for name in self.gamemodes:
            if self.gamemodes[name].getRunning():
                return True
        return False