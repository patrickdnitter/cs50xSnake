import csv

class Highscore:
    def __init__(self):
        # Load a File if there
        self.scores = self.load()

    # https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/
    def load(self):
        scores = []
        try:
            with open("highscore.csv", "r") as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    scores.append(row)
        except FileNotFoundError:
            pass

        return scores

    def addScore(self, name, score):
        new_score = {"name": name, "score": score}
        self.scores.append(new_score)
        print(self.scores)

    # https://www.geeksforgeeks.org/python/writing-csv-files-in-python/
    def save(self):
        with open("highscore.csv", 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["name", "score"])

            writer.writeheader()
            writer.writerows(self.scores)
