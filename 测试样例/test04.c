#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
	int a[1005],i,j,k;
	char ch;
	int m,count=0;
	int n;
	scanf("%d",&n);
	ch=getchar();
	for(i=1;i<=n;i++)
	scanf("%d",&a[i]);
	sort(a+1,a+(n+1));
	m=a[1];i=1;
	int flag=0;
	while(i<=n){
		count=1;
		m=a[i];
		for(j=i+1;j<=n;j++){
			if((a[j]-m)>1){
				count++;
				m=a[j];
				a[j]=a[1];
			}
		}
		sort(a+1,a+(n+1));
		i=i+count;
		flag++;
	}
	printf("%d",flag);
	return 0;
}
