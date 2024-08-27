#include <stdio.h>
#include <stdbool.h>

#define N 9

bool findUnassignedLocation(int grid[N][N], int *row, int *col);
bool isSafe(int grid[N][N], int row, int col, int num);
bool solveSudoku(int grid[N][N]);
void printGrid(int grid[N][N]);
void inputGrid(int grid[N][N]);

int main() {
    int grid[N][N];
    inputGrid(grid);

    printf("Sudoku initial :\n");
    printGrid(grid);
    
    if (solveSudoku(grid) == true) {
        printf("\nSolution :\n");
        printGrid(grid);
    }
    else {
        printf("Pas de solution trouvée.\n");
    }

    return 0;
}

bool findUnassignedLocation(int grid[N][N], int *row, int *col) {
    for (*row = 0; *row < N; (*row)++)
        for (*col = 0; *col < N; (*col)++)
            if (grid[*row][*col] == 0)
                return true;
    return false;
}

bool isSafe(int grid[N][N], int row, int col, int num) {
    for (int i = 0; i < N; i++)
        if (grid[row][i] == num || grid[i][col] == num)
            return false;
    
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (grid[i + startRow][j + startCol] == num)
                return false;
    
    return true;
}

bool solveSudoku(int grid[N][N]) {
    int row, col;
    if (!findUnassignedLocation(grid, &row, &col))
        return true;
    
    for (int num = 1; num <= 9; num++) {
        if (isSafe(grid, row, col, num)) {
            grid[row][col] = num;
            if (solveSudoku(grid))
                return true;
            grid[row][col] = 0;
        }
    }
    return false;
}

void printGrid(int grid[N][N]) {
    for (int row = 0; row < N; row++) {
        for (int col = 0; col < N; col++)
            printf("%2d ", grid[row][col]);
        printf("\n");
    }
}

void inputGrid(int grid[N][N]) {
    printf("Entrez la grille de Sudoku (utilisez 0 pour les cases vides) :\n");
    for (int row = 0; row < N; row++) {
        for (int col = 0; col < N; col++) {
            scanf("%d", &grid[row][col]);
        }
    }
}
