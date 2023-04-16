import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class BCov {

    // Purpose: JUnit test cases for Fun function in T3 for branch coverage

    @Test
        // Test Case ID: TC1
        // Purpose: Try to cover all branches
        // Test setup: Create an object of T3
        // Test inputs: x = 4, k = 2, y = 5
        // Expected Output: 7
    void TC1() {
        T3 obj = new T3();
        assertTrue(obj.Fun(4, 2, 5) == 7);
    }

    @Test
        // Test Case ID: TC2
        // Purpose: Try to cover all branches
        // Test setup: Create an object of T3
        // Test inputs: x = -1, k = 2, y = 0
        // Expected Output: -1
    void TC2() {
        T3 obj = new T3();
        assertTrue(obj.Fun(-1, 2, 0) == -1);
    }

}