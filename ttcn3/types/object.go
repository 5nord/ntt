package types

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

type Object interface {
	Name() string    // module local object name
	Type() Type      // object type
	Pos() syntax.Pos // Position of object identifier
}
