// include
#include <iostream>

// using namespace 
using namespace std;

// global
int N;
int Y;

int main()
{
  cin >> N >> Y;

  for (int tId = 0; tId <= N; tId++)
  for (int fId = 0; fId <= N; fId++)
  {
    int oId = N - (tId + fId);
    if (oId < 0)
      continue;

    if (10000 * tId + 5000 * fId + 1000 * oId == Y)
    {
      cout << tId << " " << fId << " " << oId << endl;
      return 0;
    }
  }

  cout << "-1 -1 -1" << endl;

}

