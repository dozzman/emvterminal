from emvframework.emv import EMV

class Terminal(EMV):

	def SELECT_PSE(self):
		return self.SELECT_FILE(b'1PAY.SYS.DDF01', p1=0x04, p2=0x00)
