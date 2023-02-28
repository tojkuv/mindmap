import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Q5ClassTests {

    @Test
    /*
    Test case ID : addTotalTest1
    Purpose: test the functionality of `addTotal()` with a negative number
    Test Setup: a `Q5Class` instance
    Input:
        -5
    Expected Output:
        someClass.getTotal() == -5
        someClass.getPositiveNums() == 0
    States Covered: S3
    Author: Livan Torres
     */
    void addTotalTest1() {
        Q5Class someClass = new Q5Class();
        someClass.addTotal(-5);

        assertEquals(someClass.getTotal(), -5);
        assertEquals(someClass.getPositiveNums(), 0);
    }

    @Test
    /*
    Test case ID : addTotalTest2
    Purpose: test the functionality of `addTotal()` with zero
    Test Setup: a `Q5Class` instance
    Input:
        0
    Expected Output:
        someClass.getTotal() == 0
        someClass.getPositiveNums() == 0
    States Covered: S3
    Author: Livan Torres
     */
    void addTotalTest2() {
        Q5Class someClass = new Q5Class();
        someClass.addTotal(0);

        assertEquals(0, someClass.getTotal());
        assertEquals(1, someClass.getPositiveNums());
    }

    @Test
    /*
    Test case ID : addTotalTest3
    Purpose: test the functionality of `addTotal()` with a positive number
    Test Setup: a `Q5Class` instance
    Input:
        10
    Expected Output:
        someClass.getTotal() == 10
        someClass.getPositiveNums() == 0
    States Covered: S3
    Author: Livan Torres
     */
    void addTotalTest3() {
        Q5Class someClass = new Q5Class();
        someClass.addTotal(10);

        assertEquals(10, someClass.getTotal());
        assertEquals(1, someClass.getPositiveNums());
    }

    @Test
    /*
    Test case ID : setAverageTest1
    Purpose: test the functionality of `addTotal()` with a negative
    Test Setup: a `Q5Class` instance and correct implementation of `addTotal()`
    Input:
        None
    Expected Output:
        someClass.getTotal() == -5
        someClass.getPositiveNums() == 0
    States Covered: S5, S6
    Author: Livan Torres
     */
    void setAverageTest1() {
        Q5Class someClass = new Q5Class();
        someClass.addTotal(5);
        someClass.addTotal(3);
        someClass.addTotal(-2);
        someClass.setAverage();

        assertEquals(2.0, someClass.getAverage());
    }
}