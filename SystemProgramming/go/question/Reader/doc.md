# io.Reader

io.Writer と反対で、読み込みを行う際に使用される。

ファイルのデータなどを読み取りする際にいちいちバッファの管理をしながら、Read でデータを読み取りするのはめんどくさい。
なので、io.Reader を簡単に使えるように、ラッパー関数が多く提供されている

## io.Reader のラッパー

### io.ReadAll

多く使われるのは、io.ReadAll()であり、終端記号にあたるまでのすべてのデータを読み込んで返す。

### io.ReadFull

決まったバイト数だけ確実に読み込みたい場合には、io.ReadFull()を使う

### コピーの補助関数

io.Reader から io.Writer にデータをそのまま渡す際に使われる
たとえば、ファイルを開いてそのまま HTTP で送信したい時など

### defer

ファイルを開いたりした際には、Close をしないといけない。このような場合に下記のように呼び出すことでスコープが終了した際にdeferの処理が実行される

```go
file, err := os.Open("file.go")
if err != nil {
    panic(err)
}
defer file.Close()
```
