package types

import (
	"fmt"
	"github.com/nokia/ntt/ttcn3/syntax"
)

func (check *Checker) sprintf(format string, args ...interface{}) string {
	for i, arg := range args {
		switch a := arg.(type) {
		case nil:
			arg = "<nil>"
			//case operand:
			//        panic("internal error: should always pass *operand")
			//case *operand:
			//        arg = operandString(a, check.qualifier)
		case syntax.Pos:
			arg = check.fset.Position(a).String()
			//case syntax.Expr:
			//        arg = ExprString(a)
			//case Object:
			//        arg = ObjectString(a, check.qualifier)
			//case Type:
			//        arg = TypeString(a, check.qualifier)
		}
		args[i] = arg
	}
	return fmt.Sprintf(format, args...)
}

func (check *Checker) err(pos syntax.Pos, msg string, soft bool) {
	err := Error{check.fset, pos, msg, soft}
	f := check.conf.Error
	if f == nil {
		panic(bailout{})
	}
	f(err)
}

func (check *Checker) error(pos syntax.Pos, msg string) {
	check.err(pos, msg, false)
}

func (check *Checker) errorf(pos syntax.Pos, format string, args ...interface{}) {
	check.err(pos, check.sprintf(format, args...), false)
}

func (check *Checker) invalidAST(pos syntax.Pos, format string, args ...interface{}) {
	check.errorf(pos, "invalid AST: "+format, args...)
}
