# Method 1
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    email_dict = {}
    for i in range(len(person)):
        id = person['id'][i]
        email = person['email'][i]

        if email in email_dict:
            if email_dict[email] > id:
                email_dict[email] = id
        else:
            email_dict[email] = id
    # print(email_dict)

    keep_id = set(email_dict.values())
    # print(keep_id)
    person.drop(person[~person['id'].isin(keep_id)].index, inplace = True)


# Method 2
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # first we need to sort the data by id scending so that we capture the min id in case of duplicates
    person.sort_values(by = 'id', inplace = True)
    person.drop_duplicates(subset = 'email', inplace = True)

    # print(person)


# Method 3
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    keep_id = person.groupby('email')['id'].transform('min')

    person.drop(person[~person['id'].isin(keep_id)].index, inplace = True)