

from dataclasses import dataclass

from bin.contentctl_project.contentctl_core.application.factory.new_content_factory import NewContentFactory, NewContentFactoryInputDto, NewContentFactoryOutputDto
from bin.contentctl_project.contentctl_core.domain.entities.enums.enums import SecurityContentProduct
from bin.contentctl_project.contentctl_core.application.adapter.adapter import Adapter


@dataclass(frozen=True)
class NewContentInputDto:
    factory_input_dto: NewContentFactoryInputDto
    product:SecurityContentProduct
    adapter : Adapter


class NewContent:

    def execute(self, input_dto: NewContentInputDto) -> None:
        if input_dto.product == SecurityContentProduct.ESCU:
            factory_output_dto = NewContentFactoryOutputDto(dict())
            factory = NewContentFactory(factory_output_dto)
            factory.execute(input_dto.factory_input_dto)
            input_dto.adapter.writeObjectNewContent(factory_output_dto.obj, input_dto.factory_input_dto.type)