// include
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// using namespace 
using namespace std;

// macro
#define REP(index, num) for (auto index = 0; index < num; index++)

// global
string S, T; 
vector<string> termList;

inline bool IsSEqualT(string &out_trimmedS);

int main()
{
  cin >> S;
  
  termList.push_back("dream");
  termList.push_back("dreamer");
  termList.push_back("erase");
  termList.push_back("eraser");

  REP(tId, termList.size())
    reverse(termList[tId].begin(), termList[tId].end());

  // 反転
  reverse(S.begin(), S.end());

  bool flag = IsSEqualT(S);

  if (flag)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;

}

// 深さ優先探索
inline bool IsSEqualT(string &out_trimmedS)
{
  if (!out_trimmedS.size())
    return true;

  bool flag = false;
  for (int tId = 0; tId < termList.size(); tId++)
  {
    string tempStr = out_trimmedS.substr(0, termList[tId].size());
    if (tempStr == termList[tId])
    {
      out_trimmedS.erase(out_trimmedS.begin(), out_trimmedS.begin() + tempStr.size());
      // さらに潜る
      flag = IsSEqualT(out_trimmedS);
      if (flag)
        return true;
    }
  }

  return false;

}
