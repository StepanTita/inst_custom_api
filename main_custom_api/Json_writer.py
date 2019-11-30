def put_user_data(user_data):
    col_names = ['profile pic', 'nums/length username', 'fullname words', 'nums/length fullname', 'name==username',
                 'description length', 'external URL', 'private', '#posts', '#followers', '#follows', 'fake', 'message']
    data_row = [int(user_data.no_avatar), user_data.nums_to_len_username, user_data.tokens_in_fullname,
                user_data.nums_to_len_fullname, int(user_data.name_equals_username),
                user_data.bio_len, int(user_data.has_external), int(user_data.is_private),
                user_data.posts_number, user_data.followers, user_data.follows, 'success']

    return dict(zip(col_names, data_row))
