#include <cstdio>
#include <cstring>

using namespace std;
const unsigned long long LIMIT = 1000000007;

unsigned long long acs[8000000];


int main() {
  int N;
  scanf("%d", &N);
  for(int ii=0; ii<N; ii++) {
    char s[2100];
    scanf("%s", s);

    // build acs table
    for(int i = 0; i < strlen(s); i++) {
      for(int j = 0; j < strlen(s); j++) {
        if (i == 0 || j == 0) {
          acs[i + 3000*j] = 1;
        } else {
          if (s[i-1] == s[strlen(s)-j])
            acs[i + 3000*j] = (acs[i-1 + 3000*j] + acs[i + 3000*(j-1)]) % LIMIT;
          else
            acs[i + 3000*j] = (acs[i-1 + 3000*j] + acs[i + 3000*(j-1)] + LIMIT - acs[i-1 + 3000*(j-1)]) % LIMIT;
        }
      }
    }

    unsigned long long result = 0;
    for(int i=0; i<strlen(s); i++)
      result = (result + acs[i + 3000*(strlen(s)-i-1)]) % LIMIT;

    for(int i=0; i<strlen(s)-1; i++)
      for(int j=0; j<strlen(s)-i-1; j++)
        if (s[i] == s[strlen(s)-j-1])
          result = (result + acs[i + 3000*j]) % LIMIT;

    printf("%lld\n", result);
  }
}

