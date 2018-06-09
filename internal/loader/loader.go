package loader

import (
	"fmt"
	"github.com/nokia/ntt/ttcn3/syntax"
	"github.com/nokia/ntt/ttcn3/types"
	"os"
)

func LoadFromFiles(files []string) ([]*types.Module, error) {
	fset := syntax.NewFileSet()
	list, err := parseFiles(fset, files)
	if err != nil {
		return nil, err
	}

	var modules []*types.Module

	conf := types.Config{
		Error: func(err types.Error) {
			fmt.Fprintln(os.Stderr, "\x1b[32m", err, "\x1b[0m")
		},
	}

	for _, ast := range list {
		m, err := conf.Check(fset, ast, nil)
		if err != nil {
			return nil, err
		}
		modules = append(modules, m)
	}

	return modules, nil
}
