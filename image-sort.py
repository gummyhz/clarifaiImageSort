from clarifai.rest import ClarifaiApp
import json
import os
import shutil

# Access your application
clarifai_app = ClarifaiApp(api_key='8f8a14cc0da7413ba073fe0d01e22831')
# This is the General model id
clarifai_model = clarifai_app.models.get(model_id='aaa03c23b3724a16a56b629203edc62c')

DIRECTORIES = ['puppy', 'tree', 'city', 'cream']
# Type out the full path to clarifai_images
clarifai_images_path = 'C:\\Users\\Rebecca\\github\\clarifaiImageSort\\clarifai_images'

image_filenames = os.listdir(clarifai_images_path)
for file in image_filenames:
    print('Checking if dir :', file)
    if os.path.isdir(clarifai_images_path+'\\'+file):
        image_filenames.remove(file)
# START CODING HERE

# 1. Loop through all the files in clarifai_images
for file in image_filenames:
    # 2. Use .predict_by_filename() on model to get the json response from Clarifai
    os.chdir(clarifai_images_path)
    print(file)
    response = clarifai_model.predict_by_filename(file)
    print('got response')
    # 3. Create an empty list for the image tags
    imageTags = []
    # 4.  Loop through ['outputs'][0]['data']['concepts'] and append the items to the image tags list
    for x in response['outputs'][0]['data']['concepts']:
        imageTags.append(x['name'])
    # 5. Move the files to the appropriate folder based on whether or not the image tag matches the name in DIRECTORIES
    #    Hint: Review your file organizer
    for directory in DIRECTORIES:
        if directory in imageTags:
            if directory in os.listdir(clarifai_images_path):
                print('moving to exhisting folder')
                shutil.move(file, directory)
            else:
                print('making folder')
                os.chdir(clarifai_images_path)
                os.makedirs(directory)
                shutil.move(file, directory)
