package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/nokia/ntt/internal/loader"

	"github.com/spf13/cobra"
)

var (
	formatCmd = &cobra.Command{
		Use:   "format [files...]",
		Short: "format ttcn3 files",
		Long:  `Format ttcn3 files.`,

		RunE: format,
	}

	w = bufio.NewWriter(os.Stdout)
)

func init() {
	rootCmd.AddCommand(formatCmd)
}

func list(cmd *cobra.Command, args []string) error {
	suite, err := loader.NewFromArgs(args)
	if err != nil {
		fmt.Fprintln(os.Stderr, err.Error())
		os.Exit(1)
	}

	if err := suite.Load(); err != nil {
		fmt.Fprintln(os.Stderr, err.Error())
		os.Exit(1)
	}

	for _, mod := range suite.Modules {
		var file string
		if Verbose {
			file = suite.Fset.File(mod.Pos()).Name()
		}
		printer(file, mod, mod)
	}
	w.Flush()

	return nil
}
