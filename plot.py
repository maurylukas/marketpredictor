# Start of imports
import matplotlib.pyplot as plt
# End of imports

# Start of functions


def plot_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Mean Square Error - Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='best')
    plt.show()

    plt.plot(history.history['mae'])
    plt.plot(history.history['val_mae'])
    plt.title('Model loss')
    plt.ylabel('Mean Absolute Error')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='best')
    plt.show()

    return None


# End of functions

'''
TESTING
  python main.py

DEPLOYMENT STEPS & CLI COMMANDS:
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
