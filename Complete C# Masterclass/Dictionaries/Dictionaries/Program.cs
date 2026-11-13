namespace Dictionaries
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // key - value
            // Declaring and initializing a Dictionary
            Dictionary<int, string> employees = new Dictionary<int, string>();

            // Adding Items to a Dictionary
            employees.Add(101, "John Doe");
            employees.Add(102, "Bob Smith");
            employees.Add(103, "Rob Smith");
            employees.Add(104, "Flob Smith");
            employees.Add(105, "Dob Smith");

            // access items in a dictionary
            string name = employees[101];
            //Console.WriteLine(name);

            // update data in a dictionary
            employees[102] = "Jane Smith";

            // remove an item from a dictionary
            employees.Remove(101);



            if (!employees.ContainsKey(104))
            {
                employees.Add(104, "Mike Jike");
            }

            bool added = employees.TryAdd(102, "Michal Brims");
            if (!added)
            {
                Console.WriteLine("Employee with the id of 102 already exists");
            }

            /*
            int counter = 101;

            while (employees.ContainsKey(counter))
            {
                counter++;
            }
            employees.Add(counter, "Jesus Christ");
            */

            // Iterating over a dictionary
            foreach (KeyValuePair<int, string> employee in employees)
            {
                Console.WriteLine($"ID: {employee.Key}, Name: {employee.Value}");
            }



            Console.ReadKey();
        }
    }
}
