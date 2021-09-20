#include<stdio.h>
#include<string.h>
int fun(int i,int j,char *a,char*b,int k){
	int m=0;
	while(a[i]!=0&&b[j]!=0&&(a[i]==b[i]||k>0))
	{
					if(a[i]!=b[j])
					k--;
					m++;i++;j++;
				}
				return m;
}
int main(){
	int i,j,k,m;
	char a[505],b[505],c[505];
	int count;
	char ch;
	scanf("%d",&k);
	
	ch=getchar();
	scanf("%s",a);
	ch=getchar();
	scanf("%s",b);
	int la,lb;
	la=strlen(a);
	lb=strlen(b);
	if(la>lb){
		strcpy(c,a);
		strcpy(a,b);
		strcpy(b,c);
		m=la;
		la=lb;
		lb=m;
	}
	i=0;
	count=0;
	if(k>=la)
	printf("%d",la);
	else{
		for(i=0;i<la;i++){
			for(j=0;j<lb;j++){
				m=fun(i,j,a,b,k);
				if(count<m) count=m;
			}
		}
		printf("%d",m);
		}
		return 0;
	}

