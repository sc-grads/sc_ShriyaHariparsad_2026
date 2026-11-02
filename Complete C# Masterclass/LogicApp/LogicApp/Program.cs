int num1 = 0;
int num2 = 0;

bool isEqual = num1 == num2;

bool isNotEqual = num1 != num2;

Console.WriteLine("Please enter a whole number");

if (num1 == int.Parse(Console.ReadLine()))
{
    Console.WriteLine("Numbers are equal!");
}
else
{
    Console.WriteLine("Numbers aren't equal");
}

/*

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


bool isRainy = true;
bool hasUmbrella = false;

// Logical Operators
// AND &&
// OR  ||
// NOT !

// Variants of OR statements
// true || true -> true
// true || false -> true
// false|| true -> true
// false|| false -> false

// Variants of the AND operator/statements
// true  && true -> true
// true  && false -> false
// false && true -> false
// false && false -> false


if (isRainy && !hasUmbrella)
{
    //Console.WriteLine("I'M getting wet!");
}
//Console.WriteLine("Ay OK!");
Console.ReadKey();





