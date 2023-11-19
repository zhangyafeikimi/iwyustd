#include <fstream>
#include <sstream>
#include <stddef.h> // NULL

#define A std::stringstream
#define B std::istringstream
#define C std::ostringstream
#define D std::fstream
#define E std::ifstream
#define F std::ofstream

int main() {
  // std::stringstream ss1;
  // std::istringstream ss2;
  // std::ostringstream ss3;
  std::stringstream ss1;
  std::istringstream ss2;
  std::ostringstream ss3;
  // std::fstream f1;
  // std::ifstream f2;
  // std::ofstream f3;
  std::fstream f1;
  std::ifstream f2;
  std::ofstream f3;
  // void *p1 = NULL;
  // void *p2 = nullptr;
  void *p1 = NULL;
  void *p2 = nullptr;
  return 0;
}
