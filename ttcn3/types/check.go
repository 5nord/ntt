package types

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Checker struct {
	conf *Config
	fset *syntax.FileSet
	mod  *Module
	*Info
	ast *syntax.Module
}

func (check *Checker) Module(m *syntax.Module) error {
	return nil
}

func NewChecker(conf *Config, fset *syntax.FileSet, mod *Module, info *Info) *Checker {
	if conf == nil {
		conf = new(Config)
	}

	if info == nil {
		info = new(Info)
	}

	return &Checker{
		conf: conf,
		fset: fset,
		mod:  mod,
		Info: info,
	}
}
