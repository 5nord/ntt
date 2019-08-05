package printer

import (
	"strings"
	"testing"

	"github.com/nokia/ntt/internal/loc"
	"github.com/nokia/ntt/internal/ttcn3/ast"
	"github.com/nokia/ntt/internal/ttcn3/parser"
	"github.com/stretchr/testify/assert"
)

// The formatted result mus look the same as the input for successful tests.
var tests = []string{
	"integer",
	"universal charstring",
}

func TestPartial(t *testing.T) {
	for _, src := range tests {
		actual := prettyPrint(src)
		assert.Equal(t, src, actual)
	}
}

func prettyPrint(s string) string {
	return print(parse(s))
}

func parse(s string) ast.Node {
	root, err := parser.Parse(loc.NewFileSet(), "<string>", s, 0, nil)
	if err != nil {
		panic(err.Error())
	}

	if len(root) != 1 {
		panic("unexpected length")
	}

	return root[0]
}

func print(n ast.Node) string {
	var b strings.Builder
	p := New(&b)
	p.Print(n)
	return b.String()
}
