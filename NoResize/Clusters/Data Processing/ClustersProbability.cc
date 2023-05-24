#include <iostream>
#include <sstream>
#include <vector>

int main() {
    std::string input;
    std::vector<std::string> lines;

    // Read the input
    while (std::getline(std::cin, input)) {
        lines.push_back(input);
    }

    // Process and print the modified output
    for (const std::string& line : lines) {
        std::stringstream ss(line);
        std::string token;
        std::vector<std::string> tokens;

        // Split the line into tokens using comma as the delimiter
        while (std::getline(ss, token, ',')) {
            tokens.push_back(token);
        }

        // Check if the line has three columns
        if (tokens.size() != 3) {
            std::cerr << "Invalid input format: " << line << std::endl;
            continue;
        }

        // Parse the second and third columns
        int col2;
        double col3;
        try {
            col2 = std::stoi(tokens[1]);
            col3 = std::stod(tokens[2]);
        } catch (const std::exception& e) {
            std::cerr << "Error parsing columns: " << e.what() << std::endl;
            continue;
        }

        // Calculate the modified value for the third column
        double modified = col2 * col3 / 65536.0;

        // Print the modified output
        std::cout << tokens[0] << "," << tokens[1] << "," << modified << std::endl;
    }

    return 0;
}
