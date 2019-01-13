// include
#include <iostream>

// using namespace 
using namespace std;

// global
int A, B, C, X;

int main()
{
  cin >> A >> B >> C >> X;

  int count = 0;

  for (int aId = 0; aId <= A; aId++)
    for (int bId = 0; bId <= B; bId++)
      for (int cId = 0; cId <= C; cId++)
      {
        int sumMoney = 500 * aId + 100 * bId + 50 * cId;
        if (sumMoney == X)
          count++;
      }

  cout << count << endl;

}
  
