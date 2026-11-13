using System.Globalization;

namespace ListsApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int> { 10, 5, 15, 3, 9, 25, 18 };

            Console.WriteLine("Unsorted list!");
            foreach (int number in numbers)
            {
                Console.WriteLine(number);
            }

            // Define the predicate to check if a number is greater than 10
            Predicate<int> isGreaterThanTen = x => x > 10;

            List<int> higherTen = numbers.FindAll(isGreaterThanTen);


            Console.WriteLine("All number 10 and higher in our list numbers");
            foreach (int number in higherTen)
            {
                Console.WriteLine(number);
            }


            Console.ReadKey();
        }

        // A lambda expression consists of 2 Parts
        // 1. Parameters
        // 2. Expression or Statement Block

        // Parameters are written on the left side of =>
        // (this symbol is read as "goes to" or "becomes").
        // The expression or action to perform is on the right side.

        //This reads as:
        //"Take an input x and turn it into x multiplied by x."
        //x => x * x;

        static int Squaring(int num1)
        {
            return num1 * num1;
        }
    }
}

