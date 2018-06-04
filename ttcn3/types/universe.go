package types

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

var Universe *Scope

func init() {
	Universe = NewScope(nil, syntax.NoPos, syntax.NoPos)
}
