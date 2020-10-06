#include <stdio.h>
using namespace std;
/* https://projecteuler.net/problem=1 */


int main(int argc, char** argv)
{
    unsigned int sum = 0;
    for(int i = 1; i < 1001; ++i)
        if(!(i % 3) && !(i % 5))
            sum += i;
    std::cout << i;
    return 0;
}