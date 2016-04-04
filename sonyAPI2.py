#!/usr/bin/env python
import urllib2
import json
import detectCamera

class API(object):
	def do(self,command, param=[], url = ""):
		data = {
			'method': command,
			'params': param,
			'id':1,
			'version': "1.0"
		}
		try:
			if len(url) > 0:
				req = urllib2.Request(url + '/' + self.legal_command[command])
			else:
				req = urllib2.Request(self.url + '/' + self.legal_command[command])
		except KeyError:
			print command + "method doesn't exist"
			return None
		if len(self.api_list) > 0:
			try:
				self.api_list.index(command)
			except ValueError:
				print command + "Not support"
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(data))
		return json.load(response)

	def update_api_list(self):
		result = self.do('getAvailableApiList')
		try:
			self.api_list = result['result'][0]
		except KeyError:
			print 'Update Available API List failed'

	def update_url(self):
		self.url = detectCamera.get_api_url()

	api_list = []

	url = "http://192.168.122.1:8080/sony/"

	legal_command = {
		'setShootMode' : 'camera',
		'getShootMode' : 'camera',
		'getSupportedShootMode' : 'camera',
		'getAvailableShootMode' : 'camera',
		'actTakePicture' : 'camera',
		'awaitTakePicture' : 'camera',
		'startContShooting' : 'camera',
		'stopContShooting' : 'camera',
		'startMovieRec' : 'camera',
		'stopMovieRec' : 'camera',
		'startAudioRec' : 'camera',
		'stopAudioRec' : 'camera',
		'startIntervalStillRec' : 'camera',
		'stopIntervalStillRec' : 'camera',
		'startLoopRec' : 'camera',
		'stopLoopRec' : 'camera',
		'startLiveview' : 'camera',
		'stopLiveview' : 'camera',
		'startLiveviewWithSize' : 'camera',
		'getLiveviewSize' : 'camera',
		'getSupportedLiveviewSize' : 'camera',
		'getAvailableLiveviewSize' : 'camera',
		'setLiveviewFrameInfo' : 'camera',
		'getLiveviewFrameInfo' : 'camera',
		'actZoom' : 'camera',
		'setZoomSetting' : 'camera',
		'getZoomSetting' : 'camera',
		'getSupportedZoomSetting' : 'camera',
		'getAvailableZoomSetting' : 'camera',
		'actHalfPressShutter' : 'camera',
		'cancelHalfPressShutter' : 'camera',
		'setTouchAFPosition' : 'camera',
		'getTouchAFPosition' : 'camera',
		'cancelTouchAFPosition' : 'camera',
		'actTrackingFocus' : 'camera',
		'cancelTrackingFocus' : 'camera',
		'setTrackingFocus' : 'camera',
		'getTrackingFocus' : 'camera',
		'getSupportedTrackingFocus' : 'camera',
		'getAvailableTrackingFocus' : 'camera',
		'setContShootingMode' : 'camera',
		'getContShootingMode' : 'camera',
		'getSupportedContShootingMode' : 'camera',
		'getAvailableContShootingMode' : 'camera',
		'setContShootingSpeed' : 'camera',
		'getContShootingSpeed' : 'camera',
		'getSupportedContShootingSpeed' : 'camera',
		'getAvailableContShootingSpeed' : 'camera',
		'setSelfTimer' : 'camera',
		'getSelfTimer' : 'camera',
		'getSupportedSelfTimer' : 'camera',
		'getAvailableSelfTimer' : 'camera',
		'setExposureMode' : 'camera',
		'getExposureMode' : 'camera',
		'getSupportedExposureMode' : 'camera',
		'getAvailableExposureMode' : 'camera',
		'setFocusMode' : 'camera',
		'getFocusMode' : 'camera',
		'getSupportedFocusMode' : 'camera',
		'getAvailableFocusMode' : 'camera',
		'setExposureCompensation' : 'camera',
		'getExposureCompensation' : 'camera',
		'getSupportedExposureCompensation' : 'camera',
		'getAvailableExposureCompensation' : 'camera',
		'setFNumber' : 'camera',
		'getFNumber' : 'camera',
		'getSupportedFNumber' : 'camera',
		'getAvailableFNumber' : 'camera',
		'setShutterSpeed' : 'camera',
		'getShutterSpeed' : 'camera',
		'getSupportedShutterSpeed' : 'camera',
		'getAvailableShutterSpeed' : 'camera',
		'setIsoSpeedRate' : 'camera',
		'getIsoSpeedRate' : 'camera',
		'getSupportedIsoSpeedRate' : 'camera',
		'getAvailableIsoSpeedRate' : 'camera',
		'setWhiteBalance' : 'camera',
		'getWhiteBalance' : 'camera',
		'getSupportedWhiteBalance' : 'camera',
		'getAvailableWhiteBalance' : 'camera',
		'actWhiteBalanceOnePushCustom' : 'camera',
		'setProgramShift' : 'camera',
		'getSupportedProgramShift' : 'camera',
		'setFlashMode' : 'camera',
		'getFlashMode' : 'camera',
		'getSupportedFlashMode' : 'camera',
		'getAvailableFlashMode' : 'camera',
		'setStillSize' : 'camera',
		'getStillSize' : 'camera',
		'getSupportedStillSize' : 'camera',
		'getAvailableStillSize' : 'camera',
		'setStillQuality' : 'camera',
		'getStillQuality' : 'camera',
		'getSupportedStillQuality' : 'camera',
		'getAvailableStillQuality' : 'camera',
		'setPostviewImageSize' : 'camera',
		'getPostviewImageSize' : 'camera',
		'getSupportedPostviewImageSize' : 'camera',
		'getAvailablePostviewImageSize' : 'camera',
		'setMovieFileFormat' : 'camera',
		'getMovieFileFormat' : 'camera',
		'getSupportedMovieFileFormat' : 'camera',
		'getAvailableMovieFileFormat' : 'camera',
		'setMovieQuality' : 'camera',
		'getMovieQuality' : 'camera',
		'getSupportedMovieQuality' : 'camera',
		'getAvailableMovieQuality' : 'camera',
		'setSteadyMode' : 'camera',
		'getSteadyMode' : 'camera',
		'getSupportedSteadyMode' : 'camera',
		'getAvailableSteadyMode' : 'camera',
		'setViewAngle' : 'camera',
		'getViewAngle' : 'camera',
		'getSupportedViewAngle' : 'camera',
		'getAvailableViewAngle' : 'camera',
		'setSceneSelection' : 'camera',
		'getSceneSelection' : 'camera',
		'getSupportedSceneSelection' : 'camera',
		'getAvailableSceneSelection' : 'camera',
		'setColorSetting' : 'camera',
		'getColorSetting' : 'camera',
		'getSupportedColorSetting' : 'camera',
		'getAvailableColorSetting' : 'camera',
		'setIntervalTime' : 'camera',
		'getIntervalTime' : 'camera',
		'getSupportedIntervalTime' : 'camera',
		'getAvailableIntervalTime' : 'camera',
		'setLoopRecTime' : 'camera',
		'getLoopRecTime' : 'camera',
		'getSupportedLoopRecTime' : 'camera',
		'getAvailableLoopRecTime' : 'camera',
		'setWindNoiseReduction' : 'camera',
		'getWindNoiseReduction' : 'camera',
		'getSupportedWindNoiseReduction' : 'camera',
		'getAvailableWindNoiseReduction' : 'camera',
		'setAudioRecording' : 'camera',
		'getAudioRecording' : 'camera',
		'getSupportedAudioRecording' : 'camera',
		'getAvailableAudioRecording' : 'camera',
		'setFlipSetting' : 'camera',
		'getFlipSetting' : 'camera',
		'getSupportedFlipSetting' : 'camera',
		'getAvailableFlipSetting' : 'camera',
		'setTvColorSystem' : 'camera',
		'getTvColorSystem' : 'camera',
		'getSupportedTvColorSystem' : 'camera',
		'getAvailableTvColorSystem' : 'camera',
		'startRecMode' : 'camera',
		'stopRecMode' : 'camera',
		'setCameraFunction' : 'camera',
		'getCameraFunction' : 'camera',
		'getSupportedCameraFunction' : 'camera',
		'getAvailableCameraFunction' : 'camera',
		'setInfraredRemoteControl' : 'camera',
		'getInfraredRemoteControl' : 'camera',
		'getSupportedInfraredRemoteControl' : 'camera',
		'getAvailableInfraredRemoteControl' : 'camera',
		'setAutoPowerOff' : 'camera',
		'getAutoPowerOff' : 'camera',
		'getSupportedAutoPowerOff' : 'camera',
		'getAvailableAutoPowerOff' : 'camera',
		'setBeepMode' : 'camera',
		'getBeepMode' : 'camera',
		'getSupportedBeepMode' : 'camera',
		'getAvailableBeepMode' : 'camera',
		'getStorageInformation' : 'camera',
		'getEvent' : 'camera',
		'getAvailableApiList' : 'camera',
		'getApplicationInfo' : 'camera',
		'getVersions' : 'camera',
		'getMethodTypes' : 'camera',
		'getSchemeList' : 'avContent',
		'getSourceList' : 'avContent',
		'setStreamingContent' : 'avContent',
		'startStreaming' : 'avContent',
		'pauseStreaming' : 'avContent',
		'seekStreamingPosition' : 'avContent',
		'stopStreaming' : 'avContent',
		'requestToNotifyStreamingStatus' : 'avContent',
		'deleteContent' : 'avContent',
		'getContentCount' : 'avContent',
		'getContentList' : 'avContent',
		'setCurrentTime' : 'system'
	}
