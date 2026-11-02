Console.WriteLine("How old are you? Write a whole number");
int age = int.Parse(Console.ReadLine());
bool isWithParents = false;

if (age >= 18)
{
    Console.WriteLine("Go party in the club!");
}
else if (age >= 13)
{
    Console.WriteLine("Are you with your parents? Answer with y or n");
    string isWithParentsString = Console.ReadLine();
    if (isWithParentsString == "y")
    {
        Console.WriteLine("Go party in the club with your parents!");
    }
    else
    {
        Console.WriteLine("No party for you today");
    }

}
else
{
    Console.WriteLine("Go party in Kindergarten!");
}

Console.ReadKey();
