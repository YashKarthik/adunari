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

    def comp(self, mnemonic: str) -> int:
        return 0b10

    jump_bits = {
        None: 0b00,
        "JGT": 0b001,
        "JEQ": 0b010,
        "JGE": 0b011,
        "JLT": 0b100,
        "JNE": 0b101,
        "JLE": 0b110,
        "JMP": 0b111
    }
    def jump(self, mnemonic: str) -> int:
        return self.jump_bits[mnemonic]
