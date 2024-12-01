using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AdventOfCode2024
{
    class DayOne
    {
        public static void DayOneAns()
        {
            List<int> list1 = new List<int>();
            List<int> list2 = new List<int>();

            int diff = 0;
            int SimScore = 0;

            // Reading from file
            foreach (var row in File.ReadLines("DayOne/dayone.txt"))
            {
                var rows = row.Split(' ', StringSplitOptions.RemoveEmptyEntries);
                if (rows.Length == 2)
                {
                    list1.Add(int.Parse(rows[0]));
                    list2.Add(int.Parse(rows[1]));
                }
            }

            var sortedList1 = list1.OrderBy(x => x).ToList();
            var sortedList2 = list2.OrderBy(x => x).ToList();

            // For Difference Score
            for (int i = 0; i < sortedList1.Count; i++)
            {
                diff += Math.Abs(sortedList1[i] - sortedList2[i]);
            }

            // For Similarity Score
            foreach (var item in list1)
            {
                int searchCount = list2.Count(x => x == item);
                SimScore += item * searchCount;
            }

            // Output results
            Console.WriteLine($"Difference: {diff}");
            Console.WriteLine($"Similarity Score: {SimScore}");
        }
    }
}