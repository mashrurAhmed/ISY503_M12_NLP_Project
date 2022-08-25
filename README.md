The steps required to run this project:

1. Open the .ipynb file on Google Colab.

2. Run all code snippets in Section 1 to train the model by running each code snippet serially.
2.1. Alternatively, unzip saved_model.zip and upload the saved_model.h5 into the content folder of the Colab virtual machine.

3. Move to Section 2 to test the saved model

4. Before moving to Section 3, check if the Colab content folder has the 'app.py' file. 
4.1. If it doesn't exist, upload it from the project files
4.2. Alternatively, copy the contents of the final code segment on Colab into a new file called 'app.py'.

5. Follow the code on Section 3 to set up the project and serve the backend.

6. Open the index.html file on an editor, change the base URL on line 48 to the url provided by the curl request to localhost:4040 on Colab. Ensure the base url ends with a forward slash '/'.

7. Run the index.html file on browser.