# Class built to initialize local variables and separate recursion
class KnitScarf:
    def __init__(self, finalRowStiches):  # Sets default variables
        self.finalRowStitches = finalRowStiches
        self.currentStitches = 3
        self.currentRow = 1
        self.totalStitches = 3

    def buildScarf(self):  # Calculates total amount of stitches and rows based on amount of stitches in the last row
        self.currentRow += 1
        if self.currentRow % 2 == 0:
            self.currentStitches += 2
        self.totalStitches += self.currentStitches

        if self.currentStitches < self.finalRowStitches:  # Checks whether the current row's stitches match user input
            return self.buildScarf()

        return self.totalStitches+self.currentStitches, self.currentRow+1


def main():  # Gets user input, builds and calls KnitScarf class and buildScarf function, prints results to user
    finalRowStitches = int(input("Number of stitches in the final row: "))

    scarf = KnitScarf(finalRowStitches)
    totalStitches, totalRows = scarf.buildScarf()
    totalYarn = ((totalStitches/7)*4)/36
    print(f"{'Number of Rows:':<35} {totalRows}",
          f"{'Total number of stitches:':<35} {totalStitches}",
          f"{'Total number yarn yards needed:':<35} {totalYarn:.2f}",
          sep="\n")


if __name__ == "__main__":
    main()
