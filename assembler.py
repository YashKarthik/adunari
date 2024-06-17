import re
from parser import AssemblyParser
from translator import AsmTranslator
from symbol_table import SymbolTable

class HackAssembler:
    def __init__(self, input_file: str) -> None:
        self.machine_code: list[str] = []
        self.current_symbol_idx: int = 0
        self.symbol_table = SymbolTable()
        self.translator = AsmTranslator()
        self.parser = AssemblyParser(input_file)

    def generate_symbol_table(self):
        while self.parser.has_more_instr():

            self.parser.next_instr()
            if self.parser.curr_instr_type() != "L":
                self.current_symbol_idx += 1
                continue

            self.symbol_table.add_symbol(self.parser.get_symbol_value(), self.current_symbol_idx)
        self.parser.current_instr_idx = -1

    def generate_machine_code(self):
        while self.parser.has_more_instr():

            self.parser.next_instr()
            if self.parser.curr_instr_type() == "A":
                symbol = self.parser.get_symbol_value()
                if len(re.findall("\\d", symbol[0])) > 0:
                    val = int(symbol)
                else:
                    if not self.symbol_table.contains(symbol):
                        self.symbol_table.add_symbol(symbol, self.symbol_table.free_address)
                        print("Appending", symbol, " to ", self.symbol_table.free_address)
                        self.symbol_table.free_address += 1
                    val = self.symbol_table.get_address(symbol)

                val_string = "0{0:015b}".format(val)
                self.machine_code.append(val_string)
                continue

            if self.parser.curr_instr_type() == "L":
                continue
            comp = "111{0:07b}".format(self.translator.comp(self.parser.get_comp()))
            dest = "{0:03b}".format(self.translator.dest(self.parser.get_dest()))
            jump = "{0:03b}".format(self.translator.jump(self.parser.get_jump()))
            self.machine_code.append(comp + dest + jump)

    def write_machine_code(self, output_file: str|None = None) -> None:
        code_str = "\n".join(self.machine_code)
        if output_file == None:
            print(code_str)
            return

        with open(output_file, "w") as out:
            out.write(code_str)
