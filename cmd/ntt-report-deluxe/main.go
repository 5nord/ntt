package main

import (
	"bufio"
	"fmt"
	"html/template"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
	"time"

	errors "golang.org/x/xerrors"
)

type Report struct {
	Name    string
	Timeout float64
	Mpars   []string

	tcst, tcfi time.Time
	Verdict    string
	Reason     string
}

var (
	count  = make(map[string]int)
	line   = 0
	report Report
	page   = ` <!DOCTYPE html>
<html>
<header><title>{{.Name}}</title></header>
<body>
<h1>{{.Name}}</h1>
<ul>
<li>Verdict: {{ .Verdict }}{{ if .Reason  }} ({{.Reason}}){{end}}</li>
</body></html>
`
)

func main() {

	r := bufio.NewReader(os.Stdin)

	var (
		text string
		err  error
	)
L:
	for {
		line++

		text, err = r.ReadString('\n')
		text = strings.TrimSuffix(text, "\n")
		if err != nil {
			break
		}

		e, err := NewEvent(text)
		if err != nil {
			log.Println(err.Error())
			continue
		}

		switch e.ID() {
		case "mpar":
			report.Mpars = append(report.Mpars, fmt.Sprintf("%s := %s", e.Field(3), e.Field(4)))

		case "tcst":
			if report.Name != "" {
				err = errors.Errorf("multple tests in one log file")
				break L
			}
			report.Name = e.Field(3)
			report.Timeout, _ = strconv.ParseFloat(e.Field(4), 64)
			report.tcst, _ = e.Stamp()

		case "tcfi":
			report.Verdict = e.Field(4)
			report.tcfi, _ = e.Stamp()

		case "setv":
			s := e.Field(5)
			if s != "" {
				report.Reason = s
			}

		}
	}

	if err != io.EOF {
		log.Println(err)
	}

	t := template.Must(template.New("todos").Parse(page))
	err = t.Execute(os.Stdout, report)
	if err != nil {
		log.Println(err)
	}
}
