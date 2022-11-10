#include "bits/stdc++.h"
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    int nums1[n+1];
    int nums2[m+1];
    for(int i=1;i<=n;i++){
        cin>>nums1[i];
    }
    nums1[0]=0;
    for(int j=1;j<=m;j++){
        cin>>nums2[j];
    }
    nums2[0]=0;
    int dp[n+1][m+1];
    

    dp[0][0]=0;
    for(int i=1;i<=n;i++){
        dp[i][0]=i;
    }
    for(int j=1;j<=m;j++){
        dp[0][j]=j;
    }

    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            int a=dp[i-1][j]+1;
            int b=dp[i][j-1]+1;
            int c=dp[i-1][j-1]+ (nums1[i]==nums2[j]?0:1);
            
            dp[i][j]=min(a,min(b,c));
        }
    }
    cout<<dp[n][m]<<endl;


    return 0;
}