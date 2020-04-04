#include <iostream>
using namespace std;

int main()
{
    //cout << "Hello World!\n";

    char X[5] = "";
    char Y[5] = "";

    char mypalin[5] = "";
    int mylen = 0;

    cin >> X;

    cin >> Y;

    int mylenX = sizeof(X);
    int mylenY = sizeof(Y);
    
    int i = 0;
    int j = 0;
    int counter = 0;
    int palincount = 0;
    for (i = 0; i < mylenX; i++)
    {
        counter = 0;
        for (j = i; j < mylenY; j++)
        {
            if (X[i] != Y[j])
            {
                break;
            }
            else if ((X[i] == Y[j]) && (counter == 0))
            {
                mypalin[palincount] = X[i];
                cout << "palincount = " << palincount << endl;
                cout << mypalin[palincount] << endl;
                palincount++;
                //break;
                counter++;
                break;
            }
        }
    }

    //mypalin[palincount + 1] = '\n';

    cout << "Palindrome Count = " << palincount << endl;
    cout << "Palindrome = " << mypalin << endl;
    return 0;
}
