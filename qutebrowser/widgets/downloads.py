# Copyright 2014 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""The ListView to display downloads in."""

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListView, QSizePolicy

from qutebrowser.models.downloadmodel import DownloadModel


class DownloadView(QListView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.setFlow(QListView.LeftToRight)
        self._model = DownloadModel()
        self._model.rowsInserted.connect(self.updateGeometry)
        self._model.rowsRemoved.connect(self.updateGeometry)
        self.setModel(self._model)
        self.setWrapping(True)

    def minimumSizeHint(self):
        return self.sizeHint()

    def sizeHint(self):
        height = self.sizeHintForRow(0)
        if height != -1:
            return QSize(0, height + 2)
        else:
            return QSize(0, 0)
