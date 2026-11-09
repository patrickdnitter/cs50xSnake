class GameMode:
    def __init__(self, main_gamestate):
        self.main_gamestate = main_gamestate
        self.running = False

    def getGameState(self):
        return self.gamestate

    def getRunning(self):
        return self.running

    def setRunning(self, running_state):
        self.running = running_state

    def gameloop(self):
        pass

