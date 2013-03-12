#!/usr/bin/env python

import sys
import gtk
import appindicator

from datetime import date, timedelta, datetime



PING_FREQUENCY = 1 # seconds

class LossCounter:
    def __init__(self):
        self.ind = appindicator.Indicator("time-difference-indicator",
                                           "",
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_label("0")
        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        self.update()
        gtk.timeout_add(PING_FREQUENCY * 1000, self.update)
        gtk.main()

    def quit(self, widget):
        sys.exit(0)

    def update(self):
        start = datetime(2013,1,1,0,0,0)
        end = datetime.now()
        time_diff = end - start

        loss = time_diff.total_seconds()

        self.ind.set_label('second: '+format(loss, ',.0f'))
        return True


if __name__ == "__main__":
    indicator = LossCounter()
    indicator.main()

