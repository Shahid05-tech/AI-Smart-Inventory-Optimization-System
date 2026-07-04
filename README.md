<!-- 1)Architecture Diagram             -->
                        
                        +------------------+
                        |   Daily CSV      |
                        |  ERP / POS Data  |
                        +--------+---------+
                                 |
                                 |
                                 ▼
                      AWS S3 (raw folder)
                                 |
                                 ▼
                     FastAPI ETL Service
                                 |
          +----------------------+--------------------+
          |                                           |
          ▼                                           ▼
  Pandas Cleaning                           Validation Rules
          |                                           |
          +----------------------+--------------------+
                                 |
                                 ▼
                   AWS S3 (processed folder)
                                 |
                                 ▼
                        PostgreSQL Database
                                 |
                  +--------------+--------------+
                  |                             |
                  ▼                             ▼
            Analytics APIs               Recommendation API
                  |                             |
                  ▼                             ▼
             React Dashboard          Random Forest Model
                                              |
                                              ▼
                                   Inventory Recommendation