package main

import (
	"encoding/csv"
	"os"
)

/*
encoding/csv というパッケージがあります。
このパッケージを使って、標準出力やファイルにCSV データを出力してみましょう。
Flush() メソッドを呼ぶのを忘れないでください。
*/
func main() {
	records := [][]string{
		{"名前", "年齢", "性別"},
		{"父", "24", "男"},
		{"母", "24", "女"},
		{"子供", "0", "男"},
	}
	// csvパッケージを使ってio.Writerをラップしている
	w := csv.NewWriter(os.Stdout)

	// writeでバッファに書き込んで溜め込む
	for _, record := range records {
		// WriteAllを使わない場合は、明示的にFlushしないといけない
		if err := w.Write(record); err != nil {
			panic(err)
		}
	}

	// 明示的に出力を行う
	w.Flush()

	// Flushでエラーが発生している場合のエラーハンドリング
	if err := w.Error(); err != nil {
		panic(err)
	}
}
