package types

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Config struct {
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
