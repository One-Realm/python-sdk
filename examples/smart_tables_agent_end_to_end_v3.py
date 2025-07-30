import os
import sys

# Add the parent directory to the path to import odin_sdk
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../odin_sdk/'))

from odin_sdk.v3 import create_client, OdinError

def get_agent_prompt(table_ids: dict) -> str:
    raw_prompt = """
# SQL Agent Prompt for Product Catalog Search

You are a specialized PostgreSQL-compatible SQL agent for searching an industrial piping and fitting product catalog database. Your primary goal is to find **article numbers/product codes** based on user product descriptions.

## 🚨 MANDATORY SQL RULES TO AVOID ERRORS 🚨
1. **USE QUOTED COLUMN NAMES**: `p."PN"` NOT `p.PN` 
2. **RESPECT DATA TYPES**: `p."PN" = 16` (numeric) vs `p."DN" = '20'` (text)
3. **NO ILIKE ON NUMERIC**: Use `p."PN" = 16` NOT `p."PN" ILIKE '%16%'`
4. **DN FORMAT**: Use `p."DN" = '20'` NOT `p."DN" = 'DN20'`

You always print the count of tool call you are making in monotonously increasing 1-index based counting, and conclude your findings after 18 tool calls, this behavior ensures over-using tool calling.

## Database Schema Overview

The database contains 3 normalized tables with the following relationships:

### Core Tables:

### 1. **Products Table** `PRODUCTS_TABLE`)

- **Purpose**: Main product catalog containing detailed product information

- **All Columns** (⚠️ **PAY ATTENTION TO DATA TYPES**):

- `id` (SERIAL, Primary Key)
- `product_id` (NUMERIC)
- `complete_product_html` (TEXT)
- `product` (TEXT)
- `product_type` (TEXT)
- `materials` (TEXT)
- `dimensions` (TEXT)
- `details` (TEXT)
- `SDR` (NUMERIC) ⚠️ **NUMERIC - Use =, >, < NOT ILIKE**
- `PN` (NUMERIC) ⚠️ **NUMERIC - Use =, >, < NOT ILIKE**
- `DN` (NUMERIC) ⚠️ **NUMERIC - Use =, >, < NOT ILIKE**
- `unit_length` (NUMERIC) ⚠️ **NUMERIC - Use =, >, < NOT ILIKE**
- `certificates` (TEXT)
- `angle` (TEXT)
- `category` (TEXT)
- `sub_category` (TEXT)
- `source_pdf_name` (TEXT)
- `source_pages` (TEXT)
- `colors` (TEXT)
- `application` (TEXT)
- `safety_instructions` (TEXT)
- `usage_instructions` (TEXT)
- `other_details` (TEXT)

### 2. **Variants Table** `VARIANTS_TABLE`)

- **Purpose**: Product variants with specific article numbers

- **All Columns**:

- `id` (SERIAL, Primary Key)

- `variant_id` (NUMERIC)

- `article_number` (TEXT)

- `product_id` (NUMERIC, Foreign Key to Products)

### 3. **Dimensions Table** `DIMENSIONS_TABLE`)

- **Purpose**: Technical specifications and measurements for product variants

- **All Columns** (⚠️ **PAY ATTENTION TO DATA TYPES**):

- `id` (SERIAL, Primary Key)
- `symbol` (TEXT) ⚠️ **TEXT - Use ILIKE for pattern matching**
- `value` (TEXT) ⚠️ **TEXT - Use ILIKE for pattern matching**
- `unit` (TEXT)
- `variant_id` (NUMERIC, Foreign Key to Variants)
- `product_id` (NUMERIC, Foreign Key to Products)

### **Table ID Mapping (CRUCIAL):**

- `PRODUCTS_TABLE` is the real table name for **products** table

- `VARIANTS_TABLE` is the real table name for **variants** table

- `DIMENSIONS_TABLE` is the real table name for **dimensions** table

## ⚠️ CRITICAL SQL FORMATTING RULES ⚠️

**THESE RULES MUST BE FOLLOWED TO AVOID ERRORS:**

### 1. **ALL COLUMN NAMES MUST BE QUOTED**
- Use `p."PN"` NOT `p.PN` to avoid "column does not exist" errors
- **REQUIRED QUOTES FOR ALL COLUMNS**: `"PN"`, `"DN"`, `"SDR"`, `"symbol"`, `"value"`, `"unit"`

### 2. **DATA TYPE AWARENESS - CRITICAL**
- **`p."PN"` is NUMERIC** - Use `=`, `>`, `<`, NOT `ILIKE`
- **`p."DN"` is TEXT** - Use `ILIKE`, `=` for text operations
- **`d."value"` is TEXT** - Use `ILIKE`, `=` for text operations

### 3. **CORRECT DATA TYPE USAGE**

**✅ CORRECT for NUMERIC columns (PN):**
```sql
WHERE p."PN" = 16                    -- numeric comparison
WHERE p."PN" IN (10, 16, 25)        -- numeric IN clause
WHERE d."value" ILIKE '%20%'         -- text pattern match
```

**❌ INCORRECT for NUMERIC columns:**
```sql
WHERE p."PN" ILIKE '%16%'           -- ERROR: ILIKE on numeric
WHERE p."PN" = 'PN16'                  -- wrong format
```

**✅ CORRECT for TEXT columns (DN, product_type, materials, value):**
```sql
WHERE p."DN" = '20'                 -- exact text match
WHERE p."DN" ILIKE '%20%'           -- text pattern match
WHERE p."DN" IN ('15', '20', '25')  -- text IN clause
```

Remember: Your goal is to find the exact article number that matches the user's product description. Be thorough, investigative, and always verify your results with complete product details.

All products available in the database are George Fischer products.

**NEVER** mix product types, for example when asked for a Winkel, **always** give a winkel and never a Bogen, and vice versa.
"""
    prompt = raw_prompt
    for table_name, table_id in table_ids.items():
        table_var = f"{table_name.upper()}_TABLE"
        prompt = prompt.replace(table_var, table_id)
    
    return prompt

def main():
    """
    Enhanced Smart Tables Agent Demo using the v3 wrapper.
    
    This example demonstrates v3 improvements:
    - Flattened response objects (project.id vs project.project.id)
    - Convenience methods (project.delete() vs client.projects().delete(id))
    - Project-scoped managers (project.data.import_table())
    - Resource self-awareness (agent.activate(), chat.send_message())
    
    Shows the same smart tables functionality as v2 but with cleaner API usage.
    """
    
    # Initialize client with credentials
    client = create_client(
        api_key="b13cc8df-e33a-4828-a86c-0be3c96dcd0a",
        api_secret="IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="
    )
    
    # Column mappings for CSV imports (same as v2)
    column_mappings = {
        "variants": [
            {"sourceColumn": "variant_id", "targetColumn": "variant_id", "dataType": "number"},
            {"sourceColumn": "article_number", "targetColumn": "article_number", "dataType": "text"},
            {"sourceColumn": "product_id", "targetColumn": "product_id", "dataType": "number"},
        ],
        "products": [
            {"sourceColumn": "product_id", "targetColumn": "product_id", "dataType": "number"},
            {"sourceColumn": "complete_product_html", "targetColumn": "complete_product_html", "dataType": "text"},
            {"sourceColumn": "product", "targetColumn": "product", "dataType": "text"},
            {"sourceColumn": "product_type", "targetColumn": "product_type", "dataType": "text"},
            {"sourceColumn": "materials", "targetColumn": "materials", "dataType": "text"},
            {"sourceColumn": "dimensions", "targetColumn": "dimensions", "dataType": "text"},
            {"sourceColumn": "details", "targetColumn": "details", "dataType": "text"},
            {"sourceColumn": "SDR", "targetColumn": "SDR", "dataType": "number"},
            {"sourceColumn": "PN", "targetColumn": "PN", "dataType": "number"},
            {"sourceColumn": "DN", "targetColumn": "DN", "dataType": "number"},
            {"sourceColumn": "unit_length", "targetColumn": "unit_length", "dataType": "number"},
            {"sourceColumn": "certificates", "targetColumn": "certificates", "dataType": "text"},
            {"sourceColumn": "angle", "targetColumn": "angle", "dataType": "text"},
            {"sourceColumn": "category", "targetColumn": "category", "dataType": "text"},
            {"sourceColumn": "sub_category", "targetColumn": "sub_category", "dataType": "text"},
            {"sourceColumn": "source_pdf_name", "targetColumn": "source_pdf_name", "dataType": "text"},
            {"sourceColumn": "source_pages", "targetColumn": "source_pages", "dataType": "text"},
            {"sourceColumn": "colors", "targetColumn": "colors", "dataType": "text"},
            {"sourceColumn": "application", "targetColumn": "application", "dataType": "text"},
            {"sourceColumn": "safety_instructions", "targetColumn": "safety_instructions", "dataType": "text"},
            {"sourceColumn": "usage_instructions", "targetColumn": "usage_instructions", "dataType": "text"},
            {"sourceColumn": "other_details", "targetColumn": "other_details", "dataType": "text"},
        ],
        "dimensions": [
            {"sourceColumn": "symbol", "targetColumn": "symbol", "dataType": "text"},
            {"sourceColumn": "value", "targetColumn": "value", "dataType": "text"},
            {"sourceColumn": "unit", "targetColumn": "unit", "dataType": "text"},
            {"sourceColumn": "variant_id", "targetColumn": "variant_id", "dataType": "number"},
            {"sourceColumn": "product_id", "targetColumn": "product_id", "dataType": "number"},
        ],
    }
    
    try:
        print("🚀 Starting Smart Tables Agent Demo (V3 - Enhanced Wrapper)")
        
        # Clean up any existing projects with 3+ duplicates
        print("\n🧹 Cleaning up duplicate projects...")
        existing_projects = client.projects().list()
        if existing_projects.projects:
            project_groups = {}
            for project in existing_projects.projects:
                name = project.name  # v3: Flattened attribute access
                if name not in project_groups:
                    project_groups[name] = []
                project_groups[name].append(project)
            
            for name, projects in project_groups.items():
                if len(projects) >= 3:
                    print(f"Deleting {len(projects)} duplicate projects named '{name}'")
                    for project in projects:
                        try:
                            project.delete()  # v3: Convenience method!
                            print(f"   ✅ Deleted: {project.name}")
                        except Exception as e:
                            print(f"   ❌ Failed to delete: {e}")
        
        # Create project
        print("\n📁 Creating project...")
        project = client.projects().create(
            name="SDK Smart Tables Demo V3",
            description="Smart tables demo with SQL agent using v3 wrapper SDK"
        )
        print(f"✅ Project created: {project.name} (ID: {project.id})")  # v3: Flattened attributes!
        
        # Import CSV tables using project-scoped manager
        print("\n📊 Importing CSV tables...")
        table_ids = {}
        
        for table_name, mappings in column_mappings.items():
            print(f"   Importing {table_name}.csv...")
            csv_path = os.path.join(os.path.dirname(__file__), f"{table_name}.csv")
            
            try:
                # Convert column mappings to JSON string (same as v2)
                import json
                mappings_json = json.dumps(mappings)
                
                import_response = project.data.import_table(  # v3: Project-scoped manager!
                    title=table_name,
                    description=f"Imported {table_name} data",
                    file_path=csv_path,
                    column_mappings=mappings_json
                )
                
                # Extract table ID from response (same logic as v2)
                data_type_id_part = import_response.data_type_id[:8]
                
                # Get view to find table ID
                view_response = project.data.get_view(  # v3: Project-scoped manager!
                    data_type_id=import_response.data_type_id
                )
                
                # Find matching table ID
                for view in view_response.views:
                    if data_type_id_part in view.get("table_id", ""):
                        table_ids[table_name] = view["table_id"]
                        break
                
                print(f"   ✅ {table_name} imported successfully")
                
            except Exception as e:
                print(f"   ❌ Failed to import {table_name}: {e}")
        
        print(f"✅ All tables imported. Table IDs: {list(table_ids.keys())}")
        
        # Check if any tables were actually imported
        if not table_ids:
            print("❌ No tables were successfully imported!")
            print("Cannot proceed without data tables.")
            
            # Wait for user input before cleanup
            print("\n" + "="*80)
            print("🎯 DEMO FAILED! Press Enter to clean up and delete the project...")
            print("="*80)
            input()
            
            # Clean up using convenience method
            print("\n🧹 Cleaning up...")
            project.delete()  # v3: Much cleaner!
            print(f"✅ Project '{project.name}' deleted successfully!")
            return
        
        # Create SQL agent using project-scoped manager
        print("\n🤖 Creating SQL analysis agent...")
        
        # Generate dynamic personality with actual table IDs
        personality = get_agent_prompt(table_ids)

        # Build agent configuration (same as v2 but cleaner usage)
        building_blocks = [
            {
                "name": "knowledge_base",
                "project_id": project.id,  # v3: Flattened attribute
                "document_keys": [],
                "enrich_sources": False,
                "generate_inline_citations": False,
                "enforce_strict_adherence": False,
                "query_language": "English",
                "translate_queries": False,
                "additional_kb_ids": [],
                "kb_search_results_to_return": 10,
                "kb_search_score_threshold": 0,
                "extra_strict_adherence_test_rules": [],
                "extra_strict_adherence_failure_response_rules": [],
                "use_kb_cache": False,
                "should_enrich": False,
                "use_whole_document": False,
                "cache_threshold": 0.6,
                "max_context_size": 2500
            },
            {
                "name": "agent_type",
                "agent_type": "tool_use_agent"
            },
            {
                "name": "ai_model",
                "model": "GPT 4.1"
            },
            {
                "name": "toolkits",
                "toolkits": {
                    "sql_database": {
                        "connection_id": "",
                        "data_source_type": "sql",
                        "config": [{
                            "name": "Database Configuration",
                            "connection_id": "",
                            "enabled_tools": [
                                "sql_db_query",
                                "sql_db_list_tables",
                                "sql_db_query_checker",
                                "sql_db_schema",
                                "describe_table",
                                "list_tables"
                            ],
                            "csv_names": [],
                            "enable_all_smart_tables": True,
                            "block_type": "smart_table"
                        }, {
                            "block_type": "sql",
                            "connection_id": ""
                        }],
                        "type": "sql_database"
                    }
                }
            }
        ]
        
        try:
            agent = project.agents.create(  # v3: Project-scoped manager!
                name="Smart Tables SQL Agent",
                personality=personality,
                building_blocks=building_blocks,
                temperature=0.0
            )
            print(f"✅ SQL agent created: {agent.agent_id}")
        except Exception as e:
            print(f"❌ Failed to create agent: {e}")
            
            # Wait for user input before cleanup
            print("\n" + "="*80)
            print("🎯 AGENT CREATION FAILED! Press Enter to clean up and delete the project...")
            print("="*80)
            input()
            
            # Clean up using convenience method
            print("\n🧹 Cleaning up...")
            project.delete()  # v3: Much cleaner!
            print(f"✅ Project '{project.name}' deleted successfully!")
            return
        
        # Activate agent using convenience method
        print("\n⚡ Activating agent...")
        try:
            agent.activate()  # v3: Agent knows its own context!
            print("✅ Agent activated successfully")
        except Exception as e:
            print(f"❌ Failed to activate agent: {e}")
            
            # Wait for user input before cleanup
            print("\n" + "="*80)
            print("🎯 AGENT ACTIVATION FAILED! Press Enter to clean up and delete the project...")
            print("="*80)
            input()
            
            # Clean up using convenience method
            print("\n🧹 Cleaning up...")
            project.delete()  # v3: Much cleaner!
            print(f"✅ Project '{project.name}' deleted successfully!")
            return
        
        # Create chat session using project-scoped manager
        print("\n💬 Creating data analysis chat...")
        try:
            chat = project.chats.create(  # v3: Project-scoped manager!
                name="Product Data Analysis Chat",
                context="Analyze the imported product data using SQL queries. Help users find specific products and article numbers."
            )
            print(f"✅ Chat created: {chat.chat_id}")
        except Exception as e:
            print(f"❌ Failed to create chat: {e}")
            
            # Wait for user input before cleanup
            print("\n" + "="*80)
            print("🎯 CHAT CREATION FAILED! Press Enter to clean up and delete the project...")
            print("="*80)
            input()
            
            # Clean up using convenience method
            print("\n🧹 Cleaning up...")
            project.delete()  # v3: Much cleaner!
            print(f"✅ Project '{project.name}' deleted successfully!")
            return
        
        # Send product analysis request using chat convenience method
        print("\n🔍 Requesting product analysis...")
        message = """Fetch the article number and unit length if any for below product.

Rohrleitungen PP-H DN20, d=25 mm, nach DIN 8077/8078
SDR 11, PN10"""
        
        try:
            response = chat.send_message(  # v3: Chat knows its own context!
                message=message,
                skip_stream=True
            )
        except Exception as e:
            print(f"❌ Failed to send message: {e}")
            
            # Wait for user input before cleanup
            print("\n" + "="*80)
            print("🎯 MESSAGE SENDING FAILED! Press Enter to clean up and delete the project...")
            print("="*80)
            input()
            
            # Clean up using convenience method
            print("\n🧹 Cleaning up...")
            project.delete()  # v3: Much cleaner!
            print(f"✅ Project '{project.name}' deleted successfully!")
            return
        
        print(f"\n📝 Product Query: Find article number for PP-H pipe DN20, d=25mm, SDR 11, PN10")
        print("\n🤖 AI Response:")
        print("=" * 80)
        
        # Handle different response formats
        if hasattr(response, 'message') and response.message:
            print(response.message)
        elif hasattr(response, 'response_text') and response.response_text:
            print(response.response_text)
        else:
            print(f"Response received: {response}")
        
        print("=" * 80)
        print("\n✅ Product analysis complete!")
        print("The AI agent analyzed the imported CSV data using SQL queries!")
        
        # Wait for user input before cleanup
        print("\n" + "="*80)
        print("🎯 DEMO COMPLETE! Press Enter to clean up and delete the project...")
        print("="*80)
        input()
        
        # Clean up using convenience method
        print("\n🧹 Cleaning up...")
        project.delete()  # v3: Much cleaner!
        print(f"✅ Project '{project.name}' deleted successfully!")
        print("🔄 Demo completed successfully!")
        
    except OdinError as e:
        print(f"❌ API Error: {e}")
        
        # If we have a project, offer to clean up
        if 'project' in locals() and hasattr(project, 'id'):
            print("\n" + "="*80)
            print("🎯 API ERROR OCCURRED! Press Enter to clean up and delete the project...")
            print("="*80)
            input()
            
            # Clean up using convenience method
            print("\n🧹 Cleaning up after error...")
            try:
                project.delete()  # v3: Much cleaner!
                print(f"✅ Project '{project.name}' deleted successfully!")
            except Exception as cleanup_e:
                print(f"❌ Failed to clean up project: {cleanup_e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        
        # If we have a project, offer to clean up
        if 'project' in locals() and hasattr(project, 'id'):
            print("\n" + "="*80)
            print("🎯 UNEXPECTED ERROR OCCURRED! Press Enter to clean up and delete the project...")
            print("="*80)
            input()
            
            # Clean up using convenience method
            print("\n🧹 Cleaning up after error...")
            try:
                project.delete()  # v3: Much cleaner!
                print(f"✅ Project '{project.name}' deleted successfully!")
            except Exception as cleanup_e:
                print(f"❌ Failed to clean up project: {cleanup_e}")
    
    print("\n🏁 Smart Tables Agent Demo V3 completed!")
    print("\n📈 V3 Improvements showcased:")
    print("   • Flattened response objects: project.id vs project.project.id")
    print("   • Convenience methods: project.delete() vs client.projects().delete(id)")
    print("   • Project-scoped managers: project.data.import_table(), project.agents.create()")
    print("   • Resource self-awareness: agent.activate(), chat.send_message()")

if __name__ == "__main__":
    main() 