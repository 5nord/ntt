package loader

import (
	"github.com/nokia/ntt/ttcn3/syntax"
	"github.com/nokia/ntt/ttcn3/types"
)

func LoadFromFiles(files []string) ([]*types.Module, error) {
	fset := syntax.NewFileSet()
	list, err := parseFiles(fset, files)
	if err != nil {
		return nil, err
	}

	var modules []*types.Module

	var conf types.Config
	for _, ast := range list {
		m, err := conf.Check(fset, ast, nil)
		if err != nil {
			return nil, err
		}
		modules = append(modules, m)
	}

	return modules, nil
}
