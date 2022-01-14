import face_recognition

class UserRecognition:
    def __init__(self, userImage, inputImage):
        self.userImage = userImage
        self.inputImage = inputImage

    def recognize_user(self):
        user_face_encoding, unknown_face_encoding = self.__generate_encodings()

        self.__print_result(face_recognition.compare_faces([user_face_encoding], unknown_face_encoding))
            
    def __generate_encodings(self):
        try:
            user_image, unknown_image = self.__load_images()
            user_face_encoding = face_recognition.face_encodings(user_image)[0]
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
            return user_face_encoding, unknown_face_encoding
        except:
            print("Failed to create encodings. Aborting...")
            quit()

    def __load_images(self):
        try:
            user_image = face_recognition.load_image_file(self.userImage)
            unknown_image = face_recognition.load_image_file(self.inputImage)
            return user_image, unknown_image
        except:
            print("Failed to load images. Check the image files. Aborting...")
            quit()

    def __print_result(self, results):
        if results[0]:
            print("User recognized.")
        else:
            print("User not recognized.")
