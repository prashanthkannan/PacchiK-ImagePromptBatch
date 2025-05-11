  
import os
import csv 

class LoadImageandPrompt:

    def __init__(self):
        self.current_index = 0
        pass
 

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "FolderLocation": ("STRING",),
                "PromptFileName": ("STRING", ),
                "index": ("INT",),
            },
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("Image Name", "Prompt")


    FUNCTION = "LoadImageandPrompt"

    CATEGORY = "LoadImageandPrompt"

    def LoadImageandPrompt(self, index, FolderLocation, PromptFileName):
        PromptFileName = FolderLocation + PromptFileName
        with open(PromptFileName, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip header row if it exists
            header = next(reader, None)
            
            # Read rows and find matching index
            for row in reader:
                if len(row) >= 3:  # Ensure row has at least 3 columns
                    # Check if the index matches (convert to int for comparison)
                    if str(index) == row[0]:
                        return FolderLocation+row[1], row[2]  # Return image_name and prompt
            
            # If we get here, no matching index was found
            print(f"No entry found with index {index}")
            return None, None


    @classmethod
    def IS_CHANGED(s, index, FolderLocation, PromptFileName):
        return (index, FolderLocation, PromptFileName)
        
    # This method is called when the node is queued
    def queue_execution(self, index, FolderLocation, PromptFileName):
        # Create a copy of the inputs
        new_values = {"index": index + 1, "FolderLocation": FolderLocation, "PromptFileName": PromptFileName}
        return new_values

NODE_CLASS_MAPPINGS = {
    "LoadImageandPrompt": LoadImageandPrompt

}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageandPrompt": "Load Image and Prompt",
    
}