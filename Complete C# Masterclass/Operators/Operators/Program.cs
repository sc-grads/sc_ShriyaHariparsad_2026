// Operators and Order of Evaluation
int num1 = 14;
int num2 = 13;

//5.3 as int will still be 5

// Concatination
Console.WriteLine("Age is " + num1);

Console.WriteLine("Addition num1 + num2 = " + (num1 + num2));
//Order of Evaluation
Console.WriteLine("Subtraction num1 - num2 = " + (num1 - num2));
// "Subtraction num1 - num2 = 5" - 13



Console.WriteLine("Multiplication num1 * num2 = " + num1 * num2);
Console.WriteLine("Division num1 / num2 = " + num1 / num2);



//5+3-8*2
//  5+3-16 = 8
// 5+(3-8)*2
// 5 + (-5)*2
// 5 + -10
// - 5



// implicitely typed variable
var myFavoriteGenre = "LitRPGs";

var myFavoriteNumber = 13;

var yourFavoriteNumber = 14;

var ourNumbersCombined = myFavoriteNumber + yourFavoriteNumber;


// Referency Type
// explicitely typed variable
string myName = "Denis";

// defining or setting up a variable
string petsName;

// initialize variable
petsName = "Daisy";
//Console.WriteLine($"my pet is {petsName}");

// assign a new value
petsName = "Barky";
//Console.WriteLine($"my pet is {petsName}");

Console.ReadKey();

// Value Types
int myAge = 35;
//double pi = -3.14;

byte age = 255;

short linkdinConnections = 32550;

long phoneNumber = 017657723991;

float pi = 3.14f;

