package internal

import "fmt"

/*
	 main -> Println -> FPrintln -> File.Write()
		-> File.write()->OS固有のsyscallの呼び出しというふうに処理が行われる

		OSは、syscallをファイルディスクリプたというものに対して呼び出す。
		これは一種の識別子のことであり、数値に対応するものにアクセスできる
		標準入出力や、ソケット、OSなどにも割り振られていて同じようにアクセスできる。

		ファイルディスクリプタは、stdin,stdout,stderrであり、プロセス生成時に割り当てられる。

		Goの場合は、ファイルディスクリプタの仕組みを、言語レベルで模倣しているため、OSによるAPIの差異を吸収している
*/
func HelloWorld() {
	fmt.Println("Hello World")
}
