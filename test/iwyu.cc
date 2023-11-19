#include "iwyu.h"
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

#if 0
#error Unsupported operating system.
#endif

#define A fopen
#define B std::array

int main() {
  printf("%s\n", "system");
  // exp expf
  /* exp expf */
  /*
   * exp expf
   */
  std::vector<std::string> vs1;
  std::vector<std::string> vs2;
  std::string s;
  vs1.emplace_back(std::move(s));
  std::move(vs1.begin(), vs1.end(), std::back_inserter(vs2));
  return 0;
}
