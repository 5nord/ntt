package loader

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Config struct {
	Files   []string
	Modules []*syntax.Module

	fset *syntax.FileSet
}

func LoadFromFiles(files []string) error {
	fset := syntax.NewFileSet()
	_, err := parseFiles(fset, files)
	return err
}
