def enorde(i):
  alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  def encode():
    ie=input("Enter a message:\n").lower()
    ish=int(input("Enter shift number:\n"))
    emsg=''
    for x in list(ie):
      emsg=emsg+alp[alp.index(x)+ish]
    print(emsg)
    return
  def decode():
    id=input("Enter the message:\n").lower()
    idsh=int(input("What was the shift number:\n"))
    dmsg=''
    for x in list(id):
      dmsg=dmsg+alp[alp.index(x)-idsh]
    print(dmsg)
    return
  if i.lower()=='encode':
    encode()
  if i.lower()=="decode":
    decode()
enorde(input("'Encode' or 'decode' message?\n"))
