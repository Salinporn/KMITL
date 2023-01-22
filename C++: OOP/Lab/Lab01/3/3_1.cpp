#include <iostream>
#include <string>
int main()
{
 std::cout << "Please enter size: ";
 int size;
 std::cin >> size;
 for (int i = 0; i < size; i++) {
    std::string space(i+1, '*');
    std::cout << space << std::endl;
 }
}
