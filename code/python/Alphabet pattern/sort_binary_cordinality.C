void main()
{
int n[10],a[10],temp,i,j,k,d,l,blank[10];
clrscr();
printf("Enter limit : ");
scanf("%d",&l);
printf("Enter Array : ");
for(i=0;i<l;i++)
scanf("%d",&n[i]);
for(i=0;i<l;i++)
a[i]=n[i];

for(i=0;i<l;i++)
{ k=0;
while(n[i]!=0)
{
d=n[i]%2;
if(d==1)
k++;
n[i]=n[i]/2;
}
blank[i]=k;
}


printf("\n");
for(i=0;i<l;i++)
{
printf("   %d",blank[i]);
}
for(i=0;i<l;i++)
{
for(j=0;j<l;j++)
{
if(blank[j]>blank[j+1])
{
k=blank[j];
blank[j]=blank[j+1];
blank[j+1]=k;
temp=a[j];
a[j]=a[j+1];
a[j+1]=temp;
}
}
}

printf("\n");
for(i=0;i<l;i++)
{
printf("   %d",blank[i]);
}
  printf("\n");
for(i=0;i<l;i++)
{
printf("   %d",a[i]);
}




getch();
}

