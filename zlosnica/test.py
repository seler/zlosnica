import sys

from PyQt4.QtGui import (QApplication, QColumnView, QFileSystemModel,
                         QSplitter, QTreeView)
from PyQt4.QtCore import QDir, Qt


class Model(QFileSystemModel):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Splitter to show 2 views in same widget easily.
    splitter = QSplitter()
    # The model.
    model = Model()
    # You can setRootPath to any path.
    model.setRootPath(QDir.rootPath())
    # Create the view in the splitter.
    view = QTreeView(splitter)
    # Set the model of the view.
    view.setModel(model)
    # Set the root index of the view as the user's home directory.
    view.setRootIndex(model.index(QDir.homePath()))
    # Show the splitter.
    splitter.show()
    # Maximize the splitter.
    splitter.setWindowState(Qt.WindowMaximized)
    # Start the main loop.
    sys.exit(app.exec_())
