class AsmTranslator:
    dest_bit = {
        "A": 0b100,
        "M": 0b001,
        "D": 0b010
    }
    def dest(self, mnemonic: str | None) -> int:
        ret = 0b000
        if mnemonic == None:
            return ret;

        for m in mnemonic:
            ret = self.dest_bit[m] | ret
        return ret;

    jump_bits = {
        None: 0b000,
        "JGT": 0b001,
        "JEQ": 0b010,
        "JGE": 0b011,
        "JLT": 0b100,
        "JNE": 0b101,
        "JLE": 0b110,
        "JMP": 0b111
    }
    def jump(self, mnemonic: str | None) -> int:
        return self.jump_bits[mnemonic]

    comp_table = {
        "0":   0b0101010,
        "1":   0b0111111,
        "-1":  0b0111010,
        "D":   0b0001100,
        "A":   0b0110000,
        "M":   0b1110000,
        "!D":  0b0001101,
        "!A":  0b0110001,
        "!M":  0b1110001,
        "-D":  0b0001111,
        "-A":  0b0110011,
        "-M":  0b1110011,
        "D+1": 0b0011111,
        "A+1": 0b0110111,
        "M+1": 0b1110111,
        "D-1": 0b0001110,
        "A-1": 0b0110010,
        "M-1": 0b1110010,
        "D+A": 0b0000010,
        "D+M": 0b1000010,
        "D-A": 0b0010011,
        "D-M": 0b1010011,
        "A-D": 0b0000111,
        "M-D": 0b1000111,
        "D&A": 0b0000000,
        "D&M": 0b1000000,
        "D|A": 0b0010101,
        "D|M": 0b1010101
    }

    def comp(self, mnemonic: str) -> int:
        return self.comp_table[mnemonic]

