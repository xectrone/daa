import java.util.Random;

public class Randomized_Quick_Sort {

    public static int N = 10;

    public static int[] sequence = new int[N];

    public static void QuickSort(int left, int right) {
        if (right - left <= 0) {
            return; // base case
        } else {
            Random rand = new Random();
            // Random pivot selection
            int pivotIndex = left + rand.nextInt(right - left + 1);
            swap(pivotIndex, right); // move pivot to the end
            int pivot = sequence[right];
            System.out.println("Pivot = " + pivot);

            int partition = partitionIt(left, right, pivot);

            QuickSort(left, partition - 1); // sort left side
            printSequence(sequence); // print sequence after sorting left side

            QuickSort(partition + 1, right); // sort right side
            printSequence(sequence); // print sequence after sorting right side
        }
    }

    public static int partitionIt(int left, int right, int pivot) {
        int leftPtr = left - 1;
        int rightPtr = right;

        while (true) {
            // move the left pointer to the right as long as the elements are smaller than the pivot
            while (sequence[++leftPtr] < pivot);
            // move the right pointer to the left as long as the elements are greater than the pivot
            while (rightPtr > 0 && sequence[--rightPtr] > pivot);

            // if pointers cross, the partitioning is done
            if (leftPtr >= rightPtr) {
                break;
            } else {
                swap(leftPtr, rightPtr); // swap elements
            }
        }

        swap(leftPtr, right); // swap the pivot to its correct position
        return leftPtr; // return the partition point
    }

    public static void swap(int dex1, int dex2) {
        int temp = sequence[dex1];
        sequence[dex1] = sequence[dex2];
        sequence[dex2] = temp;
    }

    static void printSequence(int[] sorted_sequence) {
        System.out.println();
        for (int i = 0; i < sorted_sequence.length; i++) {
            System.out.print(sorted_sequence[i] + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {
        System.out.println("Sorting of randomly generated numbers using RANDOMIZED QUICK SORT");

        Random random = new Random();
        // Generate random sequence
        for (int i = 0; i < N; i++) {
            sequence[i] = Math.abs(random.nextInt(100)); // generating random numbers between 0-99
        }

        System.out.println("\nOriginal Sequence: ");
        printSequence(sequence);

        System.out.println("\nSorting in progress...");
        QuickSort(0, N - 1);

        System.out.println("\nFinal Sorted Sequence: ");
        printSequence(sequence);
    }
}
