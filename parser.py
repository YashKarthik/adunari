import re
from typing import Literal

class AssemblyParser:
    def __init__(self, input_file: str):
        self.input_file: str = input_file
        self.current_instr_idx: int = -1
        self.current_instr: str | None = None
        self.instructions: list[str] = []

        with open(input_file) as f:
            for instr in f:
                if instr[:2] == "//":
                    continue

                instr = instr.replace(" ", "").replace("\n", "").replace("\t", "")
                if instr == "":
                    continue

                self.instructions.append(instr)

    def has_more_instr(self) -> bool:
        return True if (self.current_instr_idx + 1) < len(self.instructions) else False

    def next_instr(self):
        if (not self.has_more_instr()):
            raise IndexError("Reached end of instruction list.")

        self.current_instr_idx += 1
        self.current_instr = self.instructions[self.current_instr_idx];

    def curr_instr_type(self) -> Literal["A", "C", "L"]:
        if (not self.current_instr):
            raise ValueError("Current instruction not loaded.")

        if self.current_instr[0] == "@":
            return "A";
        elif self.current_instr[0] == "(": #)
            return "L"
        return "C"

    def get_symbol_value(self) -> int:
        if not self.current_instr:
            raise ValueError("Current instruction not loaded.")

        if self.curr_instr_type() == "A":
            return int(self.current_instr[1:])
        elif self.curr_instr_type() == "L":
            return int(re.findall(r'\d+', self.current_instr)[0])

        raise ValueError("Current instruction of type C, expected A or L")

    def get_dest(self):
        if not self.current_instr:
            raise ValueError("Current instruction not loaded.")
        if not self.curr_instr_type() == "C":
            raise ValueError("Destination does not exist for non-C instructions.")

        eq_idx = self.current_instr.find("=")
        return self.current_instr[:eq_idx] if eq_idx > 0 else None

    def get_comp(self):
        if not self.current_instr:
            raise ValueError("Current instruction not loaded.")
        if not self.curr_instr_type() == "C":
            raise ValueError("Comp does not exist for non-C instructions.")

        eq_idx = self.current_instr.find("=")
        colon_idx = self.current_instr.find(";")
        return self.current_instr[max(0, eq_idx+1): colon_idx if colon_idx != -1 else None]

    def get_jump(self):
        if not self.current_instr:
            raise ValueError("Current instruction not loaded.")
        if not self.curr_instr_type() == "C":
            raise ValueError("Jump does not exist for non-C instructions.")

        colon_idx = self.current_instr.find(";")
        return self.current_instr[colon_idx+1:] if colon_idx > 0 else None
