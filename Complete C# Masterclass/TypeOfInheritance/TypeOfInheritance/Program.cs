namespace InheritanceApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dog myDog = new Dog();
            myDog.Bark();
            myDog.Eat();

            Console.ReadKey();
        }
    }

    // Base Class  (Parent Class or Superclass): The class whose members are inherited
    class Animal
    {
        public void Eat()
        {
            Console.WriteLine("Eating...");
        }
    }

    //Derived Class(Child Class or Subclass):
    //The class that inherits the members of the base class.
    class Dog : Animal
    {
        public void Bark()
        {
            Console.WriteLine("Barking...");
        }
    }

    class Cat : Animal
    {
        public void Miau()
        {
            Console.WriteLine("Cat is meowing");
        }
    }

    // A breed of dog
    class Collie : Dog
    {
        public void GoingNuts()
        {
            Console.WriteLine("Collie going Nuts");
        }
    }


}

