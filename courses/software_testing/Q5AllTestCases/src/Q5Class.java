public class Q5Class {
    private int total = 0;
    private int numsAdded = 0;
    private int positiveNums = 0;
    private float average = 0;

    // add a new number to the total
    public void addTotal(int num) {
        total += num;
        numsAdded += 1;

        if (num >= 0) {
            positiveNums += 1;
        }
    }

    // gets the total
    public int getTotal() {
        return total;
    }

    // sets the average of the numbers
    public void setAverage() {
        average = (float) total / numsAdded;
    }

    // returns the average
    public float getAverage() {
        return average;
    }

    // returns the number of positive values
    public int getPositiveNums() {
        return positiveNums;
    }

    // process a given list and calculates the total and average
    public void processList(int[] list) {
        for (int num : list) {
            addTotal(num);
        }

        setAverage();
    }
}