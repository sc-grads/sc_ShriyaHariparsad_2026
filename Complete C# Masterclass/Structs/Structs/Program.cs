namespace StructsApp1
{
    public struct Point
    {
        //public int X { get; set; }
        //public int Y { get; set; }

        public int X;
        public int Y;

        public Point(int x, int y)
        {
            X = x;
            Y = y;
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

            Point p2;
            p2.X = 10;
            p2.Y = 20;
            p2.Display();

            Point p3 = p1;
            p3.X = 50;
            p1.Display();
            p3.Display();

            Console.ReadKey();

        }
    }
}

