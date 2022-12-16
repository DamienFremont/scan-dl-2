from abc import ABC, abstractmethod
import sys
import importlib

def get_plugin(name):
    try:
        sys.path.insert(0, '../scan-dl-2/scandl2_extensions')
        sys.path.insert(0, '../scan-dl-2-extensions/scandl2_extensions')
        module = importlib.import_module(f"{name}")
        serializer = getattr(module, f"{name}")
    except (ImportError, AttributeError) as err:
        raise ValueError(f"Unknown format {name!r}") from None
    return serializer

class iplugin(ABC):

    @abstractmethod
    def get_serie_title(browser, url):
        raise NotImplementedError

    @abstractmethod
    def get_chapter_url_list(browser, url):
        raise NotImplementedError

    @abstractmethod
    def get_page_url_list(browser, url):
        raise NotImplementedError

    @abstractmethod
    def get_page_img_url(browser, url):
        raise NotImplementedError
