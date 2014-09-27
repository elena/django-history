# -*- coding: utf-8 -*-
import reversion
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(_('Title'), max_length=256, null=True, blank=True)
    colour = models.CharField(_('Color'), max_length=7, null=True, blank=True,
                              help_text = "Arbitrary colour for presentation")
    slug = models.SlugField(max_length=64)

    class Meta(object):
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

reversion.register(Category)


class Talk(models.Model):
    is_live = models.BooleanField(_("Live"), default=True)
    event = models.ForeignKey('events.Event', null=True, blank=True)
    speakers = models.ManyToManyField('lore.Speaker')
    tags = TaggableManager(_('Tags'))
    slug = models.SlugField(max_length=64)
    view_count = models.IntegerField(_('View count'))


    categories = models.ManyToManyField('lore.Category',
                                        help_text="Curated and official 'categorisation' eg.: ORM; Optimization.")

    date_delivered = models.DateTimeField(_('Date delivered'),
                                          help_text="The date the talk was actually given/delivered/presented.")

    """ Detail from conference website """
    title = models.CharField(_('Title'), max_length=256, null=True, blank=True)
    abstract = models.TextField(_('Abstract'), null=True, blank=True)
    speaker_bio = models.TextField(_('Speaker bio'), null=True, blank=True)
    conference_url = models.URLField(_('Conference url'), null=True, blank=True)
    language = models.TextField(_('Language'), null=True, blank=True)

    # """ Detail from PyVideo """
    pyvideo_pk = models.IntegerField(_('PyVideo pk'), unique=True,
                                     null=True, blank=True)
    pyvideo_title = models.TextField(_('PyVideo title'), max_length=256,
                                     null=True, blank=True)
    pyvideo_summary = models.TextField(_('PyVideo summary'),
                                       null=True, blank=True)
    pyvideo_content = models.TextField(_('PyVideo content'),
                                       null=True, blank=True)
    pyvideo_tags = models.TextField(_('PyVideo tags'),
                                    null=True, blank=True)
    pyvideo_source_url = models.URLField(_('PyVideo source url'),
                                        null=True, blank=True)
    pyvideo_video_url = models.URLField(_('PyVideo hosted url'),
                                        null=True, blank=True)
    pyvideo_copyright = models.CharField(_('PyVideo copyright'), max_length=256,
                                         null=True, blank=True)

    # """ Detail from Youtube """
    youtube_id = models.CharField(_('Youtube id'), max_length=32, unique=True,
                                  null=True, blank=True)
    youtube_channel_id = models.CharField(_('Youtube channel id'),
                                          max_length=32, null=True, blank=True)
    youtube_title = models.TextField(_('Youtube title'), max_length=256,
                                     null=True, blank=True)
    youtube_summary = models.TextField(_('Youtube summary'),
                                       null=True, blank=True)
    youtube_content = models.TextField(_('Youtube content'),
                                       null=True, blank=True)
    youtube_views = models.IntegerField(_('Youtube views'),
                                        null=True, blank=True)
    youtube_likes = models.IntegerField(_('Youtube likes'),
                                        null=True, blank=True)
    youtube_duration = models.IntegerField(_('Youtube duration'),
                                        null=True, blank=True)
    youtube_thumbnail = models.URLField(_('Youtube thumbnail'),
                                        null=True, blank=True)
    youtube_copyright = models.CharField(_('Youtube copyright'), max_length=256,
                                         null=True, blank=True)

    objects = querysets.TalkManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('talks:talk_detail', kwargs={'slug': self.slug})

reversion.register(Talk)


class Speaker(models.Model):
    """ There should nearly certainly should be a separate module for speakers.

    But not looking to replace any existing resources out there, just point to them.
    """
    full_name = models.CharField(_('Full name'), max_length=128)
    prenom = models.CharField(_('Prenom'), max_length=64, blank=True, null=True,
                              help_text="Name for casual reference.")
    slug = models.SlugField(max_length=64, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    people = models.CharField(_('Django people username'), max_length=30,
                              blank=True, null=True)
    people_photo = models.URLField(_('Django people gravatar'),
                                   blank=True, null=True)
    people_finding = models.TextField(_('Django people details'),
                                      blank=True, null=True)

    pyvideo_pk = models.IntegerField(_('PyVideo pk'), blank=True, null=True,
                                     help_text="ID number used by PyVideo")

    def __str__(self):
        if self.people:
            return "{0} ({1})".format(self.full_name, self.people)
        return self.full_name

    def get_absolute_url(self):
        return reverse('talks:speaker_detail', kwargs={'slug': self.slug})

    def get_people_url(self):
        return 'https://people.djangoproject.com/{0}'.format(self.people)

    def get_existing_speaker_by_full_name(self, full_name):
        speakers_names = [x.lower() for x in Speaker.objects.all().values_list('full_name', flat=True)]
        if full_name in speakers_names:
            speakers = Speaker.objects.filter(full_name__istartswith=full_name)
            if len(speakers) == 1:
                return speakers[0]
            elif len(speakers) == 0:
                return False
            elif len(speakers) > 1:
                raise Exception("{0} results found!".format(len(speakers)))

    def fetch_pyvideo_pk(self):
        """Connect to PyVideo website and scrape (or try to) PyVideo PK.
        """
        url = 'http://pyvideo.org/search?models=videos.video&q={0}'.format(self.full_name.replace(" ", "+"))
        soup = BeautifulSoup(requests.get(url).content)
        results = soup.findAll("a")
        if results:
            links = results[0].findAll('a')
        else:
            self.pyvideo_pk = None
            self.save()
            return None
        speakers_link = []
        for link in links:
            if link.get('href'):
                if 'speaker' in link.get('href'):
                    speakers_link.append(link.get('href'))
        if speakers_link:
            pk = speakers_link[0].split('/')[2]
            soup = BeautifulSoup(requests.get(self.get_pyvideo_url(pk)).content)
            if self.full_name in str(soup.findAll('h1')[0].contents):
                self.pyvideo_pk = pk
                self.save()
                return self.pyvideo_pk
            else:
                return pk, self.full_name, str(soup.findAll('h1')[0].contents)
                #raise Exception("The name isn't matching the number that the basic scraper found here: {0}".format(url))
        else:
            self.pyvideo_pk = None
            self.save()
        return None

    def get_existing_speaker_by_people(self, people_username):
        if people_username in Speaker.objects.all().values_list('people'):
            return Speaker.objects.get(people=people_username)
        else:
            return False

    def search_people_get_or_create_speaker(self, full_name):
        """Connect to Django People website and searches and scrapes for people
        details.

        Accepts `full_name` string, returns :py:dict: of search results.
        """
        url = 'https://people.djangoproject.com/search/?q={0}'.format(full_name.replace(" ", "+"))
        request = requests.get(url)
        soup = BeautifulSoup(request.content)
        vcards = soup.findAll("li", { "class" : "vcard" })
        if len(vcards) == 1:
            for vcard in soup.findAll("li", { "class" : "vcard" }):
                people_username = vcard.findAll("a", { "class" : "url fn n" })[0].attrs['href'].strip("/")
                if self.get_existing_speaker_by_people(people_username):
                    self = self.get_existing_speaker_by_people(people_username)
                self.people = people_username
                self.photo = soup.findAll("img", { "class" : "main photo" })[0].attrs['src']
                self.prenom = soup.findAll("span", { "class" : "given-name" })[0].renderContents()
                self.save()
        elif len(vcards) == 0:
            return False
        elif len(vcards) > 1:
            raise Exception("{0} results found! No records created."
                            "".format(len(vcards)))

    def fetch_people_details(self, people):
        """Connect to Django People website and scrape people details.
        """
        request = requests.get(self.get_people_url())
        soup = BeautifulSoup(request.content)
        try:
            services = soup.findAll("ul", { "class" : "services" })[0].contents
        except IndexError:
            return ''
        links = []
        for li in services:
            try:
                links.append(li.contents[0].attrs['href'])
            except: pass
        return '' if not services else '<br>'.join(links)


    def save(self, *args, **kwargs):
        super(Speaker, self).save(*args, **kwargs)

reversion.register(Speaker)