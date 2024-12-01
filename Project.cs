using System;

namespace AdventOfCode2024
{
    class Program
    {
        static void Main()
        {
            while(true)
            {
                Console.Write("Select a day to view (1-25) | Q to quit: ");

                string response = Console.ReadLine();

                switch (response)
                {
                    case "1":
                        DayOne.DayOneAns();
                        break;
                    case "q":
                    case "Q":
                        System.Environment.Exit(0);
                        break;
                    default:
                        Console.WriteLine();
                        Console.WriteLine("!! That day has yet to come to pass !!");
                        Console.WriteLine();
                        break;
                }
            }
        }
    }
}