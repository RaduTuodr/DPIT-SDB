from repository.file_repository import FileRepository
from repository.repository import Repository
from service.admin_service import AdminService
from service.client_service import ClientService
from service.promotion_service import PromotionService
from ui.console import ConsoleUI
from validator.product_validator import ProductValidator

repository = Repository()
admin_repository = Repository()
client_repository = Repository()
promotion_repository = Repository()
file_repository = FileRepository(ProductValidator(), admin_repository)

admin_service = AdminService(admin_repository)
client_service = ClientService(client_repository)
promotion_service = PromotionService(promotion_repository, admin_service)

ui = ConsoleUI(admin_service, client_service, promotion_service, repository, file_repository)

ui.run()
