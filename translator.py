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

    """
        [ ] c6
    """
    def comp(self, mnemonic: str) -> int:
        ret = 0b0000000
        if mnemonic.find("M") != -1:
            ret = ret | 0b1000000 # a

        if mnemonic.find("D") == -1:
            ret = ret | 0b0100000 # c1

        if mnemonic.find("0") == -1 and (mnemonic.find("D") == -1 or (mnemonic.find("D") != -1 and mnemonic.find("+") and mnemonic.find("1")) or mnemonic.find("D-A") or mnemonic.find("D|A")):
            ret = ret | 0b0010000 # c2

        if mnemonic.find("A") == -1 and mnemonic.find("M") == -1:
            ret = ret | 0b0001000 # c3

        if mnemonic.find("0") == -1 and mnemonic.find("-1") == -1 and (mnemonic.find("A") == -1 or (mnemonic.find("A") != -1 and mnemonic.find("+") and mnemonic.find("1")) or mnemonic.find("A-D") or mnemonic.find("D|A")):
            ret = ret | 0b0000100 # c4

        if mnemonic.find("1") or mnemonic.find("0") or mnemonic.find("+") or mnemonic.find("-"):
            ret = ret | 0b0000010 # c5

        return ret

