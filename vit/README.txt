For VIT model, you should have a data structure like this:
-root-flowers-train
				-class_0
				-class_1
				....

read_split_data function in utils.py can split the data into train and val.
For parameters like batch size, epoch and lr:
	You can change them in train.py

Training:
python train.py
