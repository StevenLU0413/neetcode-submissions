class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set<int> all;
        for (int i = 1; i <= nums.size(); i++) {
            all.insert(i);
        }

        for (int num : nums) {
            if (all.count(num)) all.erase(num);
        }
        return vector<int>(all.begin(), all.end());
    }
};