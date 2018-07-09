void main()
{
int i,j,k,l,m,n;
clrscr();
for(i=1;i<=5;i++)
{
  if(i==1)
  printf("*******");
  else if(i==4)
  printf("*  *");
 else if(i==5)
  printf(" **");
  else
  {
     for(j=1;j<=3;j++)
      {
       printf(" ");
      }
     printf("*");
  }
printf("\n");
}
getch();
}