#include <stdio.h>


void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int* container, int left, int right, int pivot){
    while(left <= right){
        while(container[left++] < pivot){}
        while(container[right--] > pivot){}
        if(left <= right){
            printf("%d, %d\n", container[left], container[right]);
            swap(&container[left], &container[right]);
            printf("%d, %d\n", container[left], container[right]);
            left++;
            right--;
        }
    }
    return left;
}

void qs(int* container, int left, int right){
    if(left >= right){ return; }
    int middle = (left + right) / 2;
    int pivot = container[middle];
    int index = partition(container, left, right, pivot);
    qs(container, left, index - 1);
    qs(container, index, right);
}

int main(int argc, const char* argv[]){
    int array[] = {1, 32, 12, 19};
    qs(array, 0, 4);
    for(int i = 0; i < 4; ++i){
        printf("%d ", array[i]);
    }
    printf("\n");
    return 0;
}
