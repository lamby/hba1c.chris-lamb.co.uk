from django_enumfield import enum

class StageEnum(enum.Enum):
    LANDING     = 10
    NAME        = 20
    RESULTS     = 30
    GENERATE    = 40
    PREVIEW     = 50
    DOWNLOAD    = 60

    labels = {
        LANDING: "Landing",
        NAME: "Name entry",
        RESULTS: "Results entry",
        GENERATE: "Generate PDF",
        PREVIEW: "Preview",
        DOWNLOAD: "Download",
    }

    urlconfs = {
        LANDING: 'static:landing',
        NAME: 'reports:name',
        RESULTS: 'results:view',
        GENERATE: 'reports:generate',
        PREVIEW: 'reports:preview:view',
        DOWNLOAD: 'reports:download',
    }

    @classmethod
    def urlconf(cls, val):
        enum = cls.get(val)

        return cls.urlconfs[enum.value]
