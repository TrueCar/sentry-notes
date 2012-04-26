from sentry.plugins import Plugin, register

from django import forms
from django.core.context_processors import csrf

from .models import Notation, Group

__version__ = "0.1"


class NotesPlugin(Plugin):
    title = 'Notes'
    version = __version__
    author = 'TrueCar Dev Team'
    author_url = 'https://github.com/TrueCar/sentry-notes'

    def panels(self, request, group, panel_list, **kwargs):
        panel_list.append((self.get_title(), self.get_url(group)))
        return panel_list

    def view(self, request, group, **kwargs):
        try:
            note = group.notation
        except Notation.DoesNotExist:
            note = Notation(group=group)

        if request.method == 'POST' and request.user.is_authenticated():
            note.note = request.POST['note']
            note.modified_by = request.user
            note.save()

        return self.render('sentry_notes/index.html', {
                'notation': note,
            })

    def before_events(self, request, event_list, **kwargs):
        # Called before tags are applied
        notes = Notation.objects.filter(group__in=event_list)
        self._tagged = set(x.group_id for x in notes if x.note.strip())

    def tags(self, request, group, tag_list, **kwargs):
        # "group" can be an Event, not just a Group
        if isinstance(group, Group) and group.pk in self._tagged:
            tag_list.append(u"\u270D")

        return tag_list


register(NotesPlugin)
