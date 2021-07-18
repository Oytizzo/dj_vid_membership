# Model Architecture Planning

## Membership
    - slug
    - membership_type
    - price
    - stripe_plan_id

## UserMembership
    - User                  (OneToOneField to default user)
    - stripe_customer_id
    - membership            (foreignkey to Membership)

## Subscription
    - user_membership       (foreignkey to UserMembership)
    - stripe_subscription_id
    - active

## Course
    - slug
    - title
    - description
    - allowed_membership    (ManyToMany to Membership)

## Lesson
    - slug
    - position
    - title
    - description
    - course                (foreignkey to Course)
    - video
    - thumbnail
