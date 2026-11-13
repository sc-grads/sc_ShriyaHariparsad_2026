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
        // member variable
        // private hides the variable from other classes
        private string _model = "";

        private string _brand = "";

        // Constructor
        public Car(string model, string brand)
        {
            _model = model;
            _brand = brand;
            Console.WriteLine($"A {_brand} of the" +
                $" model {_model} has been created");
        }
    }
}
