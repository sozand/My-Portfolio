# USAGE
# Run โดยคำสั่ง
# python knn.py --dataset ../datasets/animals


from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from pyimagesearch.preprocessing import SimplePreprocessor
from pyimagesearch.datasets import SimpleDatasetLoader
from imutils import paths
import argparse

# argument parse and parse the arguments
ap = argparse.ArgumentParser()
# Path to dataset
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
# จำนวน neighbors สำหรับ k-nn [k- nearest neighbors]
ap.add_argument("-k", "--neighbors", type=int, default=1,
	help="# of nearest neighbors for classification")
# -1 คือใช้ทุก CPU core ที่มี
ap.add_argument("-j", "--jobs", type=int, default=-1,
	help="# of jobs for k-NN distance (-1 uses all available cores)")
args = vars(ap.parse_args())

# นำที่อยู่ทั้งหมดของรูปภาพที่จะนำมาฝึกโมเดล เก็บไว้ที่ imagePaths
print("[INFO] loading images...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialize the image preprocessor, load the dataset from disk,
# and reshape the data matrix
sp = SimplePreprocessor(32, 32)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels) = sdl.load(imagePaths, verbose=500)
data = data.reshape((data.shape[0], 3072))

# เปลี่ยนจากชื่อคลาสเป็นตัวเลข int
le = LabelEncoder()
labels = le.fit_transform(labels)

# แบ่ง Train กับ test 75:25
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.25, random_state=42)

# train and evaluate a k-NN classifier
print("[INFO] evaluating k-NN classifier...")
model = KNeighborsClassifier(n_neighbors=args["neighbors"],
	n_jobs=args["jobs"])
model.fit(trainX, trainY)
print(classification_report(testY, model.predict(testX),
	target_names=le.classes_))