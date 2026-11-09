import csv

class Highscore:
    def __init__(self):
        # Load a File if there
        self.scores = self.load()

    def getScores(self):
        return self.scores

    # Reduces the length and sortes the array reversed
    def reduceScores(self, length):
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        self.scores = self.scores[:length]

    # Insert a new score than reduce it to top 10 if scores contains more 10
    def addScore(self, name, score):
        new_score = {"name": name, "score": score}
        self.scores.append(new_score)
        self.reduceScores(10)

    # Load with the csv library https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/
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

    # Save with the csv library https://www.geeksforgeeks.org/python/writing-csv-files-in-python/
    def save(self):
        with open("highscore.csv", 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["name", "score"])

            writer.writeheader()
            writer.writerows(self.scores)
