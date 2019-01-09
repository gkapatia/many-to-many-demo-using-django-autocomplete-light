from dal import autocomplete

from colors.models import Color


class ColorAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Color.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

    def create_object(self, text):
        color = Color.objects.create(name=text, user=self.request.user)
        return color
