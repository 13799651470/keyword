#include<stdio.h>
int fun1(int flag,int a,int b);
int fun2(int flag,int a,int b);
int fun3(int a,int b);
int fun4(int a,int b);
int fun1(int flag,int a,int b){
	int i=0;
if(flag==1){
	i=366-fun4(a,b);
}
else{
	i=365-fun3(a,b);
}

return (i);
}
int fun2(int flag,int a,int b){
	if(flag==1){
	
		return (fun4(a,b));
	}
	
	else{
	
		return (fun3(a,b));
	}
	
}
int fun3(int a,int b){
	int i=0;
	i=b;
	switch(a-1){
		case 11:i+=30;  case 10:i+=31;  case 9:i+=30;  case 8:i+=31;  case 7:i+=31;
		case 6:i+=30;  case 5:i+=31;  case 4:i+=30;  case 3:i+=31;  case 2:i+=28;  case 1:i+=31;break;
	}
	 return (i);
}
int fun4(int a,int b){
	int i=0;
	i=b;
	switch(a-1){
		case 11:i+=30;  case 10:i+=31;  case 9:i+=30;  case 8:i+=31;  case 7:i+=31;
		case 6:i+=30;  case 5:i+=31;  case 4:i+=30;  case 3:i+=31;  case 2:i+=29;  case 1:i+=31;break;
	}
	 return (i);
}
int main(){
	int year1,mon1,day1;
	int year2,mon2,day2;
	int i=1,j,k,l;
	int y1=0,y2=0;
	int c=-1;
	long long int day=0;
	while(scanf("%d %d %d %d %d %d",&year1,&mon1,&day1,&year2,&mon2,&day2)!=EOF){
	i=1;y1=0;y2=0;
	c=-1;
	day=0;
		if(year1>year2||(year1==year2&&mon1>mon2)){
		c=1;	
		k=year1;
		year1=year2;
		year2=k;
		k=mon1;
		mon1=mon2;
		mon2=k;
		k=day1;
		day1=day2;
		day2=k;
		}
		else if((year1==year2)&&(mon1==mon2)&&(day1>day2)){
		c=1;	
		k=year1;
		year1=year2;
		year2=k;
		k=mon1;
		mon1=mon2;
		mon2=k;
		k=day1;
		day1=day2;
		day2=k;
		}
		else if((year1==year2)&&(mon1==mon2)&&(day1==day2)){
			c=0;
		}
		for(i=(year1+1);i<=(year2-1);i++){
			if((i%4==0&&i%100!=0)||(i%400==0)){
				day=day+366;
			}
			else {
				day+=365;
			}
		}
		if((year1%4==0&&year1%100!=0)||(year1%400==0))  y1=1;
		if((year2%4==0&&year2%100!=0)||(year2%400==0))  y2=1;
		day+=fun1(y1,mon1,day1);
		day+=fun2(y2,mon2,day2);
		if(c==0)
		printf("0\n");
		else if(c>0)
		printf("%lld\n",day);
		else printf("-%lld\n",day);
}
return 0;
}

