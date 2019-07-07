import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.metrics import auc, roc_curve, confusion_matrix

def draw_confusion_matrix(y_true, y_predicted, class_labels=None, ax=None):
    """Draws a confusion matrix for classifier predictions.
    
    Args:
        y_true (array-like): True class labels
        y_predicted (array-like): Predicted class labels
        class_labels (dict-like, optional): Specify alternative names for each class to use for axis labels
        ax (Matplotlib.Axes, optional): The axes on which to draw the confusion matrix
        
    Returns:
        ax (Matplotlib.Axes): The axes containing the confusion matrix.
    """
    
    if ax is None:
        ax = plt.gca()
    
    cm = pd.DataFrame(confusion_matrix(y_true, y_predicted)).T
    
    if class_labels is not None:
        cm.rename(class_labels, axis='index', inplace=True)
        cm.rename(class_labels, axis='columns', inplace=True)
    
    sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', square=True, linewidths=0.1, linecolor='k', cbar_kws={'shrink': 0.75}, annot_kws={'size': 20}, ax=ax)
    ax.set_ylabel('Predicted class label')
    ax.set_xlabel('True class label')

    return ax

def draw_roc_curve(y_true, y_score, annot=True, name=None, ax=None):
    """Draws a ROC (Receiver Operating Characteristic) curve using class rankings predicted by a classifier.
    
    Args:
        y_true (array-like): True class labels (0: negative; 1: positive)
        y_score (array-like): Predicted probability of positive-class membership
        annot (bool, optional): Whether to create and add a label to the curve with the computed AUC
        name (str, optional): Name of the curve to add to the AUC label
        ax (Matplotlib.Axes, optional): The axes on which to draw the ROC curve
        
    Returns:
        ax (Matplotlib.Axes): The axes containing the ROC curve
    """
    
    fpr, tpr, _ = roc_curve(y_true, y_score)
    
    if ax is None:
        ax = plt.gca()
    
    # Add a label displaying the computed area under the curve
    if annot:
        roc_auc = auc(fpr, tpr)
        if name is not None:
            label = f'{name} AUC = {roc_auc:.3f}'
        else:
            label = f'AUC = {roc_auc:.3f}'
    else:
        label=None
    
    ax.plot(fpr, tpr, label=label)
    ax.set_xlabel('False positive rate')
    ax.set_ylabel('True positive rate')
    ax.legend(loc='best')
    
    return ax
