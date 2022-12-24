# Using Medchain
## Creating the three main personas: Patient, Practitioner, and Pharmacy 
- The POST URL: http://localhost:8090/signup/new
### Examples for the request Body:  
1. Patient:
```json
{
    "persona":"patient",
    "name" : "pooya",
    "address" : "12345"
}
```
2. Practitioner:
```json
{
    "persona":"practitioner",
    "name" : "feri",
    "address" : "55555"
}
```
3- Pharmacy:
```json
{
    "persona":"pharmacy",
    "name" : "drugshop",
    "address" : "9999"
}
```
### Expected output for each request:
```json
{
    "client_id": "d12062c635c64f46b4c71f95e0ff2c33",
    "message": "client added",
    "private_key": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBaU1OM3g5RndkYW9kRklnNi8rVE1YMTVxQklQWHB6Wmg2cExEdlFTSE5xMG8rRlRTCjJHSHFWaGwzdkdhdnZPVHFaRm56bURySlY2bU5OYnlJZDYrSWEweU1IQzB3UUFZMUtKOTRGdnRtb0VEVk5MMDYKTCtyYzljWGFYeFFjV0kwUlc2M1lWNVhtOHFiQU8rUGYwbGRuNzZzZFBCWis5aC9kNkhnbXk0cW1IMXd5T043MwpvdjBiOStrMUVrUDBFUUl6L09GbGtzQ0NBUXE3UytlWWpLVzJYQ0liU2ZtYjlVdnltbytDYXBVRjV2MGpSL0lqCmd2NExJWFRMaGdKcEIwNUIwOFZvbXJCMTJyVmtJbUpQSjNsSFZUb2grOFFtWnJrTDBiU3RWdkJvejgvdFRuTDgKYjE3RThIc2RDRVU1ZlBkNml4SUpSOW9Jc0d4dnluYzNST3FySndJREFRQUJBb0lCQUVBZlljQkt4dzhzSVBGWgpCRXlwY2xjK3RiZUROMi83ZEFKZktLNHRldFljYnlxcjNxVzhsdm9pZTd6V2FveEd5azBkemJRd3ora3RvbnN3Cjk4MGgvSFRPa1p5K1pUS0hscElDM3ZQcmtJMFBpTWR1OTJLekhFR1JzQmJISDVrM0h3M2NueVJGc09CUlphMU8KNU1qQzJZVUtOaTFQb054MlNYMnZKQVZuN3dhaGJLTUNpS0NZTEJQMkpsZTRQZTVNM1ZFWkxvTTkwSDdmSm04cgpsK3lpY1ZlQXBWa0ZqWFI4RUdiREJEYk5ENjdpKzUwTnAxK3d1bVlpRGQxa2xNREhRclM0Qk5qM05TUENreTlwCkxNcEt3VC8xYUFtdnc0ams0ZUlxSk41VENlMTlVYzZvOWVRR0l3RFNqZkF5bG8wcnB4K2ptcUFKOTBIUmt6VVgKL3pZS0pWa0NnWUVBdU12Vm0rNnRjVi9BSGk3WlE3cnFSaURNQTY5OUQ2QVdNU1QvLzJ3TTNneHJJQ1pTcGxEbwpLakxka3BFa0d1VlhkZ2RwckZOT2p6QWJrZE5La3ZjS2o0MjJwaDE5c3dvNmFIdGVDV3o5ZklqMjIzSG1hNkpXCjlUMXBNNkdmSXR2UGZiMkFzbkFQWkV5QWQ4K0hqSDRJWjNUN3EwaXdRTTM2K2FMZ1IrS2RtdGtDZ1lFQXZYVzUKaEtzVDN3Zk1Tdmo1S1Q1eVlIMklHRmtYSGo1WmwzTkJzMHRHZGd0T2U1Yi85b2QwZTk3N3VTZnFXL3ZEanBXUwpsSk9Ec2JCclFBcjN4UFRWWWJ3enNpd2VIR25pQVJCUERuNEJtL0h2aFdGNU5la21YZnlJR2gxK0tRS00zWjl4CjROa2RjSUR3K3BwVll2dUtsWW9jZnk3cTNtS1FOazk4aWZ2Q3RmOENnWUVBcVpCbm5lQkJCK0hMSUNidXR3WkEKeHo1NjFQcm1yenErZ2pPb0x0QVBjb1JFbThodVdDdXZER0dHREdIZmxrcFFtWDJ0eWpEYXllcGpzY2dHQ3BwaAo5MTBhZG94aTliRHg3VU1lQTFvZHNuTGV5SGRYN2ZXVkF3eHBoclhMbHFuSlYyQldRZVV2U21Ja0UwdTYzZ0FiCmFBcmdqc2R3NnRYV2I4K3pLbUxYS09rQ2dZQWVJRHNZcW05bGRvTDRwUEJScTVsYVdIdXNpM1lPbkJGNDhKM1EKMmJaaGpOaTA5RVROT2FxL0M2enhPelNiM2NPeHgzemdYVGlDcDYvV0ppaFJ6RENsOHR3eGg2eGVEa1Flc1M0dworcjVjd3JLNGZkQmRUeTZIb1dFdTdlT2l0OElZZDRNUEl0YjRqYmhEMFFpa3phU3l0SnhsYU50MTh5eEZSb3hpCkVJTmNsd0tCZ0NFYWs3RmV3VTQ4OU53U3ZHZ2hET2Ftek4yV1djR3ZWeS9nYnJuUVZiZExYTVNxN2VCYWNxRk0KUjd0R3ovQllCcCtGcUJhRVlxb1Zxb0U0QVMvOWtlbEN6Mlh6ZUQ2Q3F5bXd6eE9XcHpVK3lkNE1ZU1BkUmlrNwpqaFpNRE5PdU5icFlrYnMxVlpUeGpuZDN6Q0RHb3FjelgrRFZRdFZlZDlTeWY5ZmpuTWlmCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t"
}
```
- The private key must be saved and kept safe by the client, as the program does not store the key and there is no other way to recover it.

## Verifying that the personas were created
- The GET URL: http://localhost:8090/signup/show
### Expected output for each request:
```json
{
    "clients": [
        {
            "address": "Ontario Tech University",
            "client_id": "5c1c382330c04ce0af1b0184e9ec9388",
            "name": "Central Authority",
            "persona_level": "CA",
            "public_key": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE5NkRNR21jSC9mRXFPcVFzNkg3MwpKOXNuaXF6TzJNTUhXN1FSWkV3OHFUbnloRDhxTjhvT1FFR21SR1BYVWRRRGpaSW9tM2h4WkFDb05TMndXdHNECnRQV29aTUkrRjAwTmRtY3BFUGhMVDloTWp3OG5iNW9ZS0dTUzhzVkNEQkxtelZvSC9FbmlucExSNTUyRGxXTzEKZWtodzNWNzRGL3BtOHBqM0RUbkVlUDVMWUtpOUgwQTZRcktpQ0hSVmFvYU1NV1RPRzlBZkxVY3BGSHFWdVovbwpDN0FRLzZFT2RhenBBN0ZDMk50S2hrMWNqTTJkRVA3TlNXaXVaSVZrdi9BSnVlckRrRUdZRlhLNEgxSUlKWm4xCnBOWHdwbDUyem96blR2NEpsRHVzOENHTW1DQWJUL3VZd1lNSitLZkpMd0JSQ1ZlclhRVHVHOXc2RWVYcVk1ckoKSFFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t"
        },
        {
            "address": "9999",
            "client_id": "d12062c635c64f46b4c71f95e0ff2c33",
            "name": "drugshop",
            "persona_level": "pharmacy",
            "public_key": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE5NkRNR21jSC9mRXFPcVFzNkg3MwpKOXNuaXF6TzJNTUhXN1FSWkV3OHFUbnloRDhxTjhvT1FFR21SR1BYVWRRRGpaSW9tM2h4WkFDb05TMndXdHNECnRQV29aTUkrRjAwTmRtY3BFUGhMVDloTWp3OG5iNW9ZS0dTUzhzVkNEQkxtelZvSC9FbmlucExSNTUyRGxXTzEKZWtodzNWNzRGL3BtOHBqM0RUbkVlUDVMWUtpOUgwQTZRcktpQ0hSVmFvYU1NV1RPRzlBZkxVY3BGSHFWdVovbwpDN0FRLzZFT2RhenBBN0ZDMk50S2hrMWNqTTJkRVA3TlNXaXVaSVZrdi9BSnVlckRrRUdZRlhLNEgxSUlKWm4xCnBOWHdwbDUyem96blR2NEpsRHVzOENHTW1DQWJUL3VZd1lNSitLZkpMd0JSQ1ZlclhRVHVHOXc2RWVYcVk1ckoKSFFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t"
        },
        {
            "address": "12345",
            "client_id": "bbc65dd047ef4048aa12f34e2f72e727",
            "name": "pooya",
            "persona_level": "patient",
            "public_key": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE5NkRNR21jSC9mRXFPcVFzNkg3MwpKOXNuaXF6TzJNTUhXN1FSWkV3OHFUbnloRDhxTjhvT1FFR21SR1BYVWRRRGpaSW9tM2h4WkFDb05TMndXdHNECnRQV29aTUkrRjAwTmRtY3BFUGhMVDloTWp3OG5iNW9ZS0dTUzhzVkNEQkxtelZvSC9FbmlucExSNTUyRGxXTzEKZWtodzNWNzRGL3BtOHBqM0RUbkVlUDVMWUtpOUgwQTZRcktpQ0hSVmFvYU1NV1RPRzlBZkxVY3BGSHFWdVovbwpDN0FRLzZFT2RhenBBN0ZDMk50S2hrMWNqTTJkRVA3TlNXaXVaSVZrdi9BSnVlckRrRUdZRlhLNEgxSUlKWm4xCnBOWHdwbDUyem96blR2NEpsRHVzOENHTW1DQWJUL3VZd1lNSitLZkpMd0JSQ1ZlclhRVHVHOXc2RWVYcVk1ckoKSFFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t"
        },
        {
            "address": "55555",
            "client_id": "ed3afc4482414b24a1088bdd88b66a4a",
            "name": "feri",
            "persona_level": "practitioner",
            "public_key": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE5NkRNR21jSC9mRXFPcVFzNkg3MwpKOXNuaXF6TzJNTUhXN1FSWkV3OHFUbnloRDhxTjhvT1FFR21SR1BYVWRRRGpaSW9tM2h4WkFDb05TMndXdHNECnRQV29aTUkrRjAwTmRtY3BFUGhMVDloTWp3OG5iNW9ZS0dTUzhzVkNEQkxtelZvSC9FbmlucExSNTUyRGxXTzEKZWtodzNWNzRGL3BtOHBqM0RUbkVlUDVMWUtpOUgwQTZRcktpQ0hSVmFvYU1NV1RPRzlBZkxVY3BGSHFWdVovbwpDN0FRLzZFT2RhenBBN0ZDMk50S2hrMWNqTTJkRVA3TlNXaXVaSVZrdi9BSnVlckRrRUdZRlhLNEgxSUlKWm4xCnBOWHdwbDUyem96blR2NEpsRHVzOENHTW1DQWJUL3VZd1lNSitLZkpMd0JSQ1ZlclhRVHVHOXc2RWVYcVk1ckoKSFFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t"
        }
    ],
    "length": 4
}
```

## Creating a prescription with the practitioner persona
- The POST URL: http://localhost:8090/prescription/new
- The input is used with a query that uses practitioner's private key as an example, to sign the prescription.
### Examples for the request Body:  
- Query: ?private_key=*[private_key_value]*
```json
{
    "practitioner_id":"34985a5d69cb450388c5ac6db1695b16",
    "patient_id" : "caa052b61ee54a048da1b46d427ef42b",
    "drugs" : ["cold", "skin"],
    "validity_duration": 5
}
```

## Using Selective-Endorsement to add the prescription to the MedChain
- The GET URL: http://localhost:8090/selective_endorsement
- The input is used with a query that uses a trusted client's private key as an example, to use the selective-endorsement.
- Query: ?private_key=*[private_key_value]*  
### Expected output example:
```json
{
    "hash_of_previous_block": "l/J9/hfxt+sKqvopaHa/iW8Lrn3wGjBYLxNXiSTEpL8=",
    "index": 1,
    "med_data": [
        {
            "data": {
                "encrypted_data": "3Bo+ZD4vXuOSjezYEFiF5poCoJlhd4XDh09QoTbEqo746n3tnLXixxzofPsN//so7e98W+y/ekKQAZStH6gbv5yN3ftfnwzBKHgCoYc9kF1G+ezmfqRGJvJkFn2qqXR/rsnHlM7h99QKOLa+kCY1CTKO31E24gWshmdZ5JaD38FZP1kxye1jRS48jSpyYXM0ZIFLj8HbnPFV9J0VbxJjy2LDJB0a3u/ToXqaoGwriFXi0w9fJqnusllLERGlbjprc8XU3wMygtqeVbH3wZW9C9Bp+tK3e9VotgK4YFmW5Octsmp+Jibf9EgtwaDTXB2LrYHYLQ1/cSWmcWLytlaiQw==",
                "id": "ST3/E/kFistvR+njqykXeX8T9vCbaF2azCqJ0pDnir3MRcpho7iBTU1NLLoPM2fBvemHnQDaRuv4bQKQJC+HZU+VZT0mFX2EdEsX8oSoA/gnOGJUIEfr0jarcVltmsOjadnmBEU5egQKwRiFYyIBRlAHFIozIzhNxG19pIqFuvziliqOG3FqX4ODDeQnW/EEwJQakTGjZCuQy+I7bQOsbUZR4A5gkW3pscp1mymZ2blH/VaPNIlm1o0B6YqYBNprzG9PN7Mf5QrH38RjkDqS/dIS0sCL/LJQIslIUk3sGMk08/3x8bPGxe8TwKHuQRmnTxlcx862T/oGBsoNvvEDwg==",
                "type": "prescription"
            },
            "receiver_id": "bbc65dd047ef4048aa12f34e2f72e727",
            "sender_id": "ed3afc4482414b24a1088bdd88b66a4a",
            "valid_until": 1672273079.3211017
        }
    ],
    "message": "new block has been added by selective endorsement",
    "signature_of_current_block_hash": "Rirc8tSj/JikabDDyT/DaI1YYv7Q95p8MXhJEgJDmsHWosRbeu7xABHgFH3agjkX0ZEwMM09H+baZ7Cg9IqtBGFU+yteJR3HxtnPyo0XB+goJ7rZiwlD3VjlRuOfwoQIXHh1fGU8P33268k1QkCy+iKK97+EnhsW5jZMr+nvNxEqdoOXCkJrZ9DW47gk05GCvpcTDkTgRRvDzTtqiL63IAnc8bXIS4LItbBmHDPDncjfoRZR5neMg/8VLJTLExuN/f2IN2O85nEvFZvMHt3dSatxhyP0gmOcd8Km+KabUfi9ySXFwWefuzvxn+oOPrJJKApeWN1qmZHX5a+f4e/QKA=="
}
```
- ***The sensitive medical data is encrypted using the patient's public key. So only the patient who the prescription is written specifically for can decrypt and access it.***

## Viewing the MedChain
- The GET URL: http://localhost:8090/medChain
### Expected output example:  
```json
{
    "chain": [
        {
            "current_signed_hash": "KZeTVnwEhEfZ93kAVLZ2A+7BcsJARuHHCc83L0Z/+673dNhAWtTDKhzkN/dbEsJ6h9huDF4rGLXIcbrsxyoMd9OEDQh4H+/lT96rndg+a6C794R3X4iAjV1oRtH33f5NNksTfRCHA4aOSbJHqRTL/eXtQGXP7h+IlNvzwTC/XGncMBtIhk26sIV8rvkbnBhE0GmQkYOCL4NQ9LFu/keS2LnqoxdCKJv9m7sK5OnC0NyFN+A69zgS1/4RQVtnMGyKoWNxQb1hH2+OoZAyiBzov/hlA7fuGlMvPphD1s6a2bW3/CNLHJuy/uuq1MxSAXQb03vgDdWu0CkJ8PcU/XpMCw==",
            "index": 0,
            "med_data": [],
            "previous_block_hash": "GBz6PoXzwqeqn7dPmS0NBh0+Sm10YXkkE6qz+XvT2pU=",
            "timestamp": 1671824900.8024986
        },
        {
            "current_signed_hash": "Rirc8tSj/JikabDDyT/DaI1YYv7Q95p8MXhJEgJDmsHWosRbeu7xABHgFH3agjkX0ZEwMM09H+baZ7Cg9IqtBGFU+yteJR3HxtnPyo0XB+goJ7rZiwlD3VjlRuOfwoQIXHh1fGU8P33268k1QkCy+iKK97+EnhsW5jZMr+nvNxEqdoOXCkJrZ9DW47gk05GCvpcTDkTgRRvDzTtqiL63IAnc8bXIS4LItbBmHDPDncjfoRZR5neMg/8VLJTLExuN/f2IN2O85nEvFZvMHt3dSatxhyP0gmOcd8Km+KabUfi9ySXFwWefuzvxn+oOPrJJKApeWN1qmZHX5a+f4e/QKA==",
            "index": 1,
            "med_data": [
                {
                    "data": {
                        "encrypted_data": "3Bo+ZD4vXuOSjezYEFiF5poCoJlhd4XDh09QoTbEqo746n3tnLXixxzofPsN//so7e98W+y/ekKQAZStH6gbv5yN3ftfnwzBKHgCoYc9kF1G+ezmfqRGJvJkFn2qqXR/rsnHlM7h99QKOLa+kCY1CTKO31E24gWshmdZ5JaD38FZP1kxye1jRS48jSpyYXM0ZIFLj8HbnPFV9J0VbxJjy2LDJB0a3u/ToXqaoGwriFXi0w9fJqnusllLERGlbjprc8XU3wMygtqeVbH3wZW9C9Bp+tK3e9VotgK4YFmW5Octsmp+Jibf9EgtwaDTXB2LrYHYLQ1/cSWmcWLytlaiQw==",
                        "id": "ST3/E/kFistvR+njqykXeX8T9vCbaF2azCqJ0pDnir3MRcpho7iBTU1NLLoPM2fBvemHnQDaRuv4bQKQJC+HZU+VZT0mFX2EdEsX8oSoA/gnOGJUIEfr0jarcVltmsOjadnmBEU5egQKwRiFYyIBRlAHFIozIzhNxG19pIqFuvziliqOG3FqX4ODDeQnW/EEwJQakTGjZCuQy+I7bQOsbUZR4A5gkW3pscp1mymZ2blH/VaPNIlm1o0B6YqYBNprzG9PN7Mf5QrH38RjkDqS/dIS0sCL/LJQIslIUk3sGMk08/3x8bPGxe8TwKHuQRmnTxlcx862T/oGBsoNvvEDwg==",
                        "type": "prescription"
                    },
                    "receiver_id": "bbc65dd047ef4048aa12f34e2f72e727",
                    "sender_id": "ed3afc4482414b24a1088bdd88b66a4a",
                    "valid_until": 1672273079.3211017
                }
            ],
            "previous_block_hash": "l/J9/hfxt+sKqvopaHa/iW8Lrn3wGjBYLxNXiSTEpL8=",
            "timestamp": 1671841094.9775188
        }
    ],
    "length": 2
}
```
- The second block is added after the selective-endorsement.

## Viewing particular client's accessible meddata on the chain
- The GET URL: http://localhost:8090/meddata
- Query: ?client_id=*[client_id_value]*
### Expected output example: 
```json
{
    "length": 1,
    "med_data": [
        {
            "data": {
                "encrypted_data": "3Bo+ZD4vXuOSjezYEFiF5poCoJlhd4XDh09QoTbEqo746n3tnLXixxzofPsN//so7e98W+y/ekKQAZStH6gbv5yN3ftfnwzBKHgCoYc9kF1G+ezmfqRGJvJkFn2qqXR/rsnHlM7h99QKOLa+kCY1CTKO31E24gWshmdZ5JaD38FZP1kxye1jRS48jSpyYXM0ZIFLj8HbnPFV9J0VbxJjy2LDJB0a3u/ToXqaoGwriFXi0w9fJqnusllLERGlbjprc8XU3wMygtqeVbH3wZW9C9Bp+tK3e9VotgK4YFmW5Octsmp+Jibf9EgtwaDTXB2LrYHYLQ1/cSWmcWLytlaiQw==",
                "id": "ST3/E/kFistvR+njqykXeX8T9vCbaF2azCqJ0pDnir3MRcpho7iBTU1NLLoPM2fBvemHnQDaRuv4bQKQJC+HZU+VZT0mFX2EdEsX8oSoA/gnOGJUIEfr0jarcVltmsOjadnmBEU5egQKwRiFYyIBRlAHFIozIzhNxG19pIqFuvziliqOG3FqX4ODDeQnW/EEwJQakTGjZCuQy+I7bQOsbUZR4A5gkW3pscp1mymZ2blH/VaPNIlm1o0B6YqYBNprzG9PN7Mf5QrH38RjkDqS/dIS0sCL/LJQIslIUk3sGMk08/3x8bPGxe8TwKHuQRmnTxlcx862T/oGBsoNvvEDwg==",
                "type": "prescription"
            },
            "receiver_id": "bbc65dd047ef4048aa12f34e2f72e727",
            "sender_id": "ed3afc4482414b24a1088bdd88b66a4a",
            "valid_until": 1672273079.3211017
        }
    ]
}
```
- The accessibility can be determined if the client is considered the receiver on any transaction.
