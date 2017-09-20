#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

struct compare {
    bool operator() (
        const pair<int, vector<long long>* >& lhs,
        const pair<int, vector<long long>* >& rhs) const {
      // lexicographically compare the vector parts of lhs and rhs, strating the
      // comparison at the indices given by the first component, and such that
      // for a sequence A which equals the initial piece of a (longer) sequence
      // B, B comes first in the ordering.
      auto itl = lhs.second->begin() + lhs.first;
      auto itr = rhs.second->begin() + rhs.first;

      while (itl != lhs.second->end()) {
        if (itr == rhs.second->end()) {
          // rhs is initial piece of lhs, but not equal
          return true;
        }
        if (*itl < *itr) return true;
        if (*itl > *itr) return false;
        itl++;
        itr++;
      }
      // lhs is initial piece of rhs, possibly equal
      return false;
    }
};


int main() {
  int N;
  cin >> N;
  multiset<pair<int, vector<long long>*>, compare> data;

  for(int i = 0; i < N; i++) {
    vector<long long>* a = new vector<long long>;
    int sz;
    cin >> sz;
    for(int j=0; j < sz; j++) {
      long long v;
      cin >> v;
      a->push_back(v);
    }
    data.insert(make_pair(0, a));
  }

  vector<long long> result;
  while (data.size()) {
    auto it = data.begin();
    long long v = (*it->second)[it->first];
    int index = it->first;
    while (index < it->second->size() && v == (*it->second)[index]) {
      index++;
      result.push_back(v);
    }
    if (it->second->size() - it->first > 1) {
      data.insert(make_pair(index, it->second));
    }
    data.erase(it);
  }
  for(auto itr = result.begin(); itr != result.end(); itr++) {
    cout << *itr;
    if (itr+1 != result.end()) cout << " ";
  }
  cout << endl;
}
