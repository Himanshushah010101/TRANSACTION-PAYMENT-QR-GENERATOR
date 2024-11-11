
#pip install pillow 
#pip install qrcode

#(1) take users upi id as a input
#(2) url defind for each payment method
#(3) generate qrcode for each payment methods
#(4) generate qrcode save in image file
#(5) display qrcode by pillow module



import qrcode

#Taking UPI ID as a input
upi_id = input("Enter your upi id : ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#(i)pa = upi_id
#(ii)pn = recipient name
#(iii)am = amount
#(iv)cu = currency
#(v)tn = message after transaction

#Defining the payment url based on the upi id and the payment app
#you can modify these urls based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#create qr codes for each payment app?

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr code to image file?

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display the qr codes by install pillow library?

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

