public static KMP{
    public static int getIndexOf(String s, String m){
        if (s == null || m == null || s.length() < 1 || m.length() < 1){
            return -1;
        }
        char[] str1 = s.toCharArray();
        char[] str2 = m.toCharArray();

        int str1i = 0;
        int str2i = 0;
        int[] next = getNextArray(str2);

        while (str1i <  str1.length && str2i < str2.length){
            if(str1[str1i] == str2[str2i]){
                str1i++;
                str2i++;
            } else if(next[str2i] == -1){
                str1i++;
            }else{
                str2i = next[str2i];
            }
        }
        return str2i == str2.length ? str1i - str2i : -1;
    }


    public static int[] getNextArray(char[] str2){
        if (str2.length == 1){
            return new int[] { -1 };
        }

        int[] next = new int[str2.length];
        next[0] = -1;
        next[1] = 0;
        int pos = 2;
        int cn = 0;
        while (pos < next.length){
            if (str2[pos - 1] == str2[cn]){
                next[pos++] == ++cn;
            }else if(cn > 0){
                cn = next(cn);
            }else{
                next[pos++] = 0;
            }
        }
        return next;

    }

}