#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
int main(){
    int t;
    cin>>t;
    int count=1;
    while(t--){
        int n;
        cin>>n;
        int dp[n+1];
        for(int i=0;i<=n;i++){
            dp[i]=1e9;
        }
        dp[0]=0;
        dp[1]=1;
        for(int i=2;i<=n;i++){
            dp[i]=min(dp[i],dp[i-1]+1);
            int j=1;
            while(i*j<=n){
                dp[i*j]=min(dp[i*j],dp[i]+4+2*(j-1));
                j+=1;
            }
        }
        cout<<"Case #"<<count<<": "<<dp[n]<<endl;
        count+=1;   
    }
    return 0;
}

