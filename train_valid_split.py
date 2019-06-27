import os
import random

def train_valid_split(images_path, train_txt_path, valid_txt_path):
    train = open(train_txt_path, 'w')
    valid = open(valid_txt_path, 'w')
    for root, dirs, files in os.walk(images_path):
        annotation_num = len(files)
        random.shuffle(files)
        for i, file in enumerate(files):
            file = file.replace('txt', 'png')
            if i < annotation_num * 0.8:
                train.writelines(os.path.join(root, file).replace('labels', 'images'))
                train.write('\n')
            else:
                valid.writelines(os.path.join(root, file).replace('labels', 'images'))
                valid.write('\n')


def main():
    images_path = '/home/stuart/Documents/PyTorch-YOLOv3/data/custom/labels'
    train_txt_path = '/home/stuart/Documents/PyTorch-YOLOv3/data/custom/train.txt'
    valid_txt_path = '/home/stuart/Documents/PyTorch-YOLOv3/data/custom/valid.txt'

    train_valid_split(images_path, train_txt_path, valid_txt_path)


if __name__ == "__main__":
    main()


