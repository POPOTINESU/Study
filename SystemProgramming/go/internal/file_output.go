package internal

import (
	"os"
)

/*
書き込みの際は、io.Writerインターフェースにより抽象化されていて、文字に限らずさまざまな用途で使用することができる
*/
func FileOutput() {
	file, err := os.Create("text.txt")
	if err != nil {
		panic(err)
	}
	file.Write([]byte("os.File Hello World\n"))
	file.Close()
}

/*
ターミナルへの出力
fmt.Println()で最終的に呼び出していたコードと同じもの
*/
func TerminalOutPut() {
	os.Stdout.Write([]byte("os.Stdout \n"))
}