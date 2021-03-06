package t3xf

import (
	"bytes"
	"io"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRead(t *testing.T) {

	t.Run("empty file", func(t *testing.T) {
		f, err := read(bytes.NewReader([]byte{}))
		assert.Nil(t, f)
		assert.Equal(t, ErrUnknownFormat, err)
	})

	t.Run("t3xf magic", func(t *testing.T) {
		f, err := read(bytes.NewReader([]byte{
			0x03, 0x00, 0x00, 0x13, // NOP
			0x43, 0x01, 0x00, 0x00, // NATLONG
			0x02, 0x00, 0x00, 0x00, // 2
			0x33, 0x00, 0x00, 0x00, // VERSION
		}))
		assert.NotNil(t, f)
		assert.Nil(t, err)
	})

	t.Run("tasm magic", func(t *testing.T) {
		f, err := read(bytes.NewReader([]byte{
			0x54, 0x33, 0x58, 0x46, 0x41, 0x53, 0x4d, 0x00, // T3XFASM\0
		}))
		assert.Nil(t, f)
		assert.Equal(t, io.EOF, err)
	})

	t.Run("tasm incomplete", func(t *testing.T) {
		f, err := read(bytes.NewReader([]byte{
			0x54, 0x33, 0x58, 0x46, 0x41, 0x53, 0x4d, 0x00, // T3XFASM\0
			0x00, 0x00, 0x00,
		}))
		assert.Nil(t, f)
		assert.Equal(t, io.ErrUnexpectedEOF, err)
	})

	t.Run("tasm empty", func(t *testing.T) {
		f, err := read(bytes.NewReader([]byte{
			0x54, 0x33, 0x58, 0x46, 0x41, 0x53, 0x4d, 0x00, // T3XFASM\0

			// TASM Header
			0x00, 0x00, 0x00, 0x00, // length t3xfSection
			0x00, 0x00, 0x00, 0x00, // length textSection
			0x00, 0x00, 0x00, 0x00, // length int32Table
			0x00, 0x00, 0x00, 0x00, // length nameTable
			0x00, 0x00, 0x00, 0x00, // length moduleTable
			0x00, 0x00, 0x00, 0x00, // length typeAliasTable
			0x00, 0x00, 0x00, 0x00, // length recordTypeTable
			0x00, 0x00, 0x00, 0x00, // length setTypeTable
			0x00, 0x00, 0x00, 0x00, // length recordOfTypeTable
			0x00, 0x00, 0x00, 0x00, // length setOfTypeTable
			0x00, 0x00, 0x00, 0x00, // length unionTypeTable
			0x00, 0x00, 0x00, 0x00, // length enumeratedTypeTable
			0x00, 0x00, 0x00, 0x00, // length arrayTypeTable
			0x00, 0x00, 0x00, 0x00, // length closureTypeTable
			0x00, 0x00, 0x00, 0x00, // length messagePortTypeTable
			0x00, 0x00, 0x00, 0x00, // length componentTypeTable
			0x00, 0x00, 0x00, 0x00, // length constTable
			0x00, 0x00, 0x00, 0x00, // length moduleParTable
			0x00, 0x00, 0x00, 0x00, // length templateTable
			0x00, 0x00, 0x00, 0x00, // length testcaseTable
			0x00, 0x00, 0x00, 0x00, // length functionTable
			0x00, 0x00, 0x00, 0x00, // length extFunctionTable
			0x00, 0x00, 0x00, 0x00, // length altstepTable
			0x00, 0x00, 0x00, 0x00, // length blockTable
			0x00, 0x00, 0x00, 0x00, // length controlTable
			0x00, 0x00, 0x00, 0x00, // length stringTable
			0x00, 0x00, 0x00, 0x00, // length collectionTable
			0x00, 0x00, 0x00, 0x00, // length dataSection

			// Random trailing data is permitted.
			0x01, 0x02, 0x03,
		}))
		assert.NotNil(t, f)
		assert.Nil(t, err)
	})
}
