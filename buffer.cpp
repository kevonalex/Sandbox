#include <iostream>
#include <chrono>
#include <thread>

int main() {
    // Print some messages using std::cout
    std::cout << "Output without endl";
    std::cout << "Output without endl";
    
    // Use std::endl to print a newline and flush the buffer
    std::cout << std::endl;
    
    // Wait for a moment to observe the output
    std::this_thread::sleep_for(std::chrono::seconds(1));

    // Print more messages
    std::cout << "Output with endl" << std::endl;
    std::cout << "Output with endl" << std::endl;

    return 0;
}

