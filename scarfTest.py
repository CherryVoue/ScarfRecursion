from KnitScarf import KnitScarf
import random
tests = int(input("How many tests?: "))
for i in range(tests):
    finalStitches = random.randint(0,1001)
    scarf = KnitScarf(finalStitches)
    stitches, rows = scarf.buildScarf()
    print(f"\nStitches in final row: {finalStitches}",
            f"Total stitches: {stitches}",
            f"Total rows: {rows}",
            sep = "\n")

