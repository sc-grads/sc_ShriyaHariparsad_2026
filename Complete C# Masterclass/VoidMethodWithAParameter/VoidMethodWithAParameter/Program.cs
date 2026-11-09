Con// Methods are structured like this
// modifier returnType MethodName(Parameters){
// code block
// }

int AddTwoValues(int value1, int value2)
{
    int result = value1 + value2;
return result;
}

int num1 = int.Parse(Console.ReadLine());

int myResult = AddTwoValues(num1, 10);
Console.WriteLine("The result is " + myResult);
Console.ReadKey();


