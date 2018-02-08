#!/usr/bin/python
#Author      : Mycroft92
#Description : Forms the base of gifs making from resources in duelyst
import xml.etree.ElementTree as ET
import logging
logger = logging.getLogger(__name__)


class xml_reader():
    def __init__(self,plist,debug=2):
        if debug>=2:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        try:
            self.data = ET.parse(plist).getroot()
            logger.debug("[*]Finished parsing plist file :"+plist)
        except Exception as e:
            logger.error("[!]Failed to parse the given file path:"+plist)
            raise (e)
        

    def __attack_list(self):
        pass

    def __breathing_list(self):
        pass

    def __cast_list(self):
        pass

    def __castend_list(self):
        pass

    def __castloop_list(self):
        pass

    def __caststart_list(self):
        pass

    def __death_list(self):
        pass

    def __hit_list(self):
        pass

    def __idle_list(self):
        pass

if __name__ == "__main__":
    x = xml_reader(
        r"C:\Steam\steamapps\common\Duelyst\resources\app\src\resources\units\boss_andromeda.plist"
    )
    #finally found the correspondence, now put them into one hash
    for tag in x.data[0][1].iter('key'):
        print tag.text
    for tag in x.data[0][1].iter('dict'):
        for child in tag.findall('string'):
            print child.text

class gif_builder():
    def __init__(self,plist="",png="",dumpdir=""):
        #plist file path,png file path and the directory to dump the gif file,default is cwd
        self.plist    = xml_reader(plist)
        self.dumpdir  = dumpdir

    def _read_images(self):
        pass

    def gif_gen(self):
        pass