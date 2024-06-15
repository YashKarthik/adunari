from assembler import HackAssembler

assembler = HackAssembler("../nand2tetris/projects/6/rect/RectL.asm")
assembler.generate_machine_code()
assembler.write_machine_code("./rectL.hack")
