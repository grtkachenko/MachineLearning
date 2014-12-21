import numpy as np

train_labels_fname = 'train-labels.idx1-ubyte'
train_images_fname = 'train-images.idx3-ubyte'
test_labels_fname  = 't10k-labels.idx1-ubyte'
test_images_fname  = 't10k-images.idx3-ubyte'

def read_int(f):
    return int.from_bytes(f.read(4), byteorder='big')

def read_labels(filename):
    labels = []
    with open(filename, 'rb') as f:
        f.read(4) # header
        cnt = read_int(f)
        for _ in range(cnt):
            labels.append(int.from_bytes(f.read(1), byteorder='big'))
    return labels

def read_images(filename):
    matrices = []
    with open(filename, 'rb') as f:
        f.read(4) # header
        cnt, h, w = read_int(f), read_int(f), read_int(f)
        cnt = min(cnt, 1000)
        bytes = np.array(bytearray(f.read(cnt*h*w)))
        idx = 0
        for _ in range(cnt):
            matrix = np.zeros(h*w).reshape(h, w)
            for i in range(h):
                for j in range(w):
                    val = int(bytes[idx]) / 255.0 * 2 - 1.0
                    matrix[i][j] = val
                    idx += 1
            matrices.append(matrix)
    return matrices

train_labels, test_labels = read_labels(train_labels_fname), read_labels(test_labels_fname)
train_images, test_images = read_images(train_images_fname), read_images(test_images_fname)


