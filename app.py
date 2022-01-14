import argparse
from user_recognition import  UserRecognition

def main():
    parser = setup_parser()
    args = vars(parser.parse_args())
    user, unknown_image = parse_arguments(args)
    recognize_user(user, unknown_image)

def setup_parser():
    parser = argparse.ArgumentParser(description='User recoginition app.')
    parser.add_argument('-u','--user', help='User image.', required=True)
    parser.add_argument('-i','--input', help='Image to check.', required=True)
    return parser

def parse_arguments(args):
    user = args['user']
    unknown_image = args['input']
    return user,unknown_image

def recognize_user(user, unknown_image):
    user_recognition = UserRecognition(user, unknown_image)
    user_recognition.recognize_user()

if __name__ == "__main__":
    main()
