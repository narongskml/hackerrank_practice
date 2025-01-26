package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the 'miniMaxSum' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

func miniMaxSum(arr []int32) {
    // Write your code here
    var arrSum int64 =0
    var arrMin int64 =int64(arr[0])
    var arrMax int64 =int64(arr[0]) 
    for _, num:= range arr {
        arrSum = arrSum+int64(num)
        
        if ( int64(num)<arrMin ){
            arrMin=int64(num)
        }
        
        if ( int64(num)>arrMax ){
            arrMax=int64(num)
        }
    }
    fmt.Printf("%d %d", arrSum-arrMax,arrSum-arrMin)   
   
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var arr []int32

    for i := 0; i < 5; i++ {
        arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    miniMaxSum(arr)
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
