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

 const std::string name1 = "Player 1: " + p1_name;
 const std::string name2 = "Player 2: " + p2_name;
 const std::string spaces(std::max(name1.size(), name2.size()), ' ');
 const std::string space1(spaces.size() - name1.size(), ' ');
 const std::string space2(spaces.size() - name2.size(), ' ');
 const std::string second = "| " + spaces + " |";
 const std::string first(second.size() - 2, '=');
 const std::string mid(second.size() - 2, '-');

 std::cout << std::endl;
 std::cout << "+" << first << "+" << std::endl;
 std::cout << second << std::endl;
 std::cout << "| " << name1 << space1 << " |" << std::endl;
 std::cout << second << std::endl;
 std::cout << "+" << mid << "+" << std::endl;
 std::cout << second << std::endl;
 std::cout << "| " << name2 << space2 << " |" << std::endl;
 std::cout << second << std::endl;
 std::cout << "+" << first << "+" << std::endl;
 return 0;
}
