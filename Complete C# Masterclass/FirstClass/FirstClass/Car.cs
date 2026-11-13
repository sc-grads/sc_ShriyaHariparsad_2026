using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassesApp
{
    // It's internal, which means that 
    //it can only be accessed from
    //within the same assembly.
    internal class Car
    {
        // Constructor
        public Car()
        {

            Console.WriteLine("An Object of Car has " +
                "been created!");
        }
    }
}

