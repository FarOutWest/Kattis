#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <valarray>
#include <complex>
#include <vector>

using namespace std;

typedef long long ll;

void nextpow(ll& n) {
    n--;
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;
    n++;
}

void fft(valarray<complex<double>>& x) {
    ll s = x.size();
    if(s <= 1) {
        return;
    }
    valarray<complex<double>> even = x[slice(0, s/2, 2)];
    valarray<complex<double>> odd  = x[slice(1, s/2, 2)];
    fft(even);
    fft(odd);
    for(ll i = 0; i < s/2; i++) {
        complex<double> t = polar(1.0, -2.0 * M_PI * i / s) * odd[i];
        x[i]     = even[i] + t;
        x[i+s/2] = even[i] - t;
    }
}

void ifft(valarray<complex<double>>& x) {
    x = x.apply(conj);
    fft(x);
    x = x.apply(conj);
    x /= x.size();
}

int main() {
    ll big = 200000;
    nextpow(big);
    big *= 2;
    vector<ll> v1, v2;
    unordered_set<ll> achievable;
    ll size1;
    cin >> size1;
    for(ll i = 0; i < size1; i++) {
        ll n;
        cin >> n;
        v1.push_back(n);
        achievable.insert(n);
    }
    ll size2;
    cin >> size2;
    for(ll i = 0; i < size2; i++) {
        ll n;
        cin >> n;
        v2.push_back(n);
    }
    valarray<complex<double>> s1;
    complex<double> empty(0, 0);
    s1.resize(big, empty);
    for(auto i : v1) {
        complex<double> temp(1, 0);
        s1[i] = temp;
    }
    fft(s1);
    for(auto& i : s1) {
        i *= i;
    }
    ifft(s1);
    ll count = 0;
    for(auto i : v2) {
        if(s1[i].real() > .5 || achievable.count(i) > 0) {
            count++;
        }
    }
    cout << count << endl;
}
