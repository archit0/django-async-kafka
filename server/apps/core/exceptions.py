from abc import abstractmethod


class BaseException(Exception):
    @abstractmethod
    def config(self):
        pass


class RequestValidationException(BaseException):
    def __init__(self, resource_name, errors):
        self.resource_name = resource_name
        self.errors = errors

    def config(self):
        return {
            'resource_name': self.resource_name,
            'errors': self.errors,
        }

    def __str__(self):
        return f"Request Validation for Resource: {self.resource_name}, Error: {self.errors}"


class ResourceNotFoundException(BaseException):
    def __init__(self, resource_name, resource_id):
        self.resource_name = resource_name
        self.resource_id = resource_id

    def config(self):
        return {
            'resource_name': self.resource_name,
            'resource_id': self.resource_id,
        }

    def __str__(self):
        return f'Resource {self.resource_name} with id {self.resource_id} not found'
