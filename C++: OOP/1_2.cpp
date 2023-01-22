#include <iostream>
#include <string>

int main()
{
 std::cout << "Warrior: ";
 std::string warrior;
 std::cin >> warrior;
 
 std::cout << "Mage: ";
 std::string mage;
 std::cin >> mage;

 std::cout << "Ninja: ";
 std::string ninja;
 std::cin >> ninja;

 std::cout << "Fighter: ";
 std::string fighter;
 std::cin >> fighter;

 const std::string name1 = "Warrior: " + warrior;
 const std::string name2 = "Mage:    " + mage;
 const std::string name3 = "Ninja:   "+ ninja;
 const std::string name4 = "Fighter: " + fighter;

 const int line1 = std::max(name1.size(), name2.size());
 const int line2 = std::max(name3.size(), name4.size());
 const std::string spaces(std::max(line1, line2), ' ');

 const std::string space1(spaces.size() - name1.size(), ' ');
 const std::string space2(spaces.size() - name2.size(), ' ');
 const std::string space3(spaces.size() - name3.size(), ' ');
 const std::string space4(spaces.size() - name4.size(), ' ');
 const std::string second = "| " + spaces + " | " + spaces + " |";
 const std::string first(second.size()/2 - 1, '=');
 const std::string mid(second.size()/2 - 1, '-');

 std::cout << std::endl;
 std::cout << "+" << first << "+" << first << "+" << std::endl;
 std::cout << second << std::endl;
 std::cout << "| " << name1 << space1 << " | " << name2 << space2 << " |" << std::endl;
 std::cout << second << std::endl;
 std::cout << "+" << mid << "+" << mid << "+" << std::endl;
 std::cout << second << std::endl;
 std::cout << "| " << name3 << space3 << " | " << name4 << space4 << " |" << std::endl;
 std::cout << second << std::endl;
 std::cout << "+" << first << "+" << first << "+" << std::endl;
 return 0;
}