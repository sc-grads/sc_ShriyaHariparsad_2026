for (int i = 0; i < 4; i++)
{
    Console.WriteLine(i);
    if (i == 2)
    {
        //Console.WriteLine("I have had enough!");
        continue;
    }
    Console.WriteLine(i);

}

Console.ReadKey();
