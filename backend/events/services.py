
from django.db import transaction
from django.core.exceptions import ValidationError

from .models import Event


@transaction.atomic
def create_event(
    argahemjeeniidugaar,
    baiguullagiindugaar,
    angilaliindugaar,
    tulwiindugaar,
    garchig,
    tailbar,
    bairshil,
    ehleh_ognoo,
    duusah_ognoo,
    oroltsohchdiin_too,
):
    if not argahemjeeniidugaar:
        raise ValidationError("Арга хэмжээний дугаар оруулна уу.")

    if not baiguullagiindugaar:
        raise ValidationError("Байгууллагыг сонгоно уу.")

    if not angilaliindugaar:
        raise ValidationError("Ангиллыг сонгоно уу.")

    if not tulwiindugaar:
        raise ValidationError("Төлөвийг сонгоно уу.")

    if not garchig or not garchig.strip():
        raise ValidationError("Арга хэмжээний гарчиг оруулна уу.")

    if not bairshil or not bairshil.strip():
        raise ValidationError("Байршил оруулна уу.")

    if ehleh_ognoo is None or duusah_ognoo is None:
        raise ValidationError("Эхлэх болон дуусах огноог оруулна уу.")

    if duusah_ognoo <= ehleh_ognoo:
        raise ValidationError(
            "Дуусах огноо эхлэх огнооноос хойш байх ёстой."
        )

    if (
        isinstance(oroltsohchdiin_too, bool)
        or not isinstance(oroltsohchdiin_too, int)
        or oroltsohchdiin_too < 0
    ):
        raise ValidationError(
            "Оролцогчдын тоо 0 буюу түүнээс их бүхэл тоо байна."
        )

    event = Event(
        argahemjeeniidugaar=argahemjeeniidugaar,
        baiguullagiindugaar=baiguullagiindugaar,
        angilaliindugaar=angilaliindugaar,
        tulwiindugaar=tulwiindugaar,
        garchig=garchig.strip(),
        tailbar=tailbar,
        bairshil=bairshil.strip(),
        ehleh_ognoo=ehleh_ognoo,
        duusah_ognoo=duusah_ognoo,
        oroltsohchdiin_too=oroltsohchdiin_too,
    )

    event.full_clean()
    event.save()

    return event
