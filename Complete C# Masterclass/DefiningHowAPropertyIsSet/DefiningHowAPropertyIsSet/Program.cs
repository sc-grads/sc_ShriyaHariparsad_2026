using System.Runtime.ConstrainedExecution;

namespace ClassesApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Creating an object of the Class Car
            // Creating an instance of the Class Car
            Car audi = new Car("A3", "Audi");
            Car bmw = new Car("i7", "BMW");

            Console.WriteLine("Please enter the Brand name");
            // "SETTING BRAND"
            audi.Brand = "CAR";

            // GETTING BRAND
            Console.WriteLine("Brand is " + audi.Brand);


            Console.ReadKey();
        }
    }
}

