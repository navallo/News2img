import tensorflow as tf
import urllib2
import os
from sklearn import preprocessing

#Usage: (tensorflow2) navallo@navallo-P65xRP:~/Documents/CODE/news2img$ python img2vector.py
def create_graph(model_file):
    """Creates a graph from saved GraphDef file and returns a saver."""
    # Creates graph from saved graph_def.pb.
    with tf.gfile.FastGFile(model_file, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

model_file = "./data/minimal_graph.proto"
dataset_dir = '/home/navallo/Documents/DATA/formalCompetition4/News_pic_info_validate/'

img_vectors = open('./data/img_vectors.txt', 'w')
count_jpeg = 0
count_not_jpeg = 0
with tf.Graph().as_default():
    with tf.Session() as new_sess:
        create_graph(model_file)
        softmax = new_sess.graph.get_tensor_by_name("InceptionResnetV2/Logits/Predictions:0")
        # Loading the injected placeholder
        input_placeholder = new_sess.graph.get_tensor_by_name("input_image:0")

        for filename in os.listdir(dataset_dir):
            path = os.path.join(dataset_dir, filename)
            image_string = tf.gfile.FastGFile(path, 'r').read()
            try:
                probabilities = new_sess.run(softmax, {input_placeholder: image_string})
                probabilities = preprocessing.normalize(probabilities, norm='l2')
                img_vectors.write(filename+':')
                for tmp in probabilities:
                    for temp in tmp:
                        img_vectors.write(str(temp)+',')
                img_vectors.write('\n')
                count_jpeg = count_jpeg + 1
            except:
                count_not_jpeg = count_not_jpeg + 1
                pass
                
print('count_jpeg = %s'%count_jpeg)
print('count_not_jpeg = %s'%count_not_jpeg)
img_vectors.close()