import xml.etree.ElementTree as ET
import os

classes = ["logo"]

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(xml_path, output_path):
    in_file = open(xml_path)
    out_file = open(output_path, 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

def main():
    voc_dir = '/home/stuart/Documents/image'
    output_dir = '/home/stuart/Documents/PyTorch-YOLOv3/data/custom/labels'

    for root, dirs, files in os.walk(voc_dir):
        for file in files:
            if file.endswith('xml'):
                xml_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, file.replace('xml', 'txt'))

                convert_annotation(xml_path, output_path)

if __name__ == '__main__':
    main()