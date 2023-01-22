# include<iostream>

int main()
{
    int number = 0;
    float value = 0;
    double bigNumber;
    std::cout << number << std::endl;
    std::cout << value << std::endl;
    std::cout << bigNumber << std::endl;

    //reassign bigNumber variable
    bigNumber = number + value;
    std::cout << bigNumber << std::endl;
    return 0;
}