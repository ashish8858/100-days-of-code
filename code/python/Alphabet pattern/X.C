void main()
{
int i,j,k,l,m=0,n=3,p=1,q=1; clrscr();
   for(i=1;i<=5;i++)
    {
    if(i<=3)
    {
      for(j=1;j<=m;j++)
       {
	 printf(" ");
       }
       m++;
       printf("*");
       for(k=1;k<=n;k++)
       {
	printf(" ");
       }n=n-2;
       if(i!=3)
       {
       printf("*");
       }
    }
    if(i>3)
    {
    for(j=1;j<=p;j++)
    {
    printf(" ");
    }p--;
    printf("*");
    for(k=1;k<=q;k++)
    {
    printf(" ");
    }
    q=q+2;
    printf("*");

    }
printf("\n");
}
getch();
}