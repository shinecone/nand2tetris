"""
  Useage :  
    prompt> ./HackAssembler.py xxx.asm
    
  Output :
    ./ xxx.hack
"""

import sys
import Parser, Code, SymbolTable


def main():
  # Input file
  asmfile = sys.argv[1]
  # Output file
  hackfile = asmfile[:-3] + 'hack'
  
  # Create an instance
  symbolTable = SymbolTable.SymbolTable()
  parser = Parser.Parser(asmfile)
  
  # Save variables
  symbol_address = 0
  while parser.hasMoreLines():
    # Gets the next instruction and makes it the current instruction(string)
    parser.advance()
    
    if parser.instructionType() == 'L_INSTRUCTION':
      if not symbolTable.contains(parser.symbol()):
        symbolTable.addEntry(parser.symbol(), symbol_address)
    elif parser.instructionType() in ['A_INSTRUCTION', 'C_INSTRUCTION']:
      symbol_address += 1
        
  parser.reset()
  # Open the output file
  hackf = open(hackfile, 'w')
  new_symbol_address = 16
  
  # Convert to binary code
  while parser.hasMoreLines():
    # Gets the next instruction and makes it the current instruction(string)
    parser.advance()
    
    # Convert to binary code per instance type
    if parser.instructionType() == 'A_INSTRUCTION':
      if parser.symbol()[0].isdigit():
        # if @xxx where xxx is a decimal number
        hackf.write(f'0{int(parser.symbol()):015b}\n')
      else:
        # if @xxx where xxx is a syambol
        if not symbolTable.contains(parser.symbol()):
          # If the symbol is not in the symbol table
          symbolTable.addEntry(parser.symbol(), new_symbol_address)
          new_symbol_address += 1
        # If the symbol is in the symbol table
        hackf.write(f'0{symbolTable.getAddress(parser.symbol()):015b}\n')
    elif parser.instructionType() == 'C_INSTRUCTION':
      hackf.write(f'111{Code.comp(parser.comp())}'+ f'{Code.dest(parser.dest())}{Code.jump(parser.jump())}\n')
    elif parser.instructionType() == 'L_INSTRUCTION':
      pass
  
  hackf.close()

if __name__ == '__main__':
  main()
