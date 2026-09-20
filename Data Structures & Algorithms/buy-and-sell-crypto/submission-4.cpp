class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprof = 0;
        int lowest = prices[0];
        for (int num : prices) {
            if (num < lowest) {
                lowest = num;
            }
            maxprof = max(maxprof, num - lowest);
        }
        return maxprof;
    }
};
