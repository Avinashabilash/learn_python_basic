import random
googled_search={
    "google":7225678,
    "amazon":921345678,
    "modi":89764765,
    "family_guy":1220000,
    "morocco":823000,
    "isis":1830000,
    "youtube":226000000,
    "amazon":124000000,
    "facebook":124000000,
    "weather":831000000,
    "subway":409000
}
google_named=list(googled_search.keys())
#print(googled_search.keys())
while True:
    name1=random.choice(google_named)
    name2=random.choice(google_named)
    search1 = googled_search[name1]
    #print(googled_search[name1])
    search2 = googled_search[name2]
    choice=input(f"compare {name1} or {name2} whoich one is googled more time?:")
    correct_answer= name1 if search1 >search2 else name2
    if choice==correct_answer:
        print("your winner")
    else:
        print("lose")
        
    play_again=input("do  u wanna  play again(yes/no)")
    if play_again=="n".lower():
        break










#choice=input("compare google or amazon").lower()
#if amazon > google:
#    correct_answer="amazon"
#else:
#    correct_answer="google"


#if choice==correct_answer:
#    print("your winner")
    
#else:
  #  print("lose")
