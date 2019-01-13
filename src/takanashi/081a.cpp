// include
#include <iostream>

// macro
#define REP(index, num) for (auto index = 0; index < num; index++)

// using namespace 
using namespace std;

int main()
{
  int val;
  int count = 0;

  cin >> val;

  REP(id, 3)
  {
    if (val % 10) count++;
    val /= 10;
}
  cout << count << endl;

}

