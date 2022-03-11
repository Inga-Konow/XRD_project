from pathlib import Path
import numpy
from matplotlib import pyplot

DATA = Path(__file__).parent / 'data'
IMG = Path(__file__).parent / 'img'

def load_data():
    '''
    Load our datasets
    '''
    set1 = DATA / 'set1.txt'
    set2 = DATA / 'set2.txt'
    return numpy.loadtxt(set1), numpy.loadtxt(set2)

def plot_data(m, fname, title):
    '''
    Supersimple plotting code
    '''
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(r'$2\theta$')
    ax.set_ylabel('Intensity')
    ax.grid()
    ax.plot(m[:,0], m[:,1])
    fig.show()
    fig.savefig(fname, format='svg')

if __name__ == '__main__':
    set1, set2 = load_data()
    plot_data(set1, IMG / 'set1.svg', 'Crystaline Si')
    plot_data(set2, IMG / 'set2.svg', 'Unknown sample')
