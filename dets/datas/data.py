'''
该模块用于对各类数据集进行读取格式的对其，
使得各类不同组织格式数据的读取之后具有相同的数据格式
对于每一张影像，self.proposal记录一条记录{
    image，array
    image_name, str
    shape, (m,n)
    object_gt, [[],[]]
}
'''
import abc
import os.path as osp

class data(abc):
    def __init__(self, 
                data_dir=None, 
                pipeline=None,
                ann_dir=None,
                annfile=None,
                img_dir=None,
                test_mode=False,
                **kwgs):
        self.data_dir = data_dir
        self.pipeline = pipeline
        self.ann_dir = ann_dir
        self.annfile = annfile
        self.img_dir = img_dir
        self.test_mode = test_mode
        self.proposals = []
        assert(osp.exists(self.data_dir))
        if(annfile is not None):
            self.proposals = self.load_annotations(osp.join(self.data_dir, self.annfile,
                                                    osp.join(self.data_dir, self.img_dir)))

    def load_annotations(self, annotation_dir_or_annfile, images):
        pass

    def __len__(self):
        return len(self.proposals)

    def pre_train(self, result):
        pass

    def pre_test(self, result):
        pass
    def _getitem__(self, index):
        return self.pipeline(self.proposals, index)