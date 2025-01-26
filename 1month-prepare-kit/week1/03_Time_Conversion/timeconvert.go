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
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

func timeConversion(s string) string {
	// Write your code here
	const format = "19:59:59"
	const inputFormat = "07:05:45PM"

	var strHour string = s[0:2]

	timeItem := strings.Split(s, ":")
	if timeItem[0] == "12" {
		timeItem[0] = "00"
	}
	if strings.Contains(s, "PM") {
		h, err := strconv.Atoi(timeItem[0])
		if err != nil {
			// ... handle error
			panic(err)
		}
		strHour = fmt.Sprint(h + 12)
	} else {
		strHour = fmt.Sprint(timeItem[0])
	}
	return strHour + ":" + timeItem[1] + ":" + timeItem[2][0:2]
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	s := readLine(reader)

	result := timeConversion(s)

	fmt.Fprintf(writer, "%s\n", result)

	writer.Flush()
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
