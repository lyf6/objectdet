from .data import data
import coco

class cocodata(data):
    
    def load_annotations(self, annotation_dir_or_annfile, images):
        