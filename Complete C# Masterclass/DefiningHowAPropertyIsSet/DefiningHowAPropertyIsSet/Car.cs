using System;
using System.Collections.Generic;
using System.Data;
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

        // Property

        public string Model { get => _model; set => _model = value; }
        public string Brand
        {
            get => _brand;

            set
            {
                if (string.IsNullOrEmpty(value))
                {
                    Console.WriteLine("You entered NOTHING!");
                    _brand = "DEFAULTVALUE";
                }
                else
                {
                    _brand = value;
                }
            }

        }

        // Custom Constructor
        public Car(string model, string brand)
        {
            Model = model;
            Brand = brand;
            Console.WriteLine($"A {Brand} of the" +
                $" model {Model} has been created");
        }
    }
}
