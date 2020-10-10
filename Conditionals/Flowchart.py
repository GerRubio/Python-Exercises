# Create a flow with conditionals to reach the expected result.

can_fly_question = int(input('Can fly? 1 = yes: '))

if can_fly_question == 1:
    print('Can fly.')
    is_human_question = int(input('Is human? 1 = yes: '))

    if is_human_question == 1:
        print('Is human.')
        has_mask_question = int(input('Has mask? 1 = yes: '))

        if has_mask_question == 1:
            print('Ironman.')
        else:
            print('Captain Marvel.')
    else:
        print('Is not human.')
        has_mask_question = int(input('Has mask? 1 = yes: '))

        if has_mask_question == 1:
            print('Ronan Accuser.')
        else:
            print('Vision.')
   
elif can_fly_question == 0:
    print('Can not fly.')
    is_human_question = int(input('Is human? 1 = yes: '))

    if is_human_question == 1:
        print('Is human.')
        has_mask_question = int(input('Has mask? 1 = yes: '))

        if has_mask_question == 1:
            print('Spiderman.')
        else:
            print('Hulk.')
    else:
        print('Is not human.')
        has_mask_question = int(input('Has mask? 1 = yes: '))

        if has_mask_question == 1:
            print('Black Bolt.')
        else:
            print('Thanos.')