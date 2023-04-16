package com.example.assignment_7;

public class T3 {
    public int Fun(int x, int k, int y) {
        int i;
        for (i = x; i < y; i++) {
            if (x%5 < 3) {
                k = y - x;
                y = y + i;
            }
            else {
                x = k - 2;
                y = y + x;
            }
            y = y - x;
            i = i + 2;
        }
        if (x < 0 || y < 0) {
            k = y - x;
        }
        else {
            x = y + k;
        }
        return x;
    }
}