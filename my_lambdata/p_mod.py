import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix

def confusionlabels(self,pipeline,X_test,y_test, values_format, display_labels,cmap) :
    disp = plot_confusion_matrix(pipeline,X_test, y_test, values_format='.0f', display_labels=labels_names, cmap=cmap)
    disp.ax_.set_title(title)
    return plt.show()

