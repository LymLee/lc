#include <map>

class Solution {
    std::map<std::pair<string, string>, bool > smap;
    std::map<std::pair<string, string>, bool >::iterator it;
public:
    bool isMatch(string s, string p) {
        if(s[0] == '\0') {
            if(p[0] == '\0') {
                return 1;
            }
            else if(p[1] == '*'){
                it = smap.find(std::make_pair(s, p.substr(2)));
                
                if(it ==  smap.end()) {
                    smap[std::make_pair(s, p.substr(2))] = isMatch(s, p.substr(2));
                }
                
                return smap[std::make_pair(s, p.substr(2))];
            }
            else {
                return 0;
            }
        }
        else if(p[0] == '\0') {
            return 0;
        }
        
        if(p[1] == '*') {
            if(p[0] == '.' || p[0] == s[0]) {
                bool b1, b2, b3;
                
                it = smap.find(std::make_pair(s.substr(1), p));
                if(it ==  smap.end()) {
                    smap[std::make_pair(s.substr(1), p)] = isMatch(s.substr(1), p);
                }
                
                it = smap.find(std::make_pair(s.substr(1), p.substr(2)));
                if(it ==  smap.end()) {
                    smap[std::make_pair(s.substr(1), p.substr(2))] = isMatch(s.substr(1), p.substr(2));
                }
                
                it = smap.find(std::make_pair(s, p.substr(2)));
                if(it ==  smap.end()) {
                    smap[std::make_pair(s, p.substr(2))] = isMatch(s, p.substr(2));
                }

                return smap[std::make_pair(s.substr(1), p)] || smap[std::make_pair(s.substr(1), p.substr(2))] || smap[std::make_pair(s, p.substr(2))];
            }
            else {
                it = smap.find(std::make_pair(s, p.substr(2)));
                
                if(it ==  smap.end()) {
                    smap[std::make_pair(s, p.substr(2))] = isMatch(s, p.substr(2));
                }
                
                return smap[std::make_pair(s, p.substr(2))];
            }
    
        }
        else if(p[0] == s[0] || p[0] == '.'){
            it = smap.find(std::make_pair(s.substr(1), p.substr(1)));
            
            if(it ==  smap.end()) {
                smap[std::make_pair(s.substr(1), p.substr(1))] = isMatch(s.substr(1), p.substr(1));
            }
            
            return smap[std::make_pair(s.substr(1), p.substr(1))];
        }
        else {
            return 0;
        }
        
    }
};