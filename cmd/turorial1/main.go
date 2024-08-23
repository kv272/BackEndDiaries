package main

import "fmt"

func main() {
	var intNum int = 10
	newNum := 10
	fmt.Println(newNum)
	fmt.Println(intNum)
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
	var arr1 = []string{"a", "b", "c", "d", "e"}
	fmt.Println(arr1)
	var myvalue string = "new string"
	fmt.Println(myvalue)
	fmt.Println(myvalue + "" + "hello brother")
}
