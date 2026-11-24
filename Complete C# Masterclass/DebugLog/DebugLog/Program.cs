using System.Diagnostics;

namespace TryCatchExceptions
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int result = 0;

            Debug.WriteLine("Main method is running");

            try
            {
                Console.WriteLine("Please enter a number");
                int num1 = int.Parse(Console.ReadLine());
                //int num1 = 0;
                int num2 = 2;
                result = num2 / num1;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
                // This next line is only executed during "Debugging"
                Debug.WriteLine(ex.ToString());
            }
            finally
            {
                // Code to cleanup or finalize
                // ideal for cleaning up resources,
                // like closing file streams or database connections.

                Console.WriteLine("This always executes");
            }

            // Don't forget to listen to these trace messages

            Console.WriteLine("Result: " + result);
            Console.ReadKey();



        }
    }
}

