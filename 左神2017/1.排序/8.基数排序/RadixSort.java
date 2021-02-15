public class RadixSort{
    public static void radixSort(int[] arr, int begin, int end, int digit){
        final int radix = 10;
        int i = 0, j = 0,
        int[] count = new int[radix];
        int[] bucket = new int[end-begin+1];
        for (int d = 1; d <= digit; d++){
            for(i=0; i<radix; i++){
                j = getDigit(arr[i], d);
                count[j]++;
            }

            for(i=begin;i<=end;i++){
                count[i] = count[i] + count[i-1];
            }

            for(i=end; i >=begin; i--){
                j = getDigit(arr[i], d);
                bucket[count[j] - 1] = arr[i];
                count[j]--;
            }

            for(i=begin,j=0; i<=end, i++,j++){
                arr[i] = bucket[j];
            }
        }
    }

    public static int getDigit(int x, int d){
        return ((x/((int) Math.pow(10, d-1)) % 10));
    }

}