#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

const int LEFTMAX = 1;
const int LEFTMIN = 2;
const int RIGHTMAX = 3;
const int RIGHTMIN = 4;


vector<vector<int> > maxsl;
vector<vector<int> > maxsr;
vector<vector<int> > minsl;
vector<vector<int> > minsr;
vector<unsigned long long> data;

int indexminl(int L, int R) {
  if (L == R) return L;
  // cout << "iminl " << L << " " << R << endl;

  int i = 14;
  int p2i = 1 << i;
  while (L % p2i) {
    i--;
    p2i /= 2;
  }

  while (1) {
    if (L + p2i - 1 == R) {
      return minsl[i][L / p2i];
    } else if (L + p2i - 1 < R) {
      int im = indexminl(L + p2i, R);
      if (data[minsl[i][L / p2i]] <= data[im]) return minsl[i][L / p2i];
      else return im;
    }
    i--;
    p2i /= 2;
  }
}


int indexminr(int L, int R) {
  if (L == R) return L;
  // cout << "iminr " << L << " " << R << endl;

  int i = 14;
  int p2i = 1 << i;
  while (L % p2i) {
    i--;
    p2i /= 2;
  }

  while (1) {
    if (L + p2i - 1 == R) {
      return minsr[i][L / p2i];
    } else if (L + p2i - 1 < R) {
      int im = indexminr(L + p2i, R);
      if (data[minsr[i][L / p2i]] < data[im]) return minsr[i][L / p2i];
      else return im;
    }
    i--;
    p2i /= 2;
  }
}


int indexmaxl(int L, int R) {
  if (L == R) return L;
  // cout << "imaxl " << L << " " << R << endl;

  int i = 14;
  int p2i = 1 << i;
  while (L % p2i) {
    i--;
    p2i /= 2;
  }

  while (1) {
    if (L + p2i - 1 == R) {
      return maxsl[i][L / p2i];
    } else if (L + p2i - 1 < R) {
      int im = indexmaxl(L + p2i, R);
      if (data[maxsl[i][L / p2i]] >= data[im]) return maxsl[i][L / p2i];
      else return im;
    }
    i--;
    p2i /= 2;
  }
}


int indexmaxr(int L, int R) {
  if (L == R) return L;
  // cout << "imaxr " << L << " " << R << endl;

  int i = 14;
  int p2i = 1 << i;
  while (L % p2i) {
    i--;
    p2i /= 2;
  }

  while (1) {
    if (L + p2i - 1 == R) {
      return maxsr[i][L / p2i];
    } else if (L + p2i - 1 < R) {
      int im = indexmaxr(L + p2i, R);
      if (data[maxsr[i][L / p2i]] > data[im]) return maxsr[i][L / p2i];
      else return im;
    }
    i--;
    p2i /= 2;
  }
}


int max_magic(int L, int R, int info=0) {
  if (L == R) return 1;
  if (L == R - 1) return 2;

  int best;
  if (info == LEFTMAX) {
    int il = indexminl(L, R);
    if (il == L) best = R - L + 1;
    else {
      int ir = indexminr(L, R);
      best = ir - L + 1;
      if (R - il >= best) best = max(best, max_magic(il, R, LEFTMIN));
    }
  } else if (info == RIGHTMAX) {
    int ir = indexminr(L, R);
    if (ir == R) best = R - L + 1;
    else {
      int il = indexminl(L, R);
      best = R - il + 1;
      if (ir - L >= best) best = max(best, max_magic(L, ir, RIGHTMIN));
    }
  } else if (info == LEFTMIN) {
    int il = indexmaxl(L, R);
    if (il == L) best = R - L + 1;
    else {
      int ir = indexmaxr(L, R);
      best = ir - L + 1;
      if (R - il >= best) best = max(best, max_magic(il, R, LEFTMAX));
    }
  } else if (info == RIGHTMIN) {
    int ir = indexmaxr(L, R);
    if (ir == R) best = R - L + 1;
    else {
      int il = indexmaxl(L, R);
      best = R - il + 1;
      if (ir - L >= best) best = max(best, max_magic(L, ir, RIGHTMAX));
    }
  } else {
    int il = indexmaxl(L, R);
    int ir = indexmaxr(L, R);
    best = max(max_magic(il, R, LEFTMAX), max_magic(L, ir, RIGHTMAX));
  }

  return best;
}

int main() {
  int N;
  cin >> N;
  for(int i = 0; i < N; i++) {
    unsigned long long v;
    cin >> v;
    data.push_back(v);
  }
  int Q;
  cin >> Q;

  vector<int> a1;
  for(int i = 0; i < data.size(); i++) a1.push_back(i);

  maxsl.push_back(a1);
  while (maxsl[maxsl.size()-1].size() > 1) {
    vector<int> l;
    for(int i=0; i < maxsl[maxsl.size()-1].size()/2; i++) {
      if (data[maxsl[maxsl.size()-1][2*i]] >= data[maxsl[maxsl.size()-1][2*i+1]]) l.push_back(maxsl[maxsl.size()-1][2*i]);
      else l.push_back(maxsl[maxsl.size()-1][2*i+1]);
  }
    maxsl.push_back(l);
  }
  // for(auto it = maxsl.begin(); it != maxsl.end(); it++) {
  //   for(auto it1 = it->begin(); it1 != it->end(); it1++)
  //     cout << *it1 << ", ";
  //   cout << endl;
  // }
  // cout << endl;

  maxsr.push_back(a1);
  while (maxsr[maxsr.size()-1].size() > 1) {
    vector<int> l;
    for(int i=0; i < maxsr[maxsr.size()-1].size()/2; i++) {
      if (data[maxsr[maxsr.size()-1][2*i]] > data[maxsr[maxsr.size()-1][2*i+1]]) l.push_back(maxsr[maxsr.size()-1][2*i]);
      else l.push_back(maxsr[maxsr.size()-1][2*i+1]);
  }
    maxsr.push_back(l);
  }

  minsl.push_back(a1);
  while (minsl[minsl.size()-1].size() > 1) {
    vector<int> l;
    for(int i=0; i < minsl[minsl.size()-1].size()/2; i++) {
      if (data[minsl[minsl.size()-1][2*i]] <= data[minsl[minsl.size()-1][2*i+1]]) l.push_back(minsl[minsl.size()-1][2*i]);
      else l.push_back(minsl[minsl.size()-1][2*i+1]);
  }
    minsl.push_back(l);
  }

  minsr.push_back(a1);
  while (minsr[minsr.size()-1].size() > 1) {
    vector<int> l;
    for(int i=0; i < minsr[minsr.size()-1].size()/2; i++) {
      if (data[minsr[minsr.size()-1][2*i]] < data[minsr[minsr.size()-1][2*i+1]]) l.push_back(minsr[minsr.size()-1][2*i]);
      else l.push_back(minsr[minsr.size()-1][2*i+1]);
  }
    minsr.push_back(l);
  }

  int L, R;
  for(int i = 0; i < Q; i++) {
    cin >> L;
    cin >> R;
    cout << max_magic(L-1, R-1) << endl;
  }
}

