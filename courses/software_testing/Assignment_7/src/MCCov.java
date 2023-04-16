import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class MCCCov {

    // Purpose: JUnit test cases for Fun function in T3 for MCC coverage

    @Test
        // Test Case ID: TC1
        // Purpose: Try to cover MCC
        // Test setup: Create an object of T3
        // Test inputs: x = 4, k = 2, y = 5
        // Expected Output: 7
    void TC1() {
        T3 obj = new T3();
        assertTrue(obj.Fun(4, 2, 5) == 7);
    }

    @Test
        // Test Case ID: TC2
        // Purpose: Try to cover MCC
        // Test setup: Create an object of T3
        // Test inputs: x = -1, k = 2, y = 0
        // Expected Output: -1
    void TC2() {
        T3 obj = new T3();
        assertTrue(obj.Fun(-1, 2, 0) == -1);
    }
    @Test
        // Test Case ID: TC3
        // Purpose: Try to cover MCC
        // Test setup: Create an object of T3
        // Test inputs: x = 5, k = 2, y = -10
        // Expected Output: 5
    void TC3() {
        T3 obj = new T3();
        assertTrue(obj.Fun(5, 2, -10) == 5);
    }

    @Test
        // Test Case ID: TC4
        // Purpose: Try to cover MCC
        // Test setup: Create an object of T3
        // Test inputs: x = -5, k = 2, y = -10
        // Expected Output: -5
    void TC4() {
        T3 obj = new T3();
        assertTrue(obj.Fun(-5, 2, -10) == -5);
    }
}