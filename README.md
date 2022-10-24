# KnitScarf
A basic example of recursion and use of classes in python. The BuildScarf function continues to call itself until the current row of stitches matches that of what is passed into it, modifying variables initialized in the KnitScarf class with each iteration.
To build the scarf, the pattern is every positive row is equal to the previous row plus 2 stitches. Odd rows are equal to the previous row.

# scarfTest
Tests the KnitScarf class and buildScarf function with randomized amounts of stitches from 0 to 1001. Amount of tests are determined by user input. 1002 stitches and above exceeded maximum recursion depth on my computer. Max is set to 950 in test file, lower if necessary.
