# USAGE
# python pelatihan_dataset.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle
# USAGE
# python buat_dataset.py --dataset dataset --embeddings output/embeddings.pickle --detector programming_mojokerto --embedding-model openface_nn4.small2.v1.t7

# impor paket yang diperlukan


# impor paket yang diperlukan
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--embeddings", required=True,
	help="path to serialized db of facial embeddings")
ap.add_argument("-r", "--recognizer", required=True,
	help="path to output model trained to recognize faces")
ap.add_argument("-l", "--le", required=True,
	help="path to output label encoder")
args = vars(ap.parse_args())

print("[INFO] memuat hiasan wajah...")
data = pickle.loads(open(args["embeddings"], "rb").read())

print("[INFO] label pengodean...")
le = LabelEncoder()
labels = le.fit_transform(data["names"])

print("[INFO] model pelatihan...")
recognizer = SVC(C=1.0, kernel="linear", probability=True)
recognizer.fit(data["embeddings"], labels)

f = open(args["recognizer"], "wb")
f.write(pickle.dumps(recognizer))
f.close()

f = open(args["le"], "wb")
f.write(pickle.dumps(le))
f.close()