class Solution {
    public:
        int romanToInt(string s) {
            std::unordered_map<char, int> u = {
                {'I', 1},
                {'V', 5},
                {'X', 10},
                {'L', 50},
                {'C', 100},
                {'D', 500},
                {'M', 1000}
            };
            
            int converted = u[s.back()];
            
            for(int i = 0; i < s.length() - 1; i++) {
                if (u[s[i]] >= u[s[i+1]]) {
                    converted += u[s[i]];
                } else {
                    converted -= u[s[i]];
                }
            }
            
            return converted;
        }
    };