// datatype variableName = initial value;
double myNumber1 = 0.0;
double myNumber2 = 0.0;

// Prints out whatever is in side of ()
Console.WriteLine("Enter a number!");

// takes the user input and stores it
// Variable with the name "userInput" and the data type "string"
// strings are used for text 
string userInput = Console.ReadLine();
//myNumber = int.Parse(Console.ReadLine());
myNumber1 = double.Parse(userInput);

Console.WriteLine("Enter a number!");
userInput = Console.ReadLine();
myNumber2 = double.Parse(userInput);



double sum = myNumber1 + myNumber2;
sum = Math.Round(sum, 2);

// we are adding to strings together and writing them onto the console
Console.WriteLine("The result of " + myNumber1 + " and " + myNumber2 + " is " + sum);
Console.ReadKey();


