using System.Globalization;

namespace ListsApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int> { 10, 5, 15, 3, 9 };

            Console.WriteLine("Unsorted list!");
            foreach (int number in numbers)
            {
                Console.WriteLine(number);
            }

            numbers.Sort();
            Console.WriteLine("Sorted List");
            foreach (int number in numbers)
            {
                Console.WriteLine(number);
            }


            Console.ReadKey();
        }
    }
}

