package types

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Scope struct {
	parent   *Scope
	children []*Scope
	elems    map[string]Object
	pos, end syntax.Pos
}

func (s *Scope) Names() []string {
	return nil
}

func (s *Scope) Lookup(name string) Object {
	return nil
}

// NewScope returns a new, empty scope contained in the given parent
// scope, if any.
func NewScope(parent *Scope, pos, end syntax.Pos) *Scope {
	s := &Scope{parent: parent, pos: pos, end: end}

	return s
}
