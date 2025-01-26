using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace diagonalDifference
{
    public class Result
    {
        /*
     * Complete the 'diagonalDifference' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY arr as parameter.
     */
        public static int diagonalDifference(List<List<int>> arr)
        {
            int iresult = 0;
            List<int> v1=new List<int>();
            List<int> v2=new List<int>();   
            int size = arr.Count;
            var nonEmptySublists = arr.Where(sublist => sublist.Any());
            int minValue = nonEmptySublists.SelectMany(sublist => sublist).Min();
            int maxValue = nonEmptySublists.SelectMany(sublist => sublist).Max();
            if (minValue < -100 && maxValue >100)
            {
                throw new ArgumentException("Value must between 0 to 100");
            }
            for (int i = 0;  i < size; i++)
            {
                v1.Add(arr[i][i]);
                v2.Add(arr[size-1-i][i]);
            }
            iresult= Math.Abs(v1.Sum()-v2.Sum());
            return iresult;
        }
    }
}