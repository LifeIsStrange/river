from creme import stream

from . import base


class SMTP(base.FileDataset):
    """SMTP dataset from the KDD 1999 cup.

    The goal is to predict whether or not an SMTP connection is anomalous or not.
    The dataset only contains 2,211 (0.4%) positive labels.

    Parameters:
        data_home: The directory where you wish to store the data.
        verbose: Whether to indicate download progress or not.

    References:
        1. [SMTP (KDDCUP99) dataset](http://odds.cs.stonybrook.edu/smtp-kddcup99-dataset/)

    """

    def __init__(self, data_home=None, verbose=True):
        super().__init__(
            n_samples=95_156,
            n_features=3,
            category=base.BINARY_CLF,
            url='https://maxhalford.github.io/files/datasets/smtp.zip',
            data_home=data_home,
            verbose=verbose
        )

    def _stream_X_y(self, directory):
        return stream.iter_csv(
            f'{directory}/smtp.csv',
            target='service',
            converters={
                'duration': float,
                'src_bytes': float,
                'dst_bytes': float,
                'service': int
            }
        )
