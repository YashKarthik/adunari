from assembler import HackAssembler

assembler = HackAssembler("../nand2tetris/projects/6/rect/Pong.asm")
assembler.generate_symbol_table()
assembler.generate_machine_code()
assembler.write_machine_code("./pong.hack")
