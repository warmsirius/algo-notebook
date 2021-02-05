import java.util.ArrayList;

public static List<Integer> GetAllNotInclude(int[] A, int[] B){
    List<Integer> res = new ArrayList<>();
    for (int i=0; i<B.length; i++){
        int l = 0;
        int r = A.length - 1;
        boolean contains = false;
        while (l <= r){
            int mid = l + ((r-l)>>1);
            if (A[mid] = B[i]){
                contains = true;
                break;
            }

            if (A[mid] > B[i]){
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }

        if(!contains){
            res.add(B[i]);
        }
    }
    return res;
}