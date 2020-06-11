#include <stdio.h>
int main() 
{
    int n;
    scanf("%d",&n);
    int A[n],i;
    for(i=0;i<n;i++)
        scanf("%d",&A[i]);
    int m;
    scanf("%d",&m);
    int sum=0;
    for(i=0;i<n;i++)
            sum+=A[i];
    for(i=0;i<m;i++)
    {
        int target;
        scanf("%d",&target);
        int total=0,turn;
        if (target>sum)
            printf("-1\n");
        else
        {
            for(turn=0;turn<n;turn++)
            {
                total+=A[turn];
                if (target<=total)
                {
                    printf("%d\n",turn+1);
                    break;
                }
             }
        }
    }
    return 0;
}
