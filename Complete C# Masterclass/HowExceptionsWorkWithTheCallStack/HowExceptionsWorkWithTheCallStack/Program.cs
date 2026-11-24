using System.Diagnostics;

namespace TryCatchExceptions
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("App running before the try block");
            try
            {
                LevelOne();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception caught in Main: " + ex.Message);
            }
            Console.WriteLine("App is still running!");
            Console.ReadKey();
        }

        static void LevelOne()
        {
            LevelTwo();
        }

        static void LevelTwo()
        {
            Console.WriteLine("Level two before throw!");
            throw new FormatException("Something went wrong!");
            Console.WriteLine("Level two After throw!");
        }
    }
}
