#include <stdio.h> 
int partition(int *A, int p, int r){
	int pivô = A[p];
	int i = (p-1);
	for(int j = p; j <= r-1; j++){
		if(A[j] <= pivô){
		i++;
		swap(A[i],A[j]);
		}
	}	
	swap(A[i+1],A[r]);
	return(i+1);
void quicksort(int *A, int p, int r){
	if(p < r){
		int q;
		q = partition(A,p,r);
		quicksort(A,p,q-1);
		quicksort(A,q+1,r);
	}	
}
int main(){
	int *A = [3,1,2];
	int i = 0;
	quicksort(A,0,2);
	for i range(2):
		print(A[i]);
		
}