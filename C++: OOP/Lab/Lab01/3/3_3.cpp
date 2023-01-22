#include <iostream>
#include <string>
int main()
{
 std::cout << "Please enter size: ";
 int size;
 std::cin >> size;
 for (int i = 0; i < size; i++) {
    std::string space(size - (i+1), ' ');
    std::string star(i+1, '*');
    std::cout << space << star << std::endl;
 }
 for (int i = 0; i < size - 1; i++) {
    std::string space(i+1, ' ');
    std::string star(size - (i+1), '*');
    std::cout << space << star << std::endl;
 }
}
