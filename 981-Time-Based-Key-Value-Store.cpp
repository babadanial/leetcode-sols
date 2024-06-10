#include <string>
#include <unordered_map>
#include <vector>
#include <utility>

using namespace std; 

class TimeMap {
    unordered_map<string, vector<pair<int, string>>> timeMap;

    public:
        TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        timeMap[key].push_back(pair(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        if (!timeMap.count(key)) return "";

        vector<pair<int, string>> & entry = timeMap.at(key);
        int left = 0;
        int right = entry.size() - 1;
        if (entry.empty() || entry[left].first > timestamp) return "";
        
        while (left < right) {
            int middle = (left + right) / 2; // recall C++ truncates
            if (entry[middle].first <= timestamp && entry[middle+1].first > timestamp) {
                return entry[middle].second;
            } else if (entry[middle].first < timestamp) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return entry[left].second;
    }
};