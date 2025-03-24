package network

import (
	"io"
	"net"
	"net/http"
	"os"
)

/*
example.comから返ってきたレスポンスを画面に出力する
これもio.Writerを受けとって使っている
*/
func Conn() {
	conn, err := net.Dial("tcp", "example.com:80")
	if err != nil {
		panic(err)
	}
	req, err := http.NewRequest("GET", "http://example.com", nil)
	if err != nil {
		panic(err)
	}
	req.Write(conn)
	io.Copy(os.Stdout, conn)
}

/*
HTTPリクエストのサンプル
通常Writeメソッドを使う場合は少ないが、特殊な用途では必要になる
*/
func SampleHTTP() {
	request, err := http.NewRequest("GET", "http://example.com", nil)
	if err != nil {
		panic(err)
	}
	request.Header.Set("X-TEST", "sample")
	request.Write(os.Stdout)
}
