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

    def jump(self, mnemonic: str) -> int:
        return 0b10
