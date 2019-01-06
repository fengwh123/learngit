import face_recognition
known_image = face_recognition.load_image_file("wcs.jpg")
unknown_image = face_recognition.load_image_file("pt.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)
print(type(results))
print(type(2))
print(results[0])
print(type(results[0]))
if results[0]:
    print(1+1)
print('132')