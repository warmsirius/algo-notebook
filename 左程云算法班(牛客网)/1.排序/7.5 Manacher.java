public class Manacher{
    public static char[] manacherString(String str){
        char[] charArr = str.toCharArray();
        char[] res = new char[str.length() * 2 + 1];
        int index = 0;
        for (int i=0; i!=res.length; i++){
            rest[i] = (i&1) == 0? "#" : charArr[index++];
        }
        return res
    }

    public static int maxLcpsLength(String str){
        if (str == null || str.length() == 0){
            return 0;
        }

        char[] charArr = manacherString(str);
        int[] pArr = new int[charArr.length];
        int index = -1;
        int pR = -1;
        int max = Integer.MIN_VALUE;
        for (int i=0; i!=charArr.length; i++){

            //起码拥有的回文半径是多少
            pArr[i] = pR > i ? Math.min(pArr[2 * index - 1], pR - i) : 1,
            //统一情况处理4种
            while(i+pArr[i] < charArr.length && i - pArr[i] > -1){
                if (charArr[i+pArr[i]] == charArr[i-pArr[i]){
                    pArr[i]++;
                }else{
                    break;
                }
            }


            if (i + pArr[i] > pR){
                pR = i + pArr[i];
                index = i;
            }
            max = Math.max(max, pArr[i]);
        }
        return max-1;
    }

}