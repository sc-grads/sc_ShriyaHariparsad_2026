//conversion helpers parse and convert

string numberString = "123";
int result = int.Parse(numberString);

string myBoolString = "true";
bool myBool = Convert.ToBoolean(myBoolString);
Console.WriteLine("myBool is " + myBool);

Console.ReadKey();
