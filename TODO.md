# MedChain ToDo

### Column Name
- [ ] Debug patient's new_share POST method  
  - current request example:
  ```json
  {
    "patient_id":"bbc65dd047ef4048aa12f34e2f72e727",
    "clinic_id" : "d12062c635c64f46b4c71f95e0ff2c33",
    "validity_duration": 5,
    "prescription_id" : "ST3/E/kFistvR+njqykXeX8T9vCbaF2azCqJ0pDnir3MRcpho7iBTU1NLLoPM2fBvemHnQDaRuv4bQKQJC+HZU+VZT0mFX2EdEsX8oSoA/gnOGJUIEfr0jarcVltmsOjadnmBEU5egQKwRiFYyIBRlAHFIozIzhNxG19pIqFuvziliqOG3FqX4ODDeQnW/EEwJQakTGjZCuQy+I7bQOsbUZR4A5gkW3pscp1mymZ2blH/VaPNIlm1o0B6YqYBNprzG9PN7Mf5QrH38RjkDqS/dIS0sCL/LJQIslIUk3sGMk08/3x8bPGxe8TwKHuQRmnTxlcx862T/oGBsoNvvEDwg=="
  }
  ```
  - Query: ?private_key=*[patient_private_key_value]*
- [ ] Test and Debug pharmacy's new_pruchase POST method
