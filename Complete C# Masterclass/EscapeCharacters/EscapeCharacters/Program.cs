// in strings \ is an "Escape Character"
// \n stands for "new line"
// \r - carriage return

string myString = "Hi \r\nHi";

for (int counter = 10; counter >= 0; counter--)
{
    Console.WriteLine("Counter is " + counter);
    Thread.Sleep(1000);
}


Console.ReadKey();


