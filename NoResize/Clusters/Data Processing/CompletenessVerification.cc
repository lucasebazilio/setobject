#include <iostream>
#include <sstream>
#include <string>

int main() {
    std::string input;
    double weightedSum = 0.0;

    std::cout << "Enter the input data (press Ctrl + Z or Ctrl + D to finish):\n";

    while (std::getline(std::cin, input)) {
        std::stringstream ss(input);
        std::string token;

        std::getline(ss, token, ',');    // Ignoring the first column

        std::getline(ss, token, ',');
        int secondColumn = std::stoi(token);

        std::getline(ss, token, ',');
        double thirdColumn = std::stod(token);

        weightedSum += secondColumn * thirdColumn;
    }

    std::cout << "Weighted Sum: " << weightedSum << std::endl;

    return 0;
}
