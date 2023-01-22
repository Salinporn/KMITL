// tag::lab1-3b[]
//// lab1_3.cpp
#include "random.hpp"

#include <iomanip>
#include <iostream>
#include <vector>

template<typename T_>
inline constexpr
    T_ pi_v{3.141592653589793238462643383279502884L};

inline constexpr double pi = pi_v<double>;

int main()
{
    constexpr double rnd_min = -1.0, rnd_max = 1.0;
    Rand_double rnd{rnd_min, rnd_max};

    std::random_device rd;
    rnd.seed(rd());
    std::cout << std::fixed << std::setprecision(6);

    const int n = 100;
    double count = 0;
     
    for (int i=0; i < n; i++) {
        double x1 = rnd();
        double y1 = rnd();
        // std::cout << "Point: (" << x1 << ", " << y1 << ")\n";
        double d = sqrt(x1*x1 + y1*y1);
        if (d <= 1) {
            count = count + 1;
        }
    }
    double pie = 4.0 * (count / n);
    double diff = (pi - pie);
    double percentErr = diff / pi;

    std::cout << pie << std::endl;
    std::cout << diff << std::endl;
    std::cout << percentErr << std::endl;
    return 0;
}