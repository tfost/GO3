import graphene
from graphene_django import DjangoObjectType

from band.models import Band, Assoc
from member.models import Member


class BandType(DjangoObjectType):
    class Meta:
        model = Band
        fields = ("name", "hometown", "creation_date")


class AssocType(DjangoObjectType):
    class Meta:
        model = Assoc
        fields = ("band", "member", "status")


class MemberType(DjangoObjectType):
    class Meta:
        model = Member
        fields = ("email", "username")


class Query(graphene.ObjectType):
    # all_bands = graphene.List(BandType)
    all_bands = graphene.List(AssocType)
    band_by_name = graphene.Field(
        BandType, name=graphene.String(required=True))
    all_members = graphene.List(MemberType)
    member_by_email = graphene.Field(
        MemberType, email=graphene.String(required=True))

    def resolve_all_bands(self, info):
        # get all assocs for the user in context
        user = info.context.user

        assocs = Assoc.objects.filter(member=user)
        # print("context: ", request.POST.items())
        if info.context.user.is_superuser:
            return Assoc.objects.all()
        elif not info.context.user.is_authenticated:
            return Assoc.objects.none()
        else:
            return assocs

    def resolve_band_by_name(self, root, name):
        try:
            return Band.objects.get(name=name)
        except Band.DoesNotExist:
            return None

    def resolve_all_members(self, root):
        return Member.objects.all()

    def resolve_member_by_email(self, root, email):
        try:
            return Member.objects.get(email=email)
        except Member.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
