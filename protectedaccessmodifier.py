class PAM:
	_name = None
	def __init__(self,name):
		self.name = name
	def _displayName(self):
		print(self.name)
		
class PAM_dc(PAM):
	def __init__(_self,name):
		PAM.__init__(_self,name)
	def displayD(self):
		self._displayName()

Obj = PAM_dc('BIA101')
Obj.displayD()
