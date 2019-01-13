// include
#include <iostream>
#include <algorithm>
#include <vector>

// using namespace 
using namespace std;

// macro
#define REP(index, num) for (auto index = 0; index < num; index++)

// global
int N;
vector<int> a_vec;

int main()
{
  cin >> N;
  a_vec.resize(N);

  REP(nId, N)
    cin >> a_vec[nId];

  // 降順ソート
  sort(a_vec.begin(), a_vec.end(), [](int &a1, int &a2) -> bool {return a1 > a2; });

  int sumAlice = 0;
  int sumBob = 0;
  REP(nId, N)
  {
    if (nId % 2 == 0)
      sumAlice += a_vec[nId];
    else
      sumBob += a_vec[nId];
  }

  cout << sumAlice - sumBob << endl;

}

