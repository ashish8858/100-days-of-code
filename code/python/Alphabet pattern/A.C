void main()
{
int i,j=4,k,l,m=1,s;
clrscr();
for(i=1;i<=5;i++)
{
s=j;
  while(s>=1)
  {
   printf(" ");
   s--;
  }
  j--;
if(i==3)
{
printf("AAAAA");
m=m+2;
}
else
{

  printf("A");
  if(i!=1)
  {
  for(k=1;k<=m;k++)
  {
    printf(" ");
  }
  m=m+2;

  printf("A");
  }
}
printf("\n");
}
getch();
}
