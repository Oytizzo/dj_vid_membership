# Model Architecture Planning

## Membership
    - slug
    - membership_type
    - price
    - stripe_plan_id

## Profile
    - User               (foreignkey to default user)
    * uncomplete

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
