// Copyright 2019 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the NOTICE file.

// Package unit holds the definitions for the units you can use in telemetry.
package unit

// Unit is used to specify the units for a given measure.
// This is can used for display purposes.
type Unit string

const (
	// Dimensionless indicates that a measure has no specified units.
	Dimensionless = "1"
	// Bytes indicates that that a measure is recording number of bytes.
	Bytes = "By"
	// Milliseconds indicates that a measure is recording a duration in milliseconds.
	Milliseconds = "ms"
)
