# Diary Software
Lets create a diary Software that allows you to :
1. write notes for any day
2. decide if other users can make a comment on your notes
3. your diary note can have a shareable id

## tables
1. UserTable, you can use the existing user table from class projects, besure to include email field and date of birth

2. CommentTable, this should have the following columns
message TextField
author ForeignKey ( you need to know who made the comment)
is_delete BooleanField
created_at DateTimeField
upddated_at DateTimeField


3. DiaryNoteTable (notes for your diary), this should have the following columns
title CharField
description TextField
link_id CharField (shareable id to friends, anyone with this id commen t on your diary note)
author ForeignKey ( you need to know who made the diary note)
comment ForeignKey ( you need to see the comments attached to the diary note)
is_accepting_comments BooleanField ( to know if a diary can accept comments)
is_delete BooleanField
created_at DateTimeField
upddated_at DateTimeField


- Build necessary apps you will need
- Build models for the required tables
- Build urls and views
- Write tests
- Attach forms where necessary (especially where we need to make comments)
- Attach templates