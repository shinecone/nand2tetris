class Parser:
  # Creates a Parser and opens the source text file
  def __init__(self, asmfile):
    with open(asmfile, 'r') as self.asmf:
      self.commands = self.asmf.readlines()
      self.count = 0
      self.curent_command = None
  
  # Checks if there is more work to do (boolean)
  def hasMoreLines(self):
    if self.count < len(self.commands):
      return True
    else:
      return False

  # Gets the next instruction and makes it the current instruction(string)
  def advance(self):
    while self.commands[self.count] == '\n' or self.commands[self.count][0:2] == '//':
      self.count += 1
    
    command = self.commands[self.count].strip()
    self.count += 1
    if command != '' and command[0:2] != '//':
      if '//' in command:
        self.curent_command = command[:command.find('//')].strip()
      else:
        self.curent_command = command
    else:
      pass

  # Returns the current instruction type (constant)
  def instructionType(self):
    if self.curent_command[0] == '@':
      return 'A_INSTRUCTION'
    elif self.curent_command[0] == '(':
      return 'L_INSTRUCTION'
    else:
      return 'C_INSTRUCTION'

  # Returns the instruction’s symbol (string)
  def symbol(self):
    if self.curent_command[0] == '@':
      return self.curent_command[1:]
    elif self.curent_command[0] == '(':
      return self.curent_command[1:-1]

  # Returns the instruction’s dest field (string)
  def dest(self):
    equal = self.curent_command.find('=')
    if equal > 0:
      return self.curent_command[:equal]
    else:
      return None
    
  # Returns the instruction’s comp field (string)
  def comp(self):
    equal = self.curent_command.find('=')
    semicolon = self.curent_command.find(';')
    if equal > 0 and semicolon > 0:
      return self.curent_command[equal+1:semicolon]
    elif equal < 0 and semicolon > 0:
      return self.curent_command[:semicolon]
    elif equal > 0 and semicolon < 0:
      return self.curent_command[equal+1:]
    else:
      return None
    
  # Returns the instruction’s jump field (string)
  def jump(self):
    semicolon = self.curent_command.find(';')
    if semicolon > 0:
      return self.curent_command[semicolon+1:]
    else:
      return None
  
  # Reset count 
  def reset(self):
    self.count = 0
