int month = 2;
string monthName;

if (month == 1)
{
    monthName = "January";
}

else if (month == 2)
    monthName = "February";
else if (month == 3)
    monthName = "March";
else
    monthName = "Unknown";


switch (month)
{
    case 1:
        monthName = "January";
        break;
    case 2:
        monthName = "February";
        break;
    case 3:
        monthName = "March";
        break;
    default:
        monthName = "Unknown";
        break;
}

Console.WriteLine($"The month is {monthName}");



/*
int num1 = 0;
int num2 = 0;
int age = 0;


bool isEqual = num1 == num2;

bool isNotEqual = num1 != num2;

Console.WriteLine("Please enter a whole number");

if (num1 == int.Parse(Console.ReadLine()))
{
    Console.WriteLine("Numbers are equal!");

    Console.WriteLine("Please enter your age");
    age = int.Parse(Console.ReadLine());
    if (age >= 18)
    {
        Console.WriteLine("Please enter your address, " +
            "so that we can send you the price!");
        string address = Console.ReadLine();
       
    }
    else
    {
        Console.WriteLine("Sorry, you can't get your price due to your age!");
        
    }

}
else
{
    Console.WriteLine("Numbers aren't equal");
}

age = 0;




int age = 16;
bool isWithParents = true;

if(age >= 13 && isWithParents)
{
    Console.WriteLine("Go party in the club with your parents!");
}else if (age > 18)
{
    Console.WriteLine("Go party in the club!");
}
else
{
    Console.WriteLine("Go party in Kindergarten!");
}

*/

Console.ReadKey();


