#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;


int main() {
  int M, N;
  cin >> N;
  cin >> M;
  vector<char> grid;
  vector<int> trees;
  int J, V;
  char x;

  vector<int> mindist(N*M, -1);
  // minimal distance to a tree for each pt in the grid

  for(int i=0; i < N; i++) {
    for(int j=0; j < M; j++) {
      cin >> x;
      if (x == 'V') {
        V = i*M + j;
        x = '.';
      }
      if (x == 'J') {
        J = i*M + j;
        x = '.';
      }
      if (x == '+') {
        trees.push_back(i*M+j);
        mindist[i*M+j] = 0;
      }
      grid.push_back(x);
    }
  }

  int numdone = trees.size();
  for(int d=1; d<N+M; d++) {
    for(auto t = trees.begin(); t != trees.end(); t++) {
      vector<int> dist_d_pts;
      // (x,y) ->  (x+d, y), (x+d-1, y+1), ..., (x, y+d),    x + (d-i), y+i
      //           (x+d, y), (x+d-1, y-1), ..., (x, y-d),    x + (d-i), y-i
      //           (x-d, y), (x-d+1, y+1), ..., (x, y+d),    x - (d-i), y+i
      //           (x-d, y), (x-d+1, y-1), ..., (x, y-d).    x - (d-i), y-i
      int x = (*t) % M;
      int y = (*t - x) / M;

      for(int i=0; i<=d; i++) {
        int xx = x + d - i;
        int yy = y + i;
        if (xx >= 0 && xx < M && yy >= 0 && yy < N) {
          dist_d_pts.push_back(yy*M + xx);
        }
      }

      for(int i=0; i<=d; i++) {
        int xx = x + d - i;
        int yy = y - i;
        if (xx >= 0 && xx < M && yy >= 0 && yy < N) {
          dist_d_pts.push_back(yy*M + xx);
        }
      }

      for(int i=0; i<d; i++) {
        int xx = x - d + i;
        int yy = y + i;
        if (xx >= 0 && xx < M && yy >= 0 && yy < N) {
          dist_d_pts.push_back(yy*M + xx);
        }
      }

      for(int i=0; i<d; i++) {
        int xx = x - d + i;
        int yy = y - i;
        if (xx >= 0 && xx < M && yy >= 0 && yy < N) {
          dist_d_pts.push_back(yy*M + xx);
        }
      }

      for(auto it=dist_d_pts.begin(); it != dist_d_pts.end(); it++) {
        if (mindist[*it] == -1) {
          mindist[*it] = d;
          numdone++;
        }
      }
    }

    if (numdone == N*M) break;
  }
  // for(int i=0; i < N; i++) {
  //   for(int j=0; j < M; j++) {
  //     cout << mindist[i*M + j] << " ";
  //   }
  //   cout << endl;
  // }

  // search for answer; define lower, upper s.t. lower <= answer < upper
  int upper = (mindist[J] < mindist[V] ? mindist[J] : mindist[V]) + 1;
  int lower = 0;

  while (upper - lower > 1) {
    int b = (upper + lower) / 2;
    // cout << lower << " " << upper << endl;
    // cout << "ff " << b << endl;

    // flood-fill starting from V with points with distance >= b to a tree as
    // borders

    bool foundJ = false;
    set<int> seen;
    seen.insert(V);
    vector<int>* newlyseen = new vector<int>;
    newlyseen->push_back(V);

    while (newlyseen->size()) {
      vector<int>* n = new vector<int>;
      for(auto x = newlyseen->begin(); x != newlyseen->end(); x++) {
        int nbs[4];
        int nbsctr = 0;
        // neighbors of x within grid with minimal distance to a tree at least b
        // candidates: x + 1, x - 1, x + M, x - M
        int xx = *x;
        if ((xx % M) < M-1 && mindist[xx+1] >= b) nbs[nbsctr++] = xx+1;
        if ((xx % M) > 0 && mindist[xx-1] >= b) nbs[nbsctr++] = xx-1;
        if (xx+M < N*M && mindist[xx+M] >= b) nbs[nbsctr++] = xx+M;
        if (xx-M >= 0 && mindist[xx-M] >= b) nbs[nbsctr++] = xx-M;
        // cout << "ex " << *x << " " << nbs.size() << endl;

        for(int yy=0; yy < nbsctr; yy++) {
          int y = nbs[yy];
          if (seen.count(y) == 0) {
            n->push_back(y);
            // cout << y << " ";
            if (y == J) {
              foundJ = true;
              break;
            }
            seen.insert(y);
          }
        }
        if (foundJ) break;
      }
      // cout << endl;
      delete newlyseen;
      newlyseen = n;
    }
    if (foundJ) {
      // can go there with min distance b
      lower = b;
      // cout << "OK" << endl;
    } else {
      upper = b;
      // cout << "not OK" << endl;
    }
  }
  cout << lower << endl;
}
