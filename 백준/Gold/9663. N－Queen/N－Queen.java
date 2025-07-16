import java.util.Scanner;

public class Main {
    private static int N;
    private static boolean[][] queen;
    private static int count = 0;
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        
        queen = new boolean[N][N];
        count = 0;
        
        nQueen(queen, 0, N);
        
        System.out.println(count);
        
        scanner.close();
    }
    
    public static void nQueen(boolean[][] queen, int depth, int N) {
        if (depth == N) {
            count++;
            return;
        }
        
        for (int i = 0; i < N; i++) {
            if (isPossible(queen, depth, i, N)) {
                queen[depth][i] = true;
                nQueen(queen, depth + 1, N);
                queen[depth][i] = false;
            }
        }
    }
    
    public static boolean isPossible(boolean[][] queen, int depth, int col, int N) {
        for (int row = 0; row < depth; row++) {
            if (queen[row][col]) {
                return false;
            }
        }
        
        for (int i = 0; i < depth; i++) {
            for (int j = 0; j < N; j++) {
                if (queen[i][j]) {
                    if (Math.abs(i - depth) == Math.abs(j - col)) {
                        return false;
                    }
                    break;
                }
            }
        }
        
        return true;
    }
}