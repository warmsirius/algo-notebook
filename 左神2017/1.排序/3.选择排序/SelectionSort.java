import java.util.Arrays;


public class SelectionSort{
    // 思路1: 每次选择出未排序范围最小的值
    public static void selectionSort_1(int[] arr){
        if (arr == null || arr.length < 2){
            return ;
        }
        for (int i=0; i < arr.length-1; i++){
            minIndex = i;
            for (int j=i+1; j<arr.length; j++){
                minIndex = arr[j] < arr[minIndex] ? j : minIndex;
            }
            swap(arr, i, minIndex)
        }
    }

    // 思路2: 每次选择出未排序范围最大的值
    public static void selectionSort_2(int[] arr){
        if (arr == null || arr.length < 2){
            return ;
        }
        for (int i=arr.length-1; i > 0; i--){
            maxIndex = i;
            for (int j=0; j<i; j++){
                maxIndex = arr[j] < arr[maxIndex] ? j : maxIndex;
            }
            swap(arr, i, maxIndex)
        }
    }


    public static void swap(int[] arr, int i, int j){
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}