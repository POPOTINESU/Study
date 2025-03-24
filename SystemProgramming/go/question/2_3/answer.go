package main

import (
	"compress/gzip"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

/*
JSON をgzip 化してクライアントに返すウェブサービスを開発しているとします。
本章で説明したようにhttp.ResponseWriter を指定してJSON エンコーダーで変
換をかけるとJSON が生成できますが、そのままではどのようなレスポンスをクラ
イアントに返したのかログを残すことができません。os.Stdout に出力するとログ
が残るものとして、JSON の文字列変換、gzip 圧縮を行いながら圧縮前の出力を標
準出力にも出すように、io.MultiWriter を使ってみましょう。gzip 出力の最後に
Flush() が必要な点に注意してください。
*/
func handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Encoding", "gzip")
	w.Header().Set("Content-Type", "application/json")
	source := map[string]string{
		"sample": "code",
	}

	gzipWriter := gzip.NewWriter(w)
	defer gzipWriter.Close()

	writer := io.MultiWriter(gzipWriter, os.Stdout)
	encoder := json.NewEncoder(writer)
	if err := encoder.Encode(source); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	fmt.Println("Response sent successfully")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}
