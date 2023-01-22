#include <iostream>
#include <iomanip>

int main()
{
    std::cout << "Fahr" << "\t" << std::setw(7) << std::setiosflags(std::ios::right) << "Celcius" << std::endl;
    for (int fahr = 300; fahr >= 0; fahr = fahr - 20) {
        double celc = (fahr - 32.0) * (5.0/9.0);
        std::cout << std::setw(3) << std::setiosflags(std::ios::right) << fahr << "\t";
        std::cout << std::fixed;
        std::cout << std::setprecision(1);
        std::cout << std::setw(7) << std::setiosflags(std::ios::right) << celc << std::endl;
    }
    return 0;
}