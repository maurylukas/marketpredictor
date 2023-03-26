# Start of imports
import matplotlib.pyplot as plt
# End of imports

# Start of functions


def plot_loss(history):
    """
    Function to plot model loss and metric on both train and validation datasets.
    """
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Mean Square Error - Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='best')
    plt.show()

    plt.plot(history.history['mae'])
    plt.plot(history.history['val_mae'])
    plt.title('Model metric')
    plt.ylabel('Mean Absolute Error - Metric')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='best')
    plt.show()

    return None


# End of functions

'''
INSTRUCTIONS TO DEPLOY THROUGH VISUAL STUDIO CODE:
    You have to run a series of commands on a Terminal and hit Enter.
    You may have to open a second Terminal console in order to complete all steps.

A) TESTING:
    python main.py

B) DEPLOYMENT STEPS & CLI COMMANDS:
1. BUILD:
    prefect deployment build main.py:price_pipeline --name price_pipeline --interval 300
2. APPLY:
    prefect deployment apply price_pipeline-deployment.yaml
3. LIST DEPLOYMENTS:
    prefect deployment ls
4. RUN:
    prefect deployment run "Price pipeline/price_pipeline"
5. ORION GUI:
    prefect orion start
6. AGENT START:
    prefect agent start --work-queue "default"
7. EXIT:
Hold CTRL and press C
'''
