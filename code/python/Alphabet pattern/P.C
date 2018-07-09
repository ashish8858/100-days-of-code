void main()
{
int i,j,k,l,m,n;
clrscr();
for(i=1;i<=5;i++)
{
  if(i==3||i==1)
  printf("****");
  else if(i==2)
  {
  printf("*");
  for(k=1;k<=3;k++)
  {
  printf(" ");
  }
  printf("*");
  }
  else
  printf("*");
printf("\n");
}
getch();
}