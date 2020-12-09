from django import template
from django.utils.translation import gettext, pgettext

register = template.Library()


@register.filter
def yes_no(value):
    """Converts boolean to yes or no string"""
    if not value:
        return gettext('Unknown')
    # Python doesn't have a ternary, so we rely on
    # type coercion to turn False into 0 and True
    # into 1, and using that as list index.
    return (gettext('No'), gettext('Yes'))[value]


@register.filter
def extended_yes_no(value):
    """Converts quad-state to human readable string"""
    if value == 'U':
        return gettext('Unknown')
    if value == 'NA':
        return gettext('N/A')
    if value == 'Yes':
        return gettext('Yes')
    if value == 'No':
        return gettext('No')
    return value


@register.filter
def track_record(value):
    """
    effects localization for company track records. While it might
    seem easier to just return gettext(value), we want to be explicit
    about the possible options, and the context in which to apply
    this tag, rather than a generic "localize" tag.
    """
    if value == 'Great':
        return pgettext("This is a rating for a company's history concerning privacy", 'Great')
    if value == 'Average':
        return pgettext("This is a rating for a company's history concerning privacy", 'Average')
    if value == 'Needs Improvement':
        return pgettext("This is a rating for a company's history concerning privacy", 'Needs Improvement')
    if value == 'Bad':
        return pgettext("This is a rating for a company's history concerning privacy", 'Bad')
    return value
