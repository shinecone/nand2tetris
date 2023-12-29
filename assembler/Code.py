# Returns the binary representation of the parsed dest field (string)
def dest(mnemonic):
  dest_dict = {
    #'null': '000',
    'M'  : '001',
    'D'  : '010',
    'DM' : '011',
    'A'  : '100',
    'AM' : '101',
    'AD' : '110',
    'ADM': '111',
  }
  if mnemonic in dest_dict:
    return dest_dict[mnemonic]
  else:
    return '000'

# Returns the binary representation of the parsed comp field (string)
def comp(mnemonic):
  comp_dict = {
    '0': '101010',
    '1': '111111',
    '-1': '111010',
    'D': '001100',
    'A': '110000',
    '!D': '001101',
    '!A': '110001',
    '-D': '001111',
    '-A': '110011',
    'D+1': '011111',
    'A+1': '110111',
    'D-1': '001110',
    'A-1': '110010',
    'D+A': '000010',
    'D-A': '010011',
    'A-D': '000111',
    'D&A': '000000',
    'D|A': '010101',
  }
  
  a_bit = '0'
  if 'M' in mnemonic:
    a_bit = '1'
    mnemonic = mnemonic.replace('M','A')
  
  if mnemonic in comp_dict:
    return a_bit + comp_dict[mnemonic]
  else:
    return '0101010'
  
# Returns the binary representation of the parsed jump field (string)
def jump(mnemonic):
  jump_dict = {
    #'null': '000',
    'JGT' : '001',
    'JEQ' : '010',
    'JGE' : '011',
    'JLT' : '100',
    'JNE' : '101',
    'JLE' : '110',
    'JMP' : '111',
  }
  
  if mnemonic in jump_dict:
    return jump_dict[mnemonic]
  else:
    return '000'
  
