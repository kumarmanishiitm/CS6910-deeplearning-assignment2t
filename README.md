 """
    README Part-A - Question 1 --------------------------------------------------------------------
        
        To compile the file with command line arguments write in following format in terminal :-
	
        !python3 filename filter_multiplier,num_filters dropout dense_size  batch_normalisation
        Example:
         !python3 q1.py 2 32 0.27 1331 True True 1 0.0007
    



                    -------------------  PartB:---------------------
       To compile the file with command line arguments write in following format in terminal :-
      !python3 filename base_model,dense_Size,batch_normalisation,augment_data,epochs,dropout,lr
       Example:
        !python3 cmdpartb.py InceptionResNetV2  128 True True 1 0.4 0.0002
    
    """
## Part A

1. The notebook is structured to be run cell by cell.
2. Next, the google drive needs to be mounted and the iNaturalist file needs to be unzipped. This part of the code will need to be modified according to the filepath on your local machine.
3. Functions train() and test() integrate WandB with the training, validation and testing process. A sweep config is defined already, whose hyperparameters and values can be modified. The train or test function can be called by the sweep agent.
4. Further, there are functions provided to plot sample image predictions and filter visualizations on the test data, which can be run from within the test function.
5. Also, there is a function which can customise the run names in WandB.
6. For the visualization of Guided Backpropgation we have made a function `Guided_Back_Propagation. To run it for visualizing the guided backpropagation of 10 images.


## Part B

1. The notebook is structured such that it can be ran cell by cell


## Part C
"""1. weights for the car or person detection are present in the github.
2.Two video i ihave taken from youtube.
3.video link:
https://drive.google.com/file/d/1Tmo3aHVu9sxj7zw6iE6-wXO0jHJXfw7W/view?usp=sharing
https://drive.google.com/file/d/1Tmo3aHVu9sxj7zw6iE6-wXO0jHJXfw7W/view?usp=sharing
4.yolov3-tiny.weights
https://drive.google.com/file/d/1VKqmd20cngqLea1x6vcfa5OSg_Hlr5Zz/view?usp=sharing"""
