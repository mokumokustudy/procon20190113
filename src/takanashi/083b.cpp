// include
#include <iostream>

// macro
#define FOR(index, num) for (auto index = 1; index <= num; index++)

// using namespace 
using namespace std;

// global
int N, A, B;

int main()
{
  cin >> N >> A >> B;

  int sum = 0;
  FOR (nId, N)
  {
    int currentNum = nId;
    int sumDigits = 0;
    while (currentNum)
    {
      sumDigits += currentNum % 10;
      currentNum /= 10;
    }
    if (A <= sumDigits && sumDigits <= B)
      sum += nId;
  }

  cout << sum << endl;

}

