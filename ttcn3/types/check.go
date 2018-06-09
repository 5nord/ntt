package types

import (
	//"fmt"
	"github.com/nokia/ntt/ttcn3/syntax"
)

type bailout struct{}

type Checker struct {
	conf *Config
	fset *syntax.FileSet
	mod  *Module
	*Info
	ast *syntax.Module
}

func (check *Checker) Module(m *syntax.Module) error {
	//moduleScope := NewScope(check.pkg.scope, pos, end, check.filename(fileNo))
	//check.recordScope(file, fileScope)

	for _, moduleDef := range m.Decls {
		switch x := moduleDef.Def.(type) {
		//case *syntax.FuncDecl:
		//	fmt.Println(x.Name.Tok.Lit)
		default:
			check.invalidAST(x.Pos(), "unknown module definition node %T", x)
		}

	}
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
