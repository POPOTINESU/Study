package main

import (
	"fmt"
	"os"
)

/*
fmt.Fprintf(writer, フォーマット文字列, 値...) でio.Writer に数値や文字列を
出力できます。fmt.Fprintf() では、他の言語と同じように、"%d" が数値の表示
に、"%s" が文字列の表示に、"%f" が浮動小数点数の表示に使えます。
これらを使って、数字や小数、文字列をファイルに書き出してみましょう。
*/
func main() {
	fmt.Fprintf(os.Stdout, "%d %f %s", 10, 3.14, "sample")
}
