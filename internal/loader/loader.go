package loader

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Config struct {
	Files   []string
	Modules []*syntax.Module

	fset *syntax.FileSet
}

func (c *Config) parseFiles() error {
	c.fset = syntax.NewFileSet()

	for _, f := range c.Files {
		m, err := syntax.ParseModules(c.fset, f, nil, 0, nil)
		if err != nil {
			return err
		}
		c.Modules = append(c.Modules, m...)
	}

	return nil
}

func LoadFromFiles(files []string) error {
    c := &Config{Files: files}
    return c.parseFiles()
}

