public class BFPRT{
    public static int[] getMinKNumsByBFPRT(int[] arr, int k){
        if(k < 1 || k > arr.length){
            return arr;
        }

        int minKth = getMinKthByBFPRT(arr, k);
        int[] res = new int[k];
        int index = 0;
        for (int i=0; i != arr.length; i++){
            if (arr[i] < minKth){
                res[index++] = arr[i];
            }
            for(; index!=res.length;index++){
                res[index] = minKth;
            }
            return res;
        }
    }

    public static int getMinKthByBFPRT(int[] arr, int K){
        int[] copyArr = copyArray(arr);
        return select(copyArr, 0, copyArr.length - 1, K -1);
    }

    public static int select(int[] arr, int begin, int end, int i){
        if (begin==end){
            return arr[begin];
        }

        int pivot = medianOfMedians(arr, begin, end);
        int[] pivotRange = partition(arr, begin, end, pivot);
        if (i >= pivotRange[0] && i <= pivotRange[1]){
            return pivotRange[1];
        }else if(i < pivotRange[0]){
            return select(arr, pivotRange[1]+1, end, i);
        }else{
            return select(arr, pivotRange[1] + 1, end, i);
        }
    }


    public static int medianOfMedians(int[] arr, int begin, int end){
        int num = end - begin + 1;
        int offset = num % 5 == 0 ? 1;
        int[] mArr = new int[num / 5 + offset];
        for (int i=0; i < mArr.length; i++){
            int beginI = begin + i * 5;
            int endI = beginI + 4;
            mArr[i] = getMedian(arr, beginI, Math.min(end, endI));
        }

        return select(mArr, 0, mArr.length-1, mArr.length / 2);
    }

    public static int[] partition(int[] arr, int begin, int end, int pivotValue){
        int small = begin - 1;
        int cur = begin;
        int big = end + 1;
        while (cur != big){
            if (arr[cur] < pivotValue){
                swap(arr, ++small, cur++);
            }else{
                swap(arr, cur, --big);
            }else{
                cur++;
            }
        }
        int[] range = new int[2];
        range[0] = small + 1;
        range[1] = big - 1;
        return range;
    }

    public static int getMedian(int[] arr, int begin, int end){
        insertionSort(arr, begin, end);
        int sum = end + begin;
        int mid = (sum/2) + (sum % 2);
        return arr[mid];
    }

}