from abc import ABC, abstractmethod


class iplugin(ABC):

    @abstractmethod
    def get_serie_title(self, browser, url):
        raise NotImplementedError

    @abstractmethod
    def get_chapter_url_list(self, browser, url):
        raise NotImplementedError

    @abstractmethod
    def get_page_url_list(self, browser, url):
        raise NotImplementedError

    @abstractmethod
    def get_page_img_url(self, browser, url):
        raise NotImplementedError
