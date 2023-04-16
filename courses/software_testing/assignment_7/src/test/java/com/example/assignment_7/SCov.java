package com.example.assignment_7;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class SCov {

    // Purpose: JUnit test cases for Fun function in T3 for statement coverage
    @Test
    // Test Case ID: TC1
    // Purpose: Try to cover all statements
    // Test setup: Create an object of T3
    // Test inputs: x = 4, k = 2, y = 5
    // Expected Output: 7
    void TC1() {
        T3 obj = new T3();
        assertEquals(7, obj.Fun(4, 2, 5));
    }

    @Test
        // Test Case ID: TC2
        // Purpose: Try to cover all statements
        // Test setup: Create an object of T3
        // Test inputs: x = -1, k = 2, y = 0
        // Expected Output: -1
    void TC2() {
        T3 obj = new T3();
        assertEquals(-1, obj.Fun(-1, 2, 0));
    }

}