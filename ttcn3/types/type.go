package types

type Type interface {
	Underlying() Type
	String() string
}

type BasicKind int

const (
	Invalid BasicKind = iota
	Bool
	Int
)

type Basic struct {
	kind BasicKind
}
