import face_recognition.api as face_recognition

known_image = face_recognition.load_image_file("face_recognition_github/examples/biden.jpg")
unknown_image = face_recognition.load_image_file("face_recognition_github/tests/test_images/obama3.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

loc = face_recognition.face_locations(unknown_image)

if (loc):
    print("good")
else:
    print("step in the frame")