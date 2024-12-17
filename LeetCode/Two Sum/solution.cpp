#include "includes.cpp"

using namespace std;

class Solution {
public:

    vector<int> twoSum(vector<int>& nums, int target) {
    
        unordered_map<int, int> hash;
        int secondIndex;
        for (int i = 0 ; i < nums.size() ; i++)
        {
            secondIndex = target - nums[i];
            if (hash.find(secondIndex) != hash.end())
                return {hash[secondIndex], i}; 
            else
                hash[nums[i]] = i; 
        }
        return{}; 
    }
};