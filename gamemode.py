class GameMode:
    running = False
    gamestate = None

    def __init__(self, gamestate = None):
        self.gamestate = gamestate
        if not self.validGameState():
            raise ValueError("Invalid GameState")

    def validGameState(self):
        return self.gamestate is not None

    # Return GameState
    def getGameState(self):
        return self.gamestate

    # Get the running
    def getRunning(self):
        return self.running

    def setRunning(self, running_state):
        self.running = running_state

    def gameloop(self):
        pass

