import mwclient
from mwclient import Site
import json
import urllib2

import logging
import time
from itertools import islice
logger = logging.getLogger("__main__")

class wiki():
    def __init__(self,config="config.txt"):
        try:
            #load user, pass file
            p               = open(config,'r').readlines()
            user            = p[0][5:].strip()
            password        = p[1][5:].strip()
        except Exception as e:
            logger.error(str(e))
            raise (type(e),e.args)
        try:
            self.site            = mwclient.Site('duelyst.gamepedia.com',path='/')
            logger.info("[*]Connected to  duelyst.gamepedia.com ")
            self.site.login(user,password)
            logger.info("[*]Logged in with bot credentials from %s"%config)
            self.success =0
            self.failed  =0
            self.existing=0
            self.forced  =0
        except Exception as e:
            logger.error(str(e))
            raise (type(e),e.args)
    
    def createPage(self,url,text,wait=0.5): #wait is the wait time after creating the page to prevent wiki ddos
        page = self.site.pages[url]
        if(page.exists):
            logger.error("[!]%s already exists!Cannot create a page for it."%url)
            self.failed   +=1
            self.existing +=1
            return False
        else:
            result = page.save(text, 'Page Creation for '+url)
            if result['result'] == 'Success':
                self.success+=1
                logger.debug("[*]Created page-%s"%url)
                time.sleep(wait)
                return True
            else:
                self.failed +=1
                logger.error(
                    "[!]Cannot create a page %s" % url)
                return False

    def editPage(self, url, text, user="Mycroft92", force=False, wait=0.5):
        #user is the guy that runs the bot under his account
        page = self.site.pages[url]
        if page.exists:  # this is needed else latest_rev might throw IndexError if page is not present
            self.existing +=1
            latest_rev = user
            for rev in islice(page.revisions(), 1):
                # this is one tricky way to get the last element, no cleaner way available
                latest_rev = rev['user']
            if (latest_rev != user) :  #if latest  edit is not by me
                if force:
                    logger.warning("[!]Latest edit for %s is not made by %s"%(url,user))
                    result = page.save(text, 'Editing Page for '+url)
                    if result['result'] == 'Success':
                        self.forced+=1
                        self.success+=1
                        logger.debug("[*]Edited page-%s"%url)
                        time.sleep(wait)
                        return True
                    else:
                        self.failed +=1
                        self.forced +=1
                        logger.error("[!]Cannot create a page %s" % url)
                        return False
                else:
                    logger.error("[!]Cannot create page :" + url +
                             ",Latest edit made by:"+latest_rev)
                    self.failed +=1
                    return False
            else:
                result = page.save(text, 'Editing page '+url)
                if result['result'] == 'Success':
                    self.success += 1
                    logger.debug("[*]Edited Page-%s" % url)
                    time.sleep(wait)
                    return True
                else:
                    self.failed += 1
                    logger.error("[!]Cannot create a page %s" % url)
                    return False
        return self.createPage(url,text)
                
    
    def getPage(self,url):
        return self.site.pages[url].text()
    
    def report(self):
        logger.info("[*]Successful creations/edits:%d"%self.success)
        logger.info("[*]Failed creations/edits:%d" % self.failed)
        logger.info("[*]Existing pages found:%d" % self.existing)
        logger.info("[*]Forced edits:%d" % self.forced)
