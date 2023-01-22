#include <iostream>
#include <string>
int main()
{
 std::cout << "Please enter P1 name: ";
 std::string p1_name;
 std::cin >> p1_name;
 
 std::cout << "Please enter P2 name: ";
 std::string p2_name;
 std::cin >> p2_name;

 const std::string names = "Player 1: " + p1_name + " * " + "Player 2: " + p2_name;
 const std::string spaces(names.size()/2, ' ');
 const std::string second = "* " + spaces + "*" + spaces + "*";
 const std::string first(second.size(), '*');
 std::cout << std::endl;
 std::cout << first << std::endl;
 std::cout << second << std::endl;
 std::cout << "* " << names << " *" << std::endl;
 std::cout << second << std::endl;
 std::cout << first << std::endl;

 return 0;
}
