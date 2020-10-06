package main

import (
	"strings"
	"time"

	errors "golang.org/x/xerrors"
)

type Event struct {
	Category
	fields []string
}

func NewEvent(s string) (Event, error) {
	var e Event

	e.fields = strings.Split(s, "|")
	id := e.Field(1)
	if len(id) < 4 {
		return e, errors.Errorf("unknown event %q", id)
	}
	id = id[:4]

	c, ok := tokens[id]
	if !ok {
		return e, errors.Errorf("unknown event %q", id)
	}

	e.Category = c
	return e, nil
}

func (e Event) Stamp() (time.Time, error) {
	return time.Parse("20060102T150405.999999", e.Field(0))
}

func (e Event) Component() string {
	c := strings.SplitN(e.Field(2), "=", 2)
	if len(c) > 0 {
		return c[0]
	}
	return ""
}

func (e Event) Source() string {
	c := strings.SplitN(e.Field(2), "=", 2)
	if len(c) == 2 {
		return c[1]
	}
	return ""
}

func (e Event) Field(i int) string {
	if i < len(e.fields) {
		return e.fields[i]
	}
	return ""
}

var (
	tokens = map[string]Category{
		"ACDC": ErrACDC,
		"ARGI": ErrARGI,
		"ARGS": ErrARGS,
		"ARRV": ErrARRV,
		"ARTE": ErrARTE,
		"ARUN": ErrARUN,
		"BREF": ErrBREF,
		"CONE": ErrCONE,
		"CONV": ErrCONV,
		"DEAD": ErrDEAD,
		"DIRE": ErrDIRE,
		"DIV0": ErrDIV0,
		"DOME": ErrDOME,
		"DTDE": ErrDTDE,
		"FILE": ErrFILE,
		"FLOW": ErrFLOW,
		"FOEX": ErrFOEX,
		"ICST": ErrICST,
		"IGRP": ErrIGRP,
		"INOP": ErrINOP,
		"LENE": ErrLENE,
		"LIDE": ErrLIDE,
		"LKUP": ErrLKUP,
		"MALF": ErrMALF,
		"MANY": ErrMANY,
		"MAPE": ErrMAPE,
		"NAME": ErrNAME,
		"NOIM": ErrNOIM,
		"NRTE": ErrNRTE,
		"NSPR": ErrNSPR,
		"NULL": ErrNULL,
		"OMIT": ErrOMIT,
		"OPTM": ErrOPTM,
		"OPTS": ErrOPTS,
		"OPTU": ErrOPTU,
		"OSUF": ErrOSUF,
		"PABV": ErrPABV,
		"PAOV": ErrPAOV,
		"PARE": ErrPARE,
		"PATE": ErrPATE,
		"PLEX": ErrPLEX,
		"PLOD": ErrPLOD,
		"PTFA": ErrPTFA,
		"RNGE": ErrRNGE,
		"SIZE": ErrSIZE,
		"SNAC": ErrSNAC,
		"SNAP": ErrSNAP,
		"SRUN": ErrSRUN,
		"SYSE": ErrSYSE,
		"TCIM": ErrTCIM,
		"TIME": ErrTIME,
		"TSTP": ErrTSTP,
		"TYPE": ErrTYPE,
		"UBLK": ErrUBLK,
		"UNAS": ErrUNAS,
		"UNDF": ErrUNDF,
		"UNOP": ErrUNOP,
		"UTF8": ErrUTF8,
		"UTOB": ErrUTOB,
		"VRSN": ErrVRSN,
		"WAIT": ErrWAIT,
		"WCPA": ErrWCPA,
		"WIDE": ErrWIDE,
		"WPAC": ErrWPAC,
		"acfg": ACFG,
		"alen": ALEN,
		"allv": ALLV,
		"alrp": ALRP,
		"alwt": ALWT,
		"asen": ASEN,
		"aslv": ASLV,
		"bctr": BCTR,
		"coal": COAL,
		"cocr": COCR,
		"codo": CODO,
		"cofi": COFI,
		"cokd": COKD,
		"coki": COKI,
		"coru": CORU,
		"cosp": COSP,
		"cost": COST,
		"cpen": CPEN,
		"cplv": CPLV,
		"dbg1": DBG1,
		"dbg2": DBG2,
		"dbg3": DBG3,
		"dbug": DBUG,
		"deco": DECO,
		"decv": DECV,
		"dtac": DTAC,
		"dtde": DTDE,
		"dten": DTEN,
		"dtlv": DTLV,
		"dump": DUMP,
		"else": ELSE,
		"enco": ENCO,
		"fnen": FNEN,
		"fnlv": FNLV,
		"fxen": FXEN,
		"fxlv": FXLV,
		"getv": GETV,
		"ilen": ILEN,
		"illv": ILLV,
		"matc": MATC,
		"mpar": MPAR,
		"paon": PAON,
		"pllg": PLLG,
		"plod": PLOD,
		"ptck": PTCK,
		"ptcl": PTCL,
		"ptcn": PTCN,
		"ptdi": PTDI,
		"ptds": PTDS,
		"ptha": PTHA,
		"ptmp": PTMP,
		"ptpu": PTPU,
		"ptqu": PTQU,
		"ptrx": PTRX,
		"ptsd": PTSD,
		"ptsp": PTSP,
		"ptst": PTST,
		"pttr": PTTR,
		"ptun": PTUN,
		"rvon": RVON,
		"sdbg": SDBG,
		"setv": SETV,
		"tcen": TCEN,
		"tcfi": TCFI,
		"tclv": TCLV,
		"tcst": TCST,
		"tmrd": TMRD,
		"tmru": TMRU,
		"tmsp": TMSP,
		"tmst": TMST,
		"tmto": TMTO,
		"uact": UACT,
		"ulog": ULOG,
		"vach": VACH,
		"vrsn": VRSN,
		"wait": WAIT,
	}
)
