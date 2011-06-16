from django.conf import settings

CACHE_PREFIX = getattr(settings, 'FLATBLOCKS_CACHE_PREFIX', 'flatblocks_')
AUTOCREATE_STATIC_BLOCKS = getattr(settings,
    'FLATBLOCKS_AUTOCREATE_STATIC_BLOCKS', False)

STRICT_DEFAULT_CHECK = getattr(settings,
    'FLATBLOCKS_STRICT_DEFAULT_CHECK', False)
STRICT_DEFAULT_CHECK_UPDATE = getattr(settings,
    'FLATBLOCKS_STRICT_DEFAULT_CHECK_UPDATE', False)
