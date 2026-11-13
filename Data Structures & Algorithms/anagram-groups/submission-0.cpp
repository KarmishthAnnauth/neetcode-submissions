class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> seen;

        for (int i = 0; i < (int)strs.size(); i++){
            std::string word = strs[i];
            std::sort(word.begin(), word.end());
            auto it = seen.find(word);
            
            if (it != seen.end()){
                seen[word].push_back(strs[i]);
            }
            else {
                seen[word] = {strs[i]};
            }
        }

        vector<vector<string>> results;

        for (auto& [key, value] : seen){
            results.push_back(value);
        }

        return results;
    }
};
