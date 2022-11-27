from loguru import logger
import pymongo

class DjangoLoggingMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request URL: {request.build_absolute_uri()}")
        logger.info(f"Request METHOD: {request.method}")
        logger.info(f"Request HEADERS: {request.headers}")
        logger.info(f"Request GET data: {request.GET}")
        logger.info(f"Request POST data: {request.POST}")
        logger.info(f"Request FILES data: {request.FILES}")

        response = self.get_response(request)
        logger.info(f"Request USER: {request.user}")
        logger.info(f"Response STATUS_CODE: {response.status_code}")
        
     
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Multikart_mongo"]
        mycol = mydb["all_logs_mylogs"]
        
 
        
        logs = {
            'URL':f'logger.info("Request URL: {request.build_absolute_uri()}")',
            'METHOD':f'logger.info("Request METHOD: {request.method}")',
            'USER':f'logger.info("Request USER: {request.user}")'
        }


        mycol.insert(logs)
   
        
        # mycol.insert({'METHOD':str(logger.info(f"Request METHOD: {request.method}"))})
        
        # mycol.insert({'HEADERS':str(logger.info(f"Request HEADERS: {request.headers}"))})

        return response

       

        
        
        # try:
        #     logger.info(f"Response MEDIA_TYPE: {response.accepted_media_type}")
        #     logger.info(f"Response _MEDIA_TYPE: {response.charset}")
        #     logger.info(f"Response DATA: {response.data}")
        # except:
        #     logger.info(f"Response MEDIA_TYPE: {response.charset}")
        #     try:
        #         logger.info(f"Response DATA: {response.content}")
        #     except:
        #         logger.info(f"Response DATA: {response.streaming_content}")

