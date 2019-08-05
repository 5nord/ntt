package printer

import (
	"fmt"
	"io"
	"reflect"

	"github.com/nokia/ntt/internal/ttcn3/ast"
)

type whiteSpace string

const (
	ignore   = whiteSpace(0)
	blank    = whiteSpace(' ')
	sp       = whiteSpace(' ')
	tab      = whiteSpace('\t')
	nl       = whiteSpace('\n')
	indent   = whiteSpace('>')
	unindent = whiteSpace('<')
)

type printer struct {
	w              io.Writer
	indent         int
	indentRequired bool
}

func New(w io.Writer) *printer {
	return &printer{w: w}
}

func (p *printer) Print(n ast.Node) {
	if reflect.ValueOf(n).IsNil() {
		return
	}

	switch x := n.(type) {
	case *ast.Module:
		p.print(x.Tok, x.Name, x.Language, x.LBrace, nl)
		p.print(indent)
		p.printModuleDefs(x.Defs)
		p.print(unindent)
		p.print(x.RBrace)
		p.print(x.With)

	case *ast.ModuleDef:
		p.print(x.Visibility, x.Def)

	case *ast.ValueDecl:
		p.print(x.Kind, x.TemplateRestriction, x.Modif, x.Type)
		p.printExprs(x.Decls)
		p.print(x.With)

	case *ast.TemplateDecl:
		p.print(x.TemplateTok, x.LParen, x.Tok, x.RParen, x.Modif)
		p.print(x.Type, x.Name, x.TypePars, x.Params)
		if x.ModifiesTok.IsValid() {
			p.print(x.ModifiesTok, x.Base, x.AssignTok)
		}
		p.print(x.Value)
		p.print(x.With)

	//case *ast.ModuleParameterGroup:
	//case *ast.FuncDecl:
	//case *ast.SignatureDecl:
	//case *ast.SubTypeDecl:
	//case *ast.StructTypeDecl:
	//case *ast.EnumTypeDecl:
	//case *ast.BehaviourTypeDecl:
	//case *ast.PortTypeDecl:
	//case *ast.PortAttribute:
	//case *ast.PortMapAttribute:
	//case *ast.ComponentTypeDecl:

	//case *ast.BlockStmt:
	//case *ast.DeclStmt:
	//case *ast.ExprStmt:
	//case *ast.BranchStmt:
	//case *ast.ReturnStmt:
	//case *ast.AltStmt:
	//case *ast.CallStmt:
	//case *ast.ForStmt:
	//case *ast.WhileStmt:
	//case *ast.DoWhileStmt:
	//case *ast.IfStmt:
	//case *ast.SelectStmt:

	//case *ast.ControlPart:
	//case *ast.ImportDecl:
	//case *ast.GroupDecl:
	//case *ast.FriendDecl:
	//case *ast.FormalPars:
	//case *ast.FormalPar:
	//case *ast.WithStmt:
	//case *ast.WithSpec:
	//case *ast.CaseClause:
	//case *ast.CommClause:
	//case *ast.LanguageSpec:
	//case *ast.RestrictionSpec:
	//case *ast.RunsOnSpec:
	//case *ast.SystemSpec:
	//case *ast.MtcSpec:
	//case *ast.ReturnSpec:
	//case *ast.Field:
	//case *ast.RefSpec:
	//case *ast.StructSpec:
	//case *ast.ListSpec:
	//case *ast.EnumSpec:
	//case *ast.BehaviourSpec:
	default:
		panic(fmt.Errorf("unexpected ast.Node type: %T", n))
	}
}

func (p *printer) printModuleDefs(defs []*ast.ModuleDef) {
	for i := range defs {
		if defs[i] != nil {
			p.print(defs[i], nl)
		}
	}
}

func (p *printer) printStmts(stmts []ast.Stmt) {
	for i := range stmts {
		if stmts[i] != nil {
			p.print(stmts[i], nl)
		}
	}
}

func (p *printer) printExprs(exprs []ast.Expr) {
	for i := range exprs {
		if exprs[i] != nil {
			p.print(exprs[i])
		}
	}
}

func (p *printer) printExpr(x ast.Expr) {

	switch x := x.(type) {
	case *ast.Ident:
		p.print(x.Tok, x.Tok2)

	case *ast.ParametrizedIdent:
		p.print(x.Ident, x.Params)

	case *ast.ValueLiteral:
		p.print(x.Tok)

	case *ast.CompositeLiteral:
		p.print(x.LBrace)
		p.printExprs(x.List)
		p.print(x.RBrace)

	case *ast.UnaryExpr:
		p.print(x.Op, x.X)

	case *ast.BinaryExpr:
		p.print(x.X, x.Op, x.X)

	case *ast.ParenExpr:
		p.print(x.LParen)
		p.printExprs(x.List)
		p.print(x.RParen)

	case *ast.SelectorExpr:
		p.print(x.X, x.Dot, x.Sel)

	case *ast.IndexExpr:
		p.print(x.X, x.LBrack, x.Index, x.RBrack)

	case *ast.CallExpr:
		p.print(x.Fun, x.Args)

	case *ast.LengthExpr:
		p.print(x.X, x.Len, x.Size)

	case *ast.ValueExpr:
		p.print(x.X, x.Tok, x.Y)

	case *ast.ParamExpr:
		p.print(x.X, x.Tok, x.Y)

	case *ast.FromExpr:
		p.print(x.Kind, x.FromTok, x.X)

	case *ast.ModifiesExpr:
		p.print(x.Tok, x.X, x.Assign, x.Y)

	case *ast.RegexpExpr:
		p.print(x.Tok, x.NoCase, x.X)

	case *ast.PatternExpr:
		p.print(x.Tok, x.NoCase, x.X)

	//case *ast.RedirectExpr:
	//case *ast.DecmatchExpr:
	//case *ast.DecodedExpr:
	//case *ast.DefKindExpr:
	//case *ast.ExceptExpr:
	default:
		panic(fmt.Errorf("unexpected ast.Node type: %T", x))
	}
}

func (p *printer) printWhiteSpace(ws whiteSpace) {
	switch ws {
	case indent:
		p.indent++
	case unindent:
		p.indent--
	case nl:
		p.indentRequired = true
		fallthrough
	default:
		fmt.Fprint(p.w, ws)
	}
}

func (p *printer) printToken(tok ast.Token) {
	if tok.IsValid() {
		p.print(tok.String())
	}
}

func (p *printer) print(args ...interface{}) {
	for _, arg := range args {

		if p.indentRequired {
			p.indentRequired = false
			p.printIndent()
		}

		switch x := arg.(type) {
		case whiteSpace:
			p.printWhiteSpace(x)
		case ast.Token:
			p.printToken(x)
		case ast.Node:
			p.Print(x)
		default:
			fmt.Fprint(p.w, arg)
		}
	}
}

func (p *printer) printIndent() {
	for i := p.indent; i > 0; i-- {
		fmt.Fprint(p.w, tab)
	}
}
