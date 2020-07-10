# Python Code ~ not working for now
# class AdvancedArithmetic(object):
#     def divisorSum(n):
#         raise NotImplementedError
#
#
# class Calculator(AdvancedArithmetic):
#     def divisorSum(n):
#         divisor_sum = 0
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 divisor_sum += i
#         return divisor_sum
#
#
# n = int(input())
# my_calculator = Calculator()
# s = my_calculator.divisorSum(n)
# print("I implemented: " + type(my_calculator).__bases__[0].__name__)
# print(s)

# JAVA Code working for now
import java.io.*;
import java.util.*;

interface AdvancedArithmetic {
    int divisorSum(int n);
}

class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (n%i == 0) {
                sum += i;
            }
        }
        return sum;
    }
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in );
        int n = scan.nextInt();
        scan.close();

        AdvancedArithmetic myCalculator = new Calculator();
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}