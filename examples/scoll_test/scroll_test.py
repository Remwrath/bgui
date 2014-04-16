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
		self.frame = bgui.Frame(self, border=0, size=[1,1], pos=[0, 0])
		self.frame.colors = [(0, 0, 0, 0.2) for i in range(4)]
		self.scrollable_frame = bgui.ScrollableFrame(self.frame, size=[0.5, 0.5], pos=[0.25, 0.25])
		self.frame0 = bgui.Frame(self.scrollable_frame.client, border=0, size=[200, 200], pos=[100, 100], options=bgui.BGUI_NO_NORMALIZE)
		self.frame0.colors = [(1, 0, 0, 1) for i in range(4)]
		self.button = bgui.FrameButton(self.scrollable_frame.view, text='Toggle Clipping!', size=[0.4, 0.1], pos=[0.5, 0.6],
			options = bgui.BGUI_DEFAULT)
		self.button.on_click = self.toggle_clip
		
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