// include
#include <iostream>

// using namespace 
using namespace std;

// macro
#define REP(index, num) for (auto index = 0; index < num; index++)
#define MAX_NUM 220

// global
int N;
int A[MAX_NUM];

int main()
{
  cin >> N;

  REP(nId, N)
    cin >> A[nId];

  bool endFlag = false;
  int count = 0;

  while (!endFlag)
  {
    REP(nId, N)
    {
      if (A[nId] % 2)
        endFlag = true;
    }
    if (!endFlag)
    {
      REP(nId, N)
      {
        A[nId] /= 2;
      }
      count++;
    }
  }

  cout << count << endl;

}

