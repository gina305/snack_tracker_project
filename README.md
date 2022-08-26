Feature Tasks and Requirements
Model
* create snack_tracker_project project
  * This will involve some preliminary steps.
  * Review previous class lab for details.
* create snacks app
* Add snacks app to project
* create Snack model
  * make sure it extends from proper base class
  * add name as a CharField with maximum length of 64 characters.
  * add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
    * from django.contrib.auth import get_user_model
  * add description TextField
* add model to admin
* modify Snack model have user friendly display in admin
* create migrations and migrate data
* create a super user
* run development server
* Add a few snacks via Admin panel
* create another user and more snacks via Admin panel
* confirm that snacks behave as expected with proper name, purchaser and description.
* Looks like your model in good shape. Congrats!