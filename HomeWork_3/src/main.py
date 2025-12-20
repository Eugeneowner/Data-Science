import random

def getValidInput(enter: str) -> int:
    while True:
        try:
            value = int(input(enter))
            if value <= 0:
                raise ValueError("Enter a positive integer.")
            return value
        except ValueError as e:
            print(f"Error: {e}")


def generateStudents(n: int, lo: int = 50, hi: int = 100):
    return [(random.randint(lo, hi), random.choice([True, False])) for _ in range(n)]


def checkProfessorConsistency(records, minScore=50, maxScore=100):
    passingScores = [score for score, passed in records if passed]
    failingScores = [score for score, passed in records if not passed]

    if passingScores and failingScores:
        minPass = min(passingScores)
        maxFail = max(failingScores)
        if maxFail < minPass:
            return True, (maxFail + 1, minPass)
        return False, None

    if passingScores and not failingScores:
        minPass = min(passingScores)
        return True, (minScore, minPass)

    if failingScores and not passingScores:
        maxFail = max(failingScores)
        low = maxFail + 1
        high = maxScore
        return True, (low, high) if low <= high else (low, low)

    return True, (minScore, maxScore)


def printStudents(records):
    for i, (score, passed) in enumerate(records, start=1):
        status = "Passed" if passed else "Failed"
        print(f"Student {i}: {score} — {status}")


def saveResultsToFile(records, consistent, threshold_range, filename="results.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Students results:\n")
        for i, (score, passed) in enumerate(records, start=1):
            status = "Passed" if passed else "Failed"
            f.write(f"Student {i}: {score} - {status}\n")

        f.write("\nProfessor consistency check:\n")
        if not consistent:
            f.write("Inconsistent\n")
        else:
            f.write("Consistent\n")
            f.write(f"Threshold range: {threshold_range[0]} - {threshold_range[1]}\n")


def main():
    n = getValidInput("Enter number of students -> ")
    records = generateStudents(n, lo=50, hi=100)

    print("\nStudents results:")
    printStudents(records)

    consistent, thresholdRange = checkProfessorConsistency(records, minScore=50, maxScore=100)

    print("\nProfessor consistency check:")
    if not consistent:
        print("Inconsistent")
    else:
        print("Consistent")
        print(f"Threshold range: {thresholdRange[0]} - {thresholdRange[1]}")

    saveResultsToFile(records, consistent, thresholdRange)
    print("\nSaved to results.txt")


if __name__ == "__main__":
    main()