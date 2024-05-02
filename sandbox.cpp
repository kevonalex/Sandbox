#include <iostream>
#include <vector>
#include <unistd.h> // for sleep function

using namespace std;

// Function to print the grid
void printGrid(const vector<vector<bool>>& grid) {
    for (const auto& row : grid) {
        for (bool cell : row) {
            cout << (cell ? "█" : " ");
        }
        cout << endl;
    }
}

// Function to count the number of live neighbors
int countLiveNeighbors(const vector<vector<bool>>& grid, int x, int y) {
    int count = 0;
    int n = grid.size();
    int m = grid[0].size();
    
    for (int i = -1; i <= 1; ++i) {
        for (int j = -1; j <= 1; ++j) {
            int newX = x + i;
            int newY = y + j;
            
            // Check if neighbor is within bounds and is alive
            if (newX >= 0 && newX < n && newY >= 0 && newY < m && grid[newX][newY]) {
                count++;
            }
        }
    }
    // Exclude the cell itself if it is alive
    return count - grid[x][y];
}

// Function to update the grid based on Conway's rules
void updateGrid(vector<vector<bool>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    
    vector<vector<bool>> newGrid(n, vector<bool>(m, false));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int liveNeighbors = countLiveNeighbors(grid, i, j);
            
            // Apply Conway's rules
            if (grid[i][j]) {
                if (liveNeighbors < 2 || liveNeighbors > 3) {
                    newGrid[i][j] = false; // Cell dies due to underpopulation or overpopulation
                } else {
                    newGrid[i][j] = true; // Cell survives
                }
            } else {
                if (liveNeighbors == 3) {
                    newGrid[i][j] = true; // Cell becomes alive due to reproduction
                }
            }
        }
    }
    grid = newGrid; // Update the original grid
}

int main() {
    int n = 20; // Size of the grid (number of rows)
    int m = 50; // Size of the grid (number of columns)
    
    vector<vector<bool>> grid(n, vector<bool>(m, false)); // Initialize grid with all dead cells
    
    // Initial pattern (glider)
    grid[1][2] = true;
    grid[2][3] = true;
    grid[3][1] = true;
    grid[3][2] = true;
    grid[3][3] = true;
    
    // Main loop to simulate the game
    for (int generation = 1; generation <= 100; ++generation) {
        system("clear"); // Clear the console (Unix/Linux)
        printGrid(grid); // Print the current state of the grid
        updateGrid(grid); // Update the grid based on Conway's rules
        usleep(100000); // Sleep for 100ms (Unix/Linux)
    }
    
    return 0;
}
