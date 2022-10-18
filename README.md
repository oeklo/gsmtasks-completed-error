1. [Install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
1. install dependencies

    `poetry instsall`
2. Run program 

    `poetry run python -m gsmtasks_complete --token [GSMTASKS_TOKEN]`

# Actual result

 ```
 DEBUG:__main__:Created tasks [UUID('1de7f111-3381-4cf5-884a-5c2c4e051d7f'), UUID('a7dd2ce1-9cfd-4369-9e40-2fc30549246b')]
 INFO:__main__:Working with a7dd2ce1-9cfd-4369-9e40-2fc30549246b
 INFO:__main__:completed
 DEBUG:__main__:Since: 2022-10-15T00:00:00+02:00
 INFO:__main__:a7dd2ce1-9cfd-4369-9e40-2fc30549246b NOT found
 DEBUG:__main__:Found [UUID('81eb58e9-dbb9-4a83-998c-9efd59392bb2'), UUID('560d8417-94e6-4601-8eb7-60c8ee7e2fcf'), UUID('be9f41b8-0112-474d-8df7-7032ddf59230'), UUID('2c52a1fc-4053-4646-bc39-74bcccbe7cb2'), UUID('c3c6be9e-bff8-4de6-b58d-822cbe7a5e9b'), UUID('a2b1ba24-14c2-47b0-9134-98a5d903da1d'), UUID('b707f2de-0a75-4d16-b056-bfe83de6610a'), UUID('4c1bab4f-93fa-41b1-bf67-75f3b387e294'), UUID('a4d9a080-2b35-4264-86bc-e64901c10cff'), UUID('ee349d5f-c21b-4247-83c7-006a62fc7a1d'), UUID('72100503-91e7-4477-bfcb-36e3c730d3fb'), UUID('f0303019-1076-490d-8715-8e23a351d209'), UUID('60997f18-7a74-4b86-93ab-8d68f5a63f25'), UUID('44bb481c-1f34-4bfd-9fba-788aa4d23708'), UUID('8e70cf88-3cef-4b05-8cec-f60ab764a98a'), UUID('0d67088e-c210-4e35-8dba-ece6ceb41c05'), UUID('e4277431-d016-4954-97aa-238d21f90f57'), UUID('8d372e83-0b13-416a-ae0a-efa119c8bb3d'), UUID('603074d3-24c6-4b24-8e91-33d811aebc2f'), UUID('72a1732f-8c45-4abd-b216-d7fc4d8818c6'), UUID('908a0750-f5a9-43b6-b0c1-d32fe0b230be'), UUID('cf9b1674-c4bc-463b-9040-ce702d8f26ab'), UUID('ff654b31-5832-44e3-85ff-edbdacb7b15f'), UUID('e7a5781c-4a81-46d3-a839-c70a9a7bbad5'), UUID('695e0e94-644e-4390-93a3-4e9f3d333c78'), UUID('2dc41cd8-d854-4677-b1a9-d7292299041c'), UUID('b81dcdd5-d2a6-46eb-a118-57a3c378a56f'), UUID('f84e6632-dcc3-4815-af0e-2d708628216a'), UUID('37ef46a0-001f-4510-a7e4-6505aa5ff41f'), UUID('b75770b1-6345-4acf-9827-d31bb5d0c85e'), UUID('44d71861-5a00-46a2-9efb-1f7f51f8039d'), UUID('ea0880ca-16f1-4906-acf5-b594ac87f87c'), UUID('f61ba993-1e6b-4a44-a1ac-2dd516eb3e9e'), UUID('851a9a4e-d14c-46b9-b762-ee7e47e4df43'), UUID('22d6af97-a554-4712-a9ff-02d90b6193ae'), UUID('5d94ceb1-6cf5-477b-9f7d-b54fc47500f2'), UUID('890016ca-da55-419d-a48e-0cb20dde3a36'), UUID('061a9cf4-3e08-49a3-82e6-e0b85a9976ee'), UUID('e428640b-ca19-4412-8bf5-71393448d7d4'), UUID('1a8d4122-83c1-457f-bb46-94ccba3a5d4c'), UUID('9c05627e-6212-471b-bf28-0a4214b4dd33'), UUID('ce6f46ce-e1a6-4436-a9f9-115d29a3b0e7'), UUID('94737a12-4617-4202-80df-b4e6fc453ca6'), UUID('9d0bbc80-d6f4-4608-8b37-14492f0b3470')]
 ```

# Expected result

```
...
INFO:__main__:[task id] found
...
```
# Additional information
Had to create multiple tasks in a single call (line 48) and pass `updated_at__gte` (line 70) to reproduce the error