using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace lonelyinteger
{
    public class Result
    {
        /*
        * Complete the 'lonelyinteger' function below.
        *
        * The function is expected to return an INTEGER.
        * The function accepts INTEGER_ARRAY a as parameter.
        */
        public static int lonelyinteger(List<int> a)
        {
            int n = a.Count;
            if (n % 2 == 0)
            {
                throw new Exception("item must be odd value");
            }

            if (a.Min() < 0 && a.Max() > 100)
            {
                throw new Exception("value must between 0 to 100 ");
            }

            // find distinct value
            var dist = a.Distinct();
            List<int> resultList = new List<int>();
            foreach (var i in dist)
            {
                var check = a.Where(x => x == i).Count();
                if (check == 1)
                {
                    resultList.Add(i);
                }
            }

            return resultList.FirstOrDefault();
        }
    }
}
