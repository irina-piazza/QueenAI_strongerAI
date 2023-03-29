import os


folder_path_out = './fitness_poses_images_out/in/'  # Replace with the path to the first subfolder
folder_path_in = './fitness_poses_images_out/out/'  # Replace with the path to the second subfolder

# List to store file names
def return_list_image(dir_path):
    file_names = []
    # Iterate over files in directory
    for file in os.listdir(dir_path):
        # Check if file is a regular file (not a directory)
        if os.path.isfile(os.path.join(dir_path, file)):
            # Add file name to list
            file_names.append(file)

    return file_names



def remove_files(folder_path_small, folder_path_big):

    # Get a list of all file names in the first subfolder
    files_to_keep = os.listdir(folder_path_small)
    print(files_to_keep)

    # Loop through all files in the second subfolder
    for file_name in os.listdir(folder_path_big):
        print(file_name)
        if file_name not in files_to_keep:
            #print(file_name2)
            # Delete the file if it doesn't match the list
            os.remove(os.path.join(folder_path_big, file_name))

def main():
    dir_path = "./fitness_poses_images_out/in/"
    list_files_up = return_list_image(dir_path)
    dir_path = "./fitness_poses_images_out/out/"
    list_files_down = return_list_image(dir_path)
    folder_path_out = './fitness_poses_images_out/out/'  # Replace with the path to the first subfolder
    folder_path_in = './fitness_poses_images_out/in/'  # Replace with the path to the second subfolder
    print(len(list_files_up))
    print(len(list_files_down))
    remove_files(folder_path_out,folder_path_in)

if __name__ == "__main__":
    main()