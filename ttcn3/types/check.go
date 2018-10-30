package types

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Config struct{}

type Checker struct {
	mod *syntax.Module
}

func (check *Checker) checkModule(mod *syntax.Module) (err error) {
	check.collectObjects()
	return nil
}

func (check *Checker) collectObjects() {

}
