using System;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;

class Result
{
    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void miniMaxSum(List<int> arr)
    {
        long total = arr.Sum();
        long min = arr.Min();
        long max = arr.Max();

        long min_sum = total - max;
        long max_sum = total - min;
        Console.WriteLine(min_sum + " " + max_sum);
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        List<int> arr = Console
            .ReadLine()
            .TrimEnd()
            .Split(' ')
            .ToList()
            .Select(arrTemp => Convert.ToInt32(arrTemp))
            .ToList();

        Result.miniMaxSum(arr);
    }
}
