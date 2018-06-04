package types

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Module struct {
	name    string
	scope   *Scope
	imports []*Module
}

func (m *Module) Name() string {
	return m.name
}

func NewModule(name string) *Module {
	scope := NewScope(Universe, syntax.NoPos, syntax.NoPos)
	return &Module{name: name, scope: scope}
}
