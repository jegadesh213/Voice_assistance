from gpiozero import LED
import speech_recognition as sr

for i,mic_name in enumerate(sr.Microphone.list_microphone_names()):
	print("mic: " + mic_name)
	if "USB Audio Device" in mic_name:
		print("USB Audio Device " + mic_name)
		mic = sr.Microphone(device_index=i,chunk_size=1024, sample_rate= 1024)

pi_ear = sr.Recogniger()

led = LED(17)
you="turn on the light"
print("you: " + you)

while True:
	with mic as source:
		pi_ear.adjust_for_ambient_noise(source,duration=0.5)
		print("pi: I'm listening")
		audio = pi_ear.listen(source)
	if you == "turn on the light":
		print("pi: " + "sure,I'm turning on the light")
		led.off()
	if you == "turn off the light":
		print("pi: " + "sure,I'm turning off the light")
		led.on()