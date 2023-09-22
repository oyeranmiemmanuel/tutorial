import cv2
import mediapipe as mp
import numpy as np 
import time


class FaceDetector:
	def __init__(self, minDetectionCon=0.5):
		self.minDetectionCon= minDetectionCon
		self.mpFaceDetection= mp.solutions.face_detection
		self.mpDraw= mp.solutions.drawing_utils
		self.faceDetection= self.mpFaceDetection.FaceDetection(self.minDetectionCon)


	def findFaces(self, img, draw=True):
		imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results= self.faceDetection.process(imgRGB)
		bboxs=[]

		if self.results.detections:
			for id, detection in enumerate(self.results.detections):
				# mpDraw.draw_detection(frame, detection)
				# print(id, detection)
				# print(detection.score)
				# print(detection.location_data.relative_bounding_box)	
				bboxC= detection.location_data.relative_bounding_box
				ih, iw, ic= imgRGB.shape
				bbox= int(bboxC.xmin * iw), int(bboxC.ymin * ih),\
						int(bboxC.width * iw), int(bboxC.height * ih)
				bboxs.append([id, bbox, detection.score])
				if draw:
					img= cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)

					img= self.fancyDraw(img, bbox)
					cv2.putText(img, f'CONFD: {int(detection.score[0]*100)}%',  (bbox[0], bbox[1]-20),
												 cv2.FONT_HERSHEY_PLAIN,
												1, (0,255,0), 2)

		return imgRGB, bboxs


	# draws the fancy bounding box 
	# the params are image, bounding box, length, thickness and rectangle thickness 
	def fancyDraw(self, img, bbox, l=5, t=1, rt=1):
		x, y, w, h= bbox
		x1, y1= x+w, y+h

		cv2.rectangle(img, bbox, (0,255,255), rt)
		#Top Left
		cv2.line(img, (x,y), (x+l, y), (255,0,255), t)
		cv2.line(img, (x,y), (x, y+l), (255,0,255), t)

		#Top Right
		cv2.line(img, (x1,y), (x1-l, y), (255,0,255), t)
		cv2.line(img, (x1,y), (x1, y+l), (255,0,255), t)

		#Buttom Left
		cv2.line(img, (x,y1), (x+l, y1), (255,0,255), t)
		cv2.line(img, (x,y1), (x, y1-l), (255,0,255), t)

		#Button Right
		cv2.line(img, (x1,y1), (x1-l, y1), (255,0,255), t)
		cv2.line(img, (x1,y1), (x1, y1-l), (255,0,255), t)

		return img

def main(cap):
	# cap= cv2.VideoCapture(cap)
	pTime=0
	detector= FaceDetector()
	count= 0
	# while True:
	success, frame= cap.read()
	frame= cv2.resize(frame, (200,250))

	# put the 3rd param as True if you want a fancy bounding box
	frame, bboxs = detector.findFaces(frame, False)


	cTime= time.time()
	fps= 1/(cTime-pTime)
	pTime= cTime
	# cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN,3, (0,255,0), 2)
	if bboxs:
		return frame, bboxs
	return frame, None


# we're not using this function due to bugs
def img_bbox(img):

    mp_face_detection = mp.solutions.face_detection

    face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

    mp_drawing = mp.solutions.drawing_utils

    sample_img = img


    face_detection_results = face_detection.process(sample_img)


    bboxs=[]
    if face_detection_results.detections:

        for face_no, face in enumerate(face_detection_results.detections):

            bboxC= face.location_data.relative_bounding_box
            ih, iw, ic= sample_img.shape
            bbox= int(bboxC.xmin * iw), int(bboxC.ymin * ih),\
                            int(bboxC.width * iw), int(bboxC.height * ih)

            bboxs.append([face_no, bbox, face.score])
    return bboxs[0][1]
