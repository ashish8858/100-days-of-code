void main()
{
int i,j,m=2;
clrscr();
for(i=1;i<=5;i++)
{
printf("*");
if(i<3)
{
for(j=1;j<=m;j++)
printf(" ");
m--;
}
if(i>=3)
{
for(j=1;j<=m;j++)
{
printf(" ");
}
m++;
}
printf("*");

printf("\n");
}
getch();
}