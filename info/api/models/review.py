import graphene


class Review(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
