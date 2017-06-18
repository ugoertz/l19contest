#include <cstdio>
#include <cstring>
#include <utility>
#include <map>
#include <string>

using namespace std;
const int LIMIT = 1000000007;
map<string, int> cache;

unsigned long long pow2limit(int i) {
  if (i==0) return 1;
  return (pow2limit(i-1) * 2) % LIMIT;
}


int num_palindromes(char* s, int start, int end) {
  // printf("%s %d-%d\n", s, start, end);
  if (start >= end) return 0;

  string ss(s+start, end-start);
  auto it = cache.find(ss);
  if (it != cache.end()) return it->second;

  unsigned long long result;

  int i = start + 1;
  for(; i < end; i++) {
    if (s[i] != s[start]) break;
  }
  if (i == end) {
    result = pow2limit(end-start) - 1;
    // printf("%s %d-%d, %d D\n", s, start, end, result);
  } else {
    result = num_palindromes(s, start+1, end) + 1;
    int pos = end - 1;
    while (1) {
      while (s[pos] != s[start]) pos--;
      if (pos > start) {
        result += num_palindromes(s, start+1, pos) + 1;
        pos--;
      } else break;
    }
  }

  // printf("%s %d-%d, %d\n", s, start, end, result);
  cache[ss] = result % LIMIT;
  return result % LIMIT;
}


int main() {
  int N;
  scanf("%d", &N);
  for(int i=0; i<N; i++) {
    cache.clear();
    char s[2100];
    scanf("%s", s);
    printf("%d\n", num_palindromes(s, 0, strlen(s)));
  }
}

