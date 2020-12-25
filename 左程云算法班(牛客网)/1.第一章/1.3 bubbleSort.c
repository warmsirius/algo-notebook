#include "stdio.h"

void swap(int *t1, int *t2)
{
    int temp;
    temp = *t1;
    *t1 = *t2;
    *t2 = temp;
}

void bubble_sort(int arr[], int len)
{
    int i, j;

    for (i = 0; i < len -1; i++) {
        for (j = 0; j < len -1 -i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}


int main()
{
    int arr[] = {34, 27, 55, 8, 97, 67, 35, 43, 22, 101, 78, 96, 35, 99};
    int i;
    int len = sizeof(arr) / sizeof(*arr);

    bubble_sort(arr, len);
    printf("len = %d \n", len);
    printf("use bubble sort the arrary is: ");

    for(i = 0; i < len; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}
