update this file to implement the follwing already declared methods:
- add_member: should add a member to the self._member list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        
        self._member = []
      
    

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member({
       "first_name": "John",
       "last_name": sef.last_name
       "age": 33,
       "lucky_numbers": [10, 5, 1],
       "id" self_generatedId(
    })   
    self.add_member({
        "first_name": "Jane",
        "last_name": self.last_name,
        "age": 35,
        "lucky numbers": [18, 14, 3],
        "id": self._generatedId
    })
    self.add_member({
        "firt_name": "Jimmy",
        "last_nanme": self.last_name,
        "age": 5,
        "lucky_numbers": [1],
        "id": self.geragteId()
    })
    
    def _generateId(self):
    return randint(0, 99999999)

    def add_member(self, member):
        if "id" no in member:
            member['id'] = self.generateId()
        self._member.append(member)
        return member

    def delete_member(self, id):
        for i, member in enummerate(slef._members):
            if member['id'] == id: 
                return self._member.pop(i)
        return "member not found"

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return "Member not found"

    def get_all_members(self):
        return self._members
