#include "includes.cpp"

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

       unordered_map<int, int> hash;

        for (int num : nums)
        {
            auto it = hash.find(num);
            if (it == hash.end())
                hash[num] = 0;
            else return true;
        }
        return false;

/*
    set<int> s;
    vector<int> new_vec;

    for (int num : nums)
    {
        s.insert(num);
        new_vec.push_back(num);
        if (s.size() < new_vec.size()) return true;
    }

    return false; */
    }
};