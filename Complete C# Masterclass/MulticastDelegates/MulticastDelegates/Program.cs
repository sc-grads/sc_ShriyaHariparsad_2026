namespace DelegatesAndEvents
{

    public delegate void LogHandler(string message);

    public class Logger
    {
        public void LogToConsole(string message)
        {
            Console.WriteLine("Console Log: " + message);
        }

        public void LogToFile(string message)
        {
            Console.WriteLine("File log: " + message);
        }
    }


    internal class Program
    {


        static void Main(string[] args)
        {
            Logger logger = new Logger();

            // Creating a multicast delegate
            LogHandler logHandler = logger.LogToConsole;
            logHandler += logger.LogToFile;

            // invoking the multicast delegate
            logHandler("Log this info!");

            // Removing a method from the multicast delegate
            logHandler -= logger.LogToFile;

            logHandler("After removing LogToFile");

            Console.ReadKey();
        }



    }
}
