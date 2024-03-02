from typing import List

class ErrorHandler():
    def __init__(self, OPTIONS_LIST: List[str]) -> None:
        self.OPTIONS_LIST = OPTIONS_LIST
      
    # Public function
    def handle(self, argv: List[str]):
        if(len(argv) < 2):
            raise ValueError("Missing argument")

        elif(len(argv) > 2):
            raise ValueError("More arguments than expected")
        
        if(argv[1] not in self.OPTIONS_LIST):
            raise ValueError("Invalid option, valid options are : 'merge', 'split_classic', 'split_pack'")
