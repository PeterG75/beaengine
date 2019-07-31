#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *


class TestSuite:

    def test(self):

        # VEX.L0.66.0F3A.W1 30 /r
        # KSHIFTRW k1, k2, imm8

        myVEX = VEX('VEX.L0.66.0F3A.W1')
        myVEX.R = 1
        Buffer = '{}30c911'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x30)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kshiftrw ')
        assert_equal(myDisasm.instr.repr, 'kshiftrw k1, k1, 11h')

        # VEX.L0.66.0F3A.W0 30 /r
        # KSHIFTRB k1, k2, imm8

        myVEX = VEX('VEX.L0.66.0F3A.W0')
        myVEX.R = 1
        Buffer = '{}30e011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x30)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kshiftrb ')
        assert_equal(myDisasm.instr.repr, 'kshiftrb k4, k0, 11h')
