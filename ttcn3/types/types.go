package types

import (
	"fmt"
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Error struct {
	Fset *syntax.FileSet // file set for interpretation of Pos
	Pos  syntax.Pos      // error position
	Msg  string          // error message
	Soft bool            // if set, error is "soft"
}

// Error returns an error string formatted as follows:
// filename:line:column: message
func (err Error) Error() string {
	return fmt.Sprintf("%s: %s", err.Fset.Position(err.Pos), err.Msg)
}

type Config struct {
	Error func(err Error)
}

type Info struct {
	Defs   map[*syntax.Ident]Object
	Uses   map[*syntax.Ident]Object
	Scopes map[syntax.Node]*Scope
}

func (conf *Config) Check(fset *syntax.FileSet, m *syntax.Module, info *Info) (*Module, error) {
	mod := NewModule("")
	return mod, NewChecker(conf, fset, mod, info).Module(m)
}
