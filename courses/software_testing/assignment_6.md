# test cases

| test id               | transitions | events        | inputs                 | expected output                               | states |
|-----------------------|-------------|---------------|------------------------|-----------------------------------------------|--------|
| classInstanceTest     | T1          | new Q5Class() |                        |                                               | S1     |
| arrayListInstanceTest | T2          | new int[]     | (-5, -1, 0, 1, 10)     |                                               | S2     |
| processListTest1      | T3          | processList() | list[-5, -1, 0, 1, 10] |                                               | S3     |
| addTotalTest1         | T5          | addTotal()    | -5                     | listTotal = -5, positiveNums = 0, average = 0 | S3     |
| addTotalTest2         | T5          | addTotal()    | -1                     | listTotal = -6, positiveNums = 0, average = 0 | S3     |
| addTotalTest3         | T4          | addTotal()    | 0                      | listTotal = -6, positiveNums = 1, average = 0 | S3     |
| addTotalTest4         | T4          | addTotal()    | 1                      | listTotal = -5, positiveNums = 2, average = 0 | S3     |
| addTotalTest5         | T6          | addTotal()    | 10                     | listTotal = 5, positiveNums = 3, average = 0  | S4     |
| setAverageTest1       | T8          | setAverage()  |                        | listTotal = 5, positiveNums = 3, average = 3  | S5     |
| processListTest2      | T3          | processList() | list[10, 1, 0, -1, -5] |                                               | S3     |
| addTotalTest1         | T4          | addTotal()    | 10                     | listTotal = 10, positiveNums = 1, average = 0 | S3     |
| addTotalTest2         | T4          | addTotal()    | 1                      | listTotal = 11, positiveNums = 2, average = 0 | S3     |
| addTotalTest3         | T4          | addTotal()    | 0                      | listTotal = 11, positiveNums = 3, average = 0 | S3     |
| addTotalTest4         | T5          | addTotal()    | -1                     | listTotal = 10, positiveNums = 3, average = 0 | S3     |
| addTotalTest5         | T7          | addTotal()    | -5                     | listTotal = 5, positiveNums = 3, average = 0  | S4     |
| setAverageTest1       | T8          | setAverage()  |                        | listTotal = 5, positiveNums = 3, average = 3  | S5     |
| getAverageTest1       | T9          | getAverage()  |                        | average = 3                                   | S6     |
