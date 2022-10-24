# Quiz Game

print('Welcome to the Quiz Game.')
print('Pick a Catagory')
catagory = input('Computers or Cars? ' ).lower()
score = 0
num_questions = 0

if catagory == 'computers':
    print('Welcome to the Computers Quiz.')
    print('You will be asked a number of Computer related Questions.\nLets see how many you get right.')
    question = input('What does CPU stand for? ').lower()
    num_questions += 1
    if question == 'central processing unit':
        print('Correct.')
        score += 1
    else:
        print('Incorrect. CPU stands for Central Processing Unit.')

    question = input('What does GPU stand for? ').lower()
    num_questions += 1
    if question == 'graphics processing unit' or question == 'graphical processing unit':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. GPU stands for Graphics Processing Unit.')

    question = input('What does RAM stand for? ').lower()
    num_questions += 1
    if question == 'random access memory':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. RAM stands for Random Access Memory.')

    question = input('What does PSU stand for? ').lower()
    num_questions += 1
    if question == 'power supply unit' or question == 'power suply':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. PSU stands for Power Supply Unit.')

    question = input('What does ROM stand for? ').lower()
    num_questions += 1
    if question == 'read only memory' or question == 'read-only memory':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. ROM stands for Read Only Memory.')

    question = input('What does MAC Address stand for? ').lower()
    num_questions += 1
    if question == 'media access control address' or question == 'media access control':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. MAC Address stands for Media Access Control Address.')

    question = input('What does PC stand for? ').lower()
    num_questions += 1
    if question == 'personal computer':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. PC stands for Personal Computer.')

    question = input('What does BIOS Address stand for? ').lower()
    num_questions += 1
    if question == 'basic input output services' or question == 'basic input output service' or question == 'basic input-output services'or question == 'basic input-output service':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. BIOS stands for Basic Input-Output Services.')

    question = input('What does CD stand for? ').lower()
    num_questions += 1
    if question == 'compact disc':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. CD stands for Compact Disc.')

    question = input('What does DIMM stand for? ').lower()
    num_questions += 1
    if question == 'dual in-line memory module' or question == 'dual inline memory module':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. DIMM stands for Dual Inline Memory Modual.')       

    question = input('What does DVD stand for? ').lower()
    num_questions += 1
    if question == 'digital versatile disc':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. DVD stands for Digital Versatile Disc.')

    question = input('What does HDD stand for? ').lower()
    num_questions += 1
    if question == 'hard drive' or question == 'hard disc drive' or question == 'hard disc':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. HDD stands for Hard Disc Drive.')

    question = input('What does HDMI stand for? ').lower()
    num_questions += 1
    if question == 'high-definition multimedia interface' or question == 'high definition multimedia interface':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. HDMI stands for High-Definition Multimedia Interface.')

    question = input('What does LAN stand for? ').lower()
    num_questions += 1
    if question == 'local area network':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. LAN stands for Local Area Network.')

    question = input('What does LUN stand for? ').lower()
    num_questions += 1
    if question == 'logical unit number':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. LUN stands for Logical Unit Number.')

    question = input('What does NIC stand for? ').lower()
    num_questions += 1
    if question == 'network interface card':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. NIC stands for Network Interface Card.')

    question = input('What does SSD stand for? ').lower()
    num_questions += 1
    if question == 'solid state drive':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. SSD stands for Solid State Drive.')

    question = input('What does UPS stand for? ').lower()
    num_questions += 1
    if question == 'uninterrupted power supply' or question == 'uninterruptible power supply':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. UPS stands for Uninterruptible or Uninterrupted Power Supply.')

    question = input('What does USB stand for? ').lower()
    num_questions += 1
    if question == 'universal serial bus':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. USB stands for Universal Serial Bus.')

    question = input('What does WAN stand for? ').lower()
    num_questions += 1
    if question == 'wide area network':
       print('Correct.')
       score += 1
    else:
       print('Incorrect. WAN stands for Wide Area Network.')

    print('Your score on the Computer Quiz is: '+ str(int((score/num_questions) *100))+'% \n You got ',score,' out of', num_questions, 'correct.')
    quit()    

if catagory == 'cars':
    print('Cars Questions have not been created yet.')
    quit()

else:
    print('You did not choose computers or cars.')
