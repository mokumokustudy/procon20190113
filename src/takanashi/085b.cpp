// include
#include <iostream>
#include <vector>
#include <algorithm>

// using namespace 
using namespace std;

// macro
#define REP(index, num) for (auto index = 0; index < num; index++)

// global
int N;
vector<int> d_vec;

int main()
{
  cin >> N;
  d_vec.resize(N);

  REP(nId, N)
    cin >> d_vec[nId];

  sort(d_vec.begin(), d_vec.end());
  
  int count = 1;
  REP(nId, N)
  {
    if (nId == 0) 
      continue;
    
    if (d_vec[nId] > d_vec[nId - 1])
      count++;
  }

  
  cout << count << endl;

}

