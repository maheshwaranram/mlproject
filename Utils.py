from typing import List

class Function:

    'This Function returns Library requirements'
    def get_requirements(filepath:str)-> List[str]:
        library=[]
        with open(filepath) as file_obj:
            library= file_obj.readlines()
            library= [package.replace("\n","") for package in library if package !='-e .']
        return library



Function.get_requirements("requirements.txt")