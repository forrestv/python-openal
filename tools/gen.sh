#!/bin/sh
{ cat _$1.start ; python conv.py _$1.proto $1; } | grep -v GetError.errcheck
