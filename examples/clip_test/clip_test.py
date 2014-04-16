import sys

# So we can find the bgui module
sys.path.append('../..')

import bgui
import bgui.bge_utils
import bge

class SimpleLayout(bgui.bge_utils.Layout):
	"""A layout showcasing various Bgui features"""

	def __init__(self, sys, data):
		super().__init__(sys, data)
		self.frame = bgui.Frame(self, border=0, size=[0.5, 0.5], pos=[0, 0], clip=True)
		self.frame.colors = [(0, 0, 0, 0.8) for i in range(4)]
		self.frame0 = bgui.Frame(self.frame, border=0, size=[0.8, 1.1], pos=[0, 0])
		self.frame0.colors = [(1, 1, 1, 1) for i in range(4)]
		self.lbl_file = bgui.label.Label(self.frame, text='TESTING123', pos=[0.9, 0.1], color=(1,0,0,1))
		self.frame1 = bgui.Frame(self, border=0, size=[0.5, 0.5], pos=[0.5, 0.5], clip=True)
		self.frame1.colors = [(0, 0, 0, 0.8) for i in range(4)]
		self.frame2 = bgui.Frame(self.frame1, border=0, size=[0.8, 1.1], pos=[0, -0.1])
		self.frame2.colors = [(1, 1, 1, 1) for i in range(4)]
		self.lbl_file = bgui.label.Label(self.frame1, text='TESTING123', pos=[-0.1, 0.1], color=(1,0,0,1))
		self.button = bgui.FrameButton(self.frame, text='Toggle Clipping!', size=[0.4, 0.1], pos=[0.5, 0.5],
			options = bgui.BGUI_DEFAULT)
		self.button.on_click = self.toggle_clip
		self.button1 = bgui.FrameButton(self.frame1, text='Toggle Clipping!', size=[0.4, 0.1], pos=[0.5, 0.5],
			options = bgui.BGUI_DEFAULT)
		self.button1.on_click = self.toggle_clip
		
	def toggle_clip(self, widget):
		widget.parent.clip = not widget.parent.clip
		
def main(cont):
	own = cont.owner
	mouse = bge.logic.mouse

	if 'sys' not in own:
		# Create our system and show the mouse
		own['sys'] = bgui.bge_utils.System()
		own['sys'].load_layout(SimpleLayout, None)
		mouse.visible = True
	else:
		own['sys'].run()