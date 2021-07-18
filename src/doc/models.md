# Model Architecture Planning

## Membership
    - slug
    - membership_type
    - price
    - stripe_plan_id

## Profile
    - User                  (OneToOneField to default user)
    - stripe_customer_id
    - membership            (foreignkey to Membership)

## Subscription
    * uncomplete

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
