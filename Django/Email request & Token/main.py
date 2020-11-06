@login_required()
def deposit_detial(request, request_id):
    try:
        current_site = get_current_site(request)
        # email confirmation
        current_site = get_current_site(request)
        subject = ('Confirm password change from SmsBaseApp')
        message = render_to_string('diposit/deposit_template_request.html', {
            'user': request_detial.user,
            'domain': current_site,
            'rid': urlsafe_base64_encode(force_bytes(request_detial.pk)),
            # 'uid': urlsafe_base64_encode(force_bytes(request_detial.user.pk)),
            'token': account_activation_token.make_token(request_detial.user), # Use Request make Token
            'date': urlsafe_base64_encode(force_bytes(datetime.now().strftime('%y%m%d'))),
            'time': urlsafe_base64_encode(force_bytes(datetime.now().strftime('%H%M'))),
        })
        # ส่ง Email ไปยังผู้ฝาก
        request_detial.user.email_user(subject, message)
        message_header = _('Create BBH Code Success.')
        message_detail = _('Sent Email to User.')
        message_header_json = str(message_header)
        message_detail_json = str(message_detail)
        request.session['sm_value'] = {'message_header': message_header_json,
                                       'message_detail': message_detail_json,
                                       'type': 'error',
                                       'displaytime': '5'}
        request.session['goto'] = '/SmsBackEnd/homedeposit/'
        return redirect('/Users/status_message/')
    except Exception as e:  # contains my own custom exception raising with custom messages.
        return HttpResponseServerError(e)
    finally:
        print('=== end funtion manegeDiposit ===')

def appecpt_deposit_activate(request, ridb64, token, date, time):
    email_expired = 43200 # 43200 Minute = 30 days
    try:
        rid = force_text(urlsafe_base64_decode(ridb64))
        udi = Request_Diposit_ID.objects.get(pk=rid)
        user = User.objects.get(pk=udi.user.pk)
        date = force_text(urlsafe_base64_decode(date))
        time = force_text(urlsafe_base64_decode(time))
        dt = datetime.strptime(date + time, '%y%m%d%H%M')
        diff_dt = datetime.now() - dt
        diff_dt_minute = (diff_dt.days * 86400 + diff_dt.seconds)/60
        
        # 
        # return redirect('/SmsBackEnd/accept/deposit/request/{}'.format(ridb64))
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    
    form_Diposit_id = Form_Diposit.objects.filter(rquest_diposit = rid)

    # Check User Accept
    accepted = True
    for deposit in form_Diposit_id:
        status_Diposit = Status_Diposit.objects.filter(form_Diposit = deposit.pk)
        if (status_Diposit[0].status_user) == 0:
           accepted = False

    # request correct
    if user is not None  and account_activation_token.check_token(user, token) and (accepted == False) and (diff_dt_minute <= email_expired):
        # print("💖")
        # print("request correct")
        # print("💖")
        request.session['reset_password'] = {'user': udi.user.pk,
                                             'dt': datetime.now().strftime('%y%m%d%H%M')}
        return redirect('/SmsBackEnd/accept/deposit/request/{}'.format(ridb64))

    # request expired
    elif user is not None and account_activation_token.check_token(user, token) and (accepted == False) and diff_dt_minute > email_expired:
        # print("💖")
        # print("equest expired")
        # print("💖")
        message_header = _('Accept Deposit.')
        message_detail = _('Time over 30 days.')
        message_header_json = str(message_header)
        message_detail_json = str(message_detail)
        request.session['sm_value'] = {'message_header': message_header_json,
                                       'message_detail': message_detail_json,
                                       'type': 'error',
                                       'displaytime': '5'}
        request.session['goto'] = '/'
        return redirect('/Users/status_message/')

    elif accepted == True:
        # print("💖")
        # print("accepted == True")
        # print("💖")
        message_header = _('Accept Deposit.')
        message_detail = _('You Deposit is Accepted.')
        message_header_json = str(message_header)
        message_detail_json = str(message_detail)
        request.session['sm_value'] = {'message_header': message_header_json,
                                       'message_detail': message_detail_json,
                                       'type': 'error',
                                       'displaytime': '5'}
        request.session['goto'] = '/'
        return redirect('/Users/status_message/')

    else :
        # print("💖")
        # print("Token Error")
        # print("💖")
        # Token Error
        message_header = _('Accept Deposit failed.')
        message_detail = _('Please contact officer.')
        message_header_json = str(message_header)
        message_detail_json = str(message_detail)
        request.session['sm_value'] = {'message_header': message_header_json,
                                       'message_detail': message_detail_json,
                                       'type': 'error',
                                       'displaytime': '5'}
        request.session['goto'] = '/'
        return redirect('/Users/status_message/')
