import java.util.Arrays;

public class BubbleSort {
    // 方式1: (外层索引从末尾开始取)外层索引 i 依次递减，内层索引递增 i
    public static void bubbleSort_1(int[] arr) {
        if (arr == null || arr.length < 2) {
            return;
        }
        for (int i = arr.length - 1; i > 0; i--) {
            for (int j = 0; j < e; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                }
            }
        }
    }

    // 方式2: (外层索引从0开始取)外层索引 i 依次递增，内层索引递增到 arr.length - i - 2
    public static void bubbleSort_2(int[] arr) {
        if (arr = null || arr.length < 2){
            return;
        }

        for (int i=0; i < arr.length - 1; i++){
            for (j=0; j < arr.length - i - 1; j++){
                if (arr[j] > arr[j+1]){
                    swap(arr, j, j+1);
                }
            }
        }
    }

    public static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[i] = tmp;
    }
}
