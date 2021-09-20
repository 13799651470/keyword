#include<stdio.h>
int a[300005];
int main(){
	int i,j,k;
	int n;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	scanf("%d",&a[i]);
	for(i=1;i<=n;i++){
		if(a[i]<(i-1))
		break;
	}
	for(j=n,k=0;j>=1;j--,k++){
		if(a[j]<k)
		break;
	}
	if(i>j)
	printf("Yes");
	else
	printf("No");
	return 0;
	
}
