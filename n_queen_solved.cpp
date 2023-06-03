#include <iostream>
#include <string>
using namespace std;


int is_diagonal_clear(int x, int y, int k, int board[][8]){
    //checking first diagonal k=board size
    int m=x;
    int n=y;
    int batti=0;
    while(n>=0 && m<k){
        if(m!=x && n!=y){
            // cout << "checking: (" << m << "," << n << ")" << endl;
            if(board[m][n]==1){
                //not clear
                return 0;
            }
        }
        if(batti==0){
            m-=1;
            n+=1;
            if(m<0 || n==k){
                batti=1;
                m=x;
                n=y;
            }
        }
        if(batti==1){
            m+=1;
            n-=1;
        }
        
    }
    //checking the second diagonal;
    m=x;
    n=y;
    batti=0;
    while(n>=0 && m>=0){
        if(m!=x && n!=y){
            // cout << "checking: (" << m << "," << n << ")" << endl;
            if(board[m][n]==1){
                //not clear
                return 0;
            }
        }
        if(batti==0){
            m+=1;
            n+=1;
            if(m==k || n==k){
                batti=1;
                m=x;
                n=y;
            }
        }
        if(batti==1){
            m-=1;
            n-=1;
        }
    }
    return 1;
}


int is_straight_line_clear(int x,int y,int k, int board[][8]){
    //going to row
    for(int col=0;col<k;col++){
        if(col==y)
            continue;
        if(board[x][col]==1)
            return 0;    
    }
    //going to column
    for(int row=0;row<k;row++){
        if(row==x)
            continue;
        if(board[row][y]==1)
            return 0;
    }
    return 1;
}

int is_safe(int board[][8],int row, int col){
    if((is_diagonal_clear(row, col, 8, board)) && (is_straight_line_clear(row,col,8,board))){
        return 1;
    }
    return 0;
}

int p1=0;  //life savoiur global variable

// at first give row =0 in myfxn
//also give pull=0

int myfxn(int board[][8], int row){
    for(int x=0;x<8;x++){
        if(is_safe(board,row,x))
        {
            board[row][x]=1;
            if(row==7){
                p1=1;
                return 0;
            }

            int rev = myfxn(board, row+1);
            if(p1==1)
                return 0;
            if(rev == -1)
                board[row][x]=0;
            
        }
        if(x==7)return -1;
    }
    return 0; 
}


int main()
{
    int board_size = 8;
    int chess_board[][8]={
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0}
    };

    int row=0;
    myfxn(chess_board, 0);

    cout << "printing the board final:\n";
    for(int k=0;k<8;k++){
        for(int h=0;h<8;h++){
            cout << chess_board[k][h] << " ";
        }
        cout << endl;
    }
    return 0;
}
