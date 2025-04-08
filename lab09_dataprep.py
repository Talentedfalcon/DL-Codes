import os
import shutil
import random

source_dir = "LGG_MRI_dataset/lgg-mri-segmentation"
train_dir = "mri-dataset/train"
val_dir = "mri-dataset/val"
test_dir = "mri-dataset/test"

patient_folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]
# random.shuffle(patient_folders)

# print(patient_folders)

train_split = int(0.8 * len(patient_folders))
val_split = int(0.9 * len(patient_folders))

train_patients = patient_folders[:train_split]
val_patients = patient_folders[train_split:val_split]
test_patients = patient_folders[val_split:]

print(patient_folders)

def move_files(patients, destination):
    for patient in patients:
        patient_path = os.path.join(source_dir, patient)
        print(patient_path)
        for file in os.listdir(patient_path):
            src = os.path.join(patient_path, file)
            if "_mask" in file:
                dst = os.path.join(destination, "masks", file)
            else:
                dst = os.path.join(destination, "images", file)
            shutil.move(src, dst)

move_files(train_patients, train_dir)
move_files(val_patients, val_dir)
move_files(test_patients, test_dir)

print("Dataset split completed!")
