namespace TryCatchExceptions
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int result = 0;

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
            }
            finally
            {
                // Code to cleanup or finalize
                // ideal for cleaning up resources,
                // like closing file streams or database connections.

                Console.WriteLine("This always executes");
            }

            Console.WriteLine("Result: " + result);
            Console.ReadKey();



        }
    }
}

