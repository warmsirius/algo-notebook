#include <stdio.h>

int main(void) {
    //冒泡排序，升序
    int a[] = {5, 4, 3, 2, 0, 1};
    int n; //存放数组a中元素的个数
    int i; //比较的轮数
    int j; //每轮比较的次数
    int tmp; //交换数据时用于存放中间数据
    n = sizeof(a) / sizeof(a[0]);/*a[0]是int型, 占4字节, 所以总的字节数除以4等于元素的个数*/

    for (i = 0; i < n - 1; ++i) {
        //比较n-1轮
        for (j = 0; j < n - i - 1; ++j) {
            //每轮比较n-1-i次,
            if (a[j] > a[j + 1]) {
                tmp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = tmp;
            }
        }
    }

    for (i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
}