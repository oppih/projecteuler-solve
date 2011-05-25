#include<iostream>
using namespace std;
// to find lowest divisble number till 20

int main()
{
int num = 20, flag = 0;

while(flag == 0)
{
    int divisor; 
    for (divisor=2; divisor<=20; divisor++)
    {
        if (num%divisor != 0)
            break;
    }
    if (divisor != 21)
    {
        flag =  1;
        cout<< " lowest divisible number upto 20 is  "<< num<<endl;
    }
    num++;
}
}
