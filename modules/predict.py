# <YOUR_IMPORTS>
import dill


def predict():
    # <YOUR_CODE>
    with open('file', 'rb') as f:
        model = dill.load(f)

    pass


if __name__ == '__main__':
    predict()
