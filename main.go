package main

import (
	"github.com/nokia/ntt/internal/cmd"
	"runtime/debug"
)

func main() {
	debug.SetGCPercent(20000)
	cmd.Execute()
}
