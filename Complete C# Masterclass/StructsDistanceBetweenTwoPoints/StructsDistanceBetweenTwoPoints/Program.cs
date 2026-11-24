namespace StructsApp1
{
    public struct Point
    {
        // It’s a common practice to make structs immutable
        // by declaring all fields as readonly and providing only
        // get accessors for properties.
        public double X { get; }
        public double Y { get; }


        public Point(double x, double y)
        {
            X = x;
            Y = y;
        }

        public double DistanceTo(Point other)
        {
            double dx = other.X - X;
            double dy = other.Y - Y;
            return Math.Sqrt(dx * dx + dy * dy);
        }

        public void Display()
        {
            Console.WriteLine($"Point: ({X},{Y})");
        }
    }


    internal class Program
    {
        static void Main(string[] args)
        {
            Point p1 = new Point(10, 20);
            p1.Display();

            Point p2 = new Point(20, 30);
            p2.Display();

            double distance = p1.DistanceTo(p2);

            Console.WriteLine($"Distance between points: {distance:F5}");


            Console.ReadKey();

        }
    }
}

