import java.util.Arrays;


public class InsertionSort{
    // 方式1: 当前插入值，每步都进行值交换
    public static void insertionSort(int[] arr){
        if (arr == null || arr.length < 2){
            return ;
        }
        for (int i=1; i < arr.length; i++){
            for (int j = i-1; j >=0 && arr[j] > arr[j+1]; j--){
                swap(arr, j, j+1);
            }
        }
    }

     //方式2: 前面有序范围把大于需要插入的数往后移动一位，最后找到不大于插入的数就位置空，和插入的值进行交换
     public static void insertionSort(int[] arr){
        if (arr == null || arr.length < 2){
            return ;
        }
        for (int i=1; i < arr.length; i++){
            key = arr[i]
            for (int j = i-1; j >=0 && arr[j] > arr[j+1]; j--){
                swap(arr, j, j+1);
            }
        }
    }

    public static void swap(int[] arr, int i, int j){
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[i] = tmp;
    }
}
