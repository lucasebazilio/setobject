#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <iomanip>

int main() {
    std::unordered_map<int, std::pair<double, int>> mp;
    int n, m;
    while (std::cin >> n >> m) {
        mp[n].first += m;
        mp[n].second++;
    }

    std::vector<std::pair<int, double>> sorted_mp;
    for (auto it = mp.begin(); it != mp.end(); ++it) {
        double value = it->second.first / it->second.second;
        sorted_mp.push_back({it->first, value});
    }

    std::sort(sorted_mp.begin(), sorted_mp.end());

    for (const auto& p : sorted_mp) {
        std::cout << "Average value for key " << p.first << " is "
                  << std::fixed << std::setprecision(1) << p.second << '\n';
    }

    return 0;
}
