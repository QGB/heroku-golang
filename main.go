package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", hello)
	if err := http.ListenAndServe(":"+"8083", nil); err != nil {
		panic(err)
	}
}

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "<h1>Hello Full Cycle Developers</h1>")
}
