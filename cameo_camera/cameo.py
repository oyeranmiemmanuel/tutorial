import cv2
from managers import WindowManager, CaptureManager
import utils
import filter
import numpy as np



class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo',self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        # self._captureManager.enterFrame()
        # self.frame = self._captureManager.frame
        self.blank= np.zeros((400,400))
        self.kernel= np.array([
                            [-1,-1,-1],
                            [-1,-9,-1],
                            [-1,-1,-1]
                        ])
        filter.VConvolutionFilter(self.kernel)
        self.filt1= filter.SharpenFilter()
        self.filt2= filter.FindEdgesFilter()
        self.filt3= filter.BlurFilter()
        self.filt4= filter.EmbossFilter()



    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated: 
            self._captureManager.enterFrame()
            self.frame = self._captureManager.frame
            sharpen= self.filt1.apply(self.frame, self.blank)
            find_edges= self.filt2.apply(self.frame, self.blank)
            blur= self.filt3.apply(self.frame, self.blank)
            emboss=self.filt4.apply(self.frame, self.blank)
            utils.strokeEdges(self.frame, self.frame)
            gray= cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            neat= self.filt3.apply(gray, self.blank)
            new_edge= cv2.addWeighted(gray, 0.7, neat, 0.3, 0)
            # cv2.imshow("sharpen", sharpen)
            # cv2.imshow("Edges", find_edges)
            # cv2.imshow("Blur", blur)
            # cv2.imshow("Emboss", emboss)
            cv2.imshow("Emboss", new_edge)
            #heres the filter
            # TODO: Filter the frame (Chapter 3).
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress (self, keycode):
        """Handle a keypress.
        space -> Take a screenshot.
        tab -> Start/stop recording a screencast.
        escape -> Quit.
        """
        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()

        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__=="__main__":
    Cameo().run()

