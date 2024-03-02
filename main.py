from services.merger import Merger
from services.splitter import Splitter
from services.error_handler import ErrorHandler
from sys import argv

FOLDER = "pdf_files"

MERGE_OPTION = "merge"
SPLIT_CLASSIC_OPTION = "split_classic"
SPLIT_PACK_OPTION = "split_pack"
OPTIONS_LIST = (MERGE_OPTION, SPLIT_CLASSIC_OPTION, SPLIT_PACK_OPTION)


if __name__ == '__main__':
    print("=== Start to work ! ===")

    error_handler = ErrorHandler(OPTIONS_LIST)
    error_handler.handle(argv)

    option = argv[1]

    if(option == MERGE_OPTION):
        merger = Merger(FOLDER)
        merger.merge_pdf()

    else:
        splitter = Splitter()

        if(option == SPLIT_PACK_OPTION):
            splitter.split(True)

        elif(option == SPLIT_CLASSIC_OPTION):
            splitter.split(False)

    print("=== Job done ! ===")
