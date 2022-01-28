class Solution {
public:
    
    int minEatingSpeed(vector<int>& piles, int h) {
        int l=1;
        int r=*max_element(piles.begin(),piles.end());
        while(l<r){
            int mid=(l+r)/2;
            if (check(mid,piles)<=h){
                r=mid;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
    int check(int mid,vector<int>& piles){
        int temp=0;
        for(auto & num:piles){
            if(num%mid==0){
                temp+=num/mid;
            }
            else{
                temp+=(num/mid)+1;
            }
        }
        return temp;       
    } 
};
