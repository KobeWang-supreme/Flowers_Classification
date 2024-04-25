For VGG model, you should have a data structure like this:
root-train
		-class_0
		-class_1
		...
	-val
		-class_0
		-class_1
		....

For parameters like batch size, epoch and lr:
	You can change them in vgg_train.py