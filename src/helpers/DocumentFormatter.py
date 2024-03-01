from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json


class DocumentFormatter:
    # @staticmethod
    # def merge_json_from_txt(path_1, path_2):
    #     """ merge two json files from txt """
    #     with open(path_1, 'r', encoding='UTF-8') as file_1:
    #         json_1 = json.loads(file_1.read())
    #
    #     with open(path_1, 'r', encoding='UTF-8') as file_2:
    #         json_2 = json.loads(file_2.read())
    #
    #     merged_json = {**json_1, **json_2}
    #
    #     return merged_json

    @staticmethod
    def merge_json(docs):
        """ merge several json files """
        merged = {}

        for doc in docs:
            json_content = json.loads(doc)
            merged.update(json_content)

        return merged

    @staticmethod
    def split(doc):
        """ split documents by chunks """
        loader = TextLoader(doc, encoding='utf-8')
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 32000,
            chunk_overlap = 0,
            length_function = len,
            is_separator_regex = False,
        )
        
        documents = text_splitter.split_documents(documents)

        return documents
