package types

import (
	"github.com/nokia/ntt/ttcn3/syntax"
)

// An Object describes a named language entity, such as consts or functions
type Object interface {
	Parent() *Scope
	Name() string
	Pos() syntax.Pos
	Type() Type
}

// An object implements common parts of an Object
type object struct {
	parent *Scope
	pos    syntax.Pos
	name   string
	typ    Type
}

func (obj *object) Parent() *Scope {
	return obj.parent
}

func (obj *object) Pos() syntax.Pos {
	return obj.pos
}

func (obj *object) Name() string {
	return obj.name
}

func (obj *object) Type() Type {
	return obj.typ
}
