
public static T1SubTreeEqualsT2{
    public static class Node{
        public int value;
        public Node left;
        public Node right;

        public Node(int data){
            this.value = data
        }
    }

    public static boolean isSubTree(Node t1, Node t2){
        String t1Str = serialByPre(t1);
        String t2Str = serialByPre(t2);
        return getIndexOf(t1Str, t2Str) != -1;

    };

    public static String serialByPre(Node head){
        if (head == null){
            return "#!"
        }
        String res = head.value + "!";
        res += serialByPre(head.left);
        res += serialByPre(head.right);
        return res;
    }

    public static getIndexOf(String str1, String str2){
        if(s1==null || s2==null || s1.length()<1 || s2.length()<1){
            return -1;
        }
        char[] ss = s1.toCharArray();
        char[] ms = s2.toCharArray();
        int[] nextArray = getNextArray(s2);
        int index = 0;

    }
}