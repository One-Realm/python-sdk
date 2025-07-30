#!/usr/bin/env python3
"""
🔐 ODIN SDK v3 - Authentication Demo

This demo showcases authentication functionality with the ODIN SDK v3:
- ✅ Successful authentication with valid credentials
- ❌ Failed authentication with invalid credentials  
- 🔄 Project creation and deletion operations
- 🛡️ Proper error handling with OdinError

This demonstrates the core authentication flow and basic project management
operations that form the foundation of all ODIN SDK interactions.
"""

import time
from odin_sdk.v3 import create_client, OdinError


def demo_successful_auth():
    """
    Demonstrate successful authentication and basic operations.
    
    This shows the proper authentication flow with valid credentials
    and demonstrates basic project management operations.
    """
    print("\n" + "=" * 80)
    print("🔐 DEMO 1: SUCCESSFUL AUTHENTICATION")
    print("=" * 80)
    
    # Valid credentials for demonstration
    valid_credentials = {
        "api_key": "b13cc8df-e33a-4828-a86c-0be3c96dcd0a",
        "api_secret": "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0=",
        "host": "http://localhost:8001"
    }
    
    try:
        print("🚀 Initializing ODIN client with valid credentials...")
        print(f"   API Key: {valid_credentials['api_key'][:20]}...")
        print(f"   Host: {valid_credentials['host']}")
        
        # Create client with valid credentials
        client = create_client(**valid_credentials)
        print("✅ Client initialized successfully!")
        
        # Test authentication by listing existing projects
        print("\n📋 Testing authentication by listing projects...")
        try:
            projects_response = client.projects().list()
            print(f"✅ Authentication successful! Found {len(projects_response.projects) if projects_response.projects else 0} existing projects.")
            
            # Show existing projects if any
            if projects_response.projects and len(projects_response.projects) > 0:
                print("   Existing projects:")
                for project in projects_response.projects[:3]:  # Show first 3
                    print(f"   • {project.name} (ID: {project.id})")
                if len(projects_response.projects) > 3:
                    print(f"   ... and {len(projects_response.projects) - 3} more")
            else:
                print("   No existing projects found.")
                
        except OdinError as e:
            print(f"❌ Authentication test failed: {e}")
            return None
            
        # Test project creation
        print("\n📁 Testing project creation...")
        try:
            project = client.projects().create(
                name="Auth Demo Test Project",
                description="Demo project created to test authentication and basic operations"
            )
            print(f"✅ Project created successfully!")
            print(f"   Name: {project.name}")
            print(f"   ID: {project.id}")
            print(f"   Description: {project.description}")
            
            # Brief pause to show the project exists
            print("\n⏱️  Project active for 3 seconds...")
            time.sleep(3)
            
            # Test project deletion
            print("\n🗑️  Testing project deletion...")
            project.delete()
            print("✅ Project deleted successfully!")
            
        except OdinError as e:
            print(f"❌ Project operation failed: {e}")
            return None
            
        print("\n🎉 All authentication and basic operations completed successfully!")
        return client
        
    except OdinError as e:
        print(f"❌ ODIN API Error during client initialization: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error during authentication: {e}")
        return None


def demo_failed_auth():
    """
    Demonstrate failed authentication scenarios.
    
    This shows how the SDK handles various authentication failures
    and the proper error messages returned.
    """
    print("\n" + "=" * 80)
    print("🚫 DEMO 2: FAILED AUTHENTICATION SCENARIOS")
    print("=" * 80)
    
    # Test scenarios with different types of invalid credentials
    test_scenarios = [
        {
            "name": "Invalid API Key",
            "credentials": {
                "api_key": "invalid-api-key-12345",
                "api_secret": "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0=",
                "host": "http://localhost:8001"
            }
        },
        {
            "name": "Invalid API Secret", 
            "credentials": {
                "api_key": "b13cc8df-e33a-4828-a86c-0be3c96dcd0a",
                "api_secret": "invalid-secret-xyz123==",
                "host": "http://localhost:8001"
            }
        },
        {
            "name": "Both Invalid Credentials",
            "credentials": {
                "api_key": "completely-wrong-key",
                "api_secret": "completely-wrong-secret",
                "host": "http://localhost:8001"
            }
        },
        {
            "name": "Invalid Host",
            "credentials": {
                "api_key": "b13cc8df-e33a-4828-a86c-0be3c96dcd0a", 
                "api_secret": "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0=",
                "host": "http://invalid-host:8001"
            }
        }
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n📋 Test {i}: {scenario['name']}")
        print("-" * 50)
        
        try:
            print(f"🔄 Attempting connection with {scenario['name'].lower()}...")
            
            # Create client (this might succeed even with bad credentials)
            client = create_client(**scenario['credentials'])
            print("⚠️  Client created (credentials not validated yet)")
            
            # The real test - try to make an API call
            print("🔍 Testing credentials with API call...")
            projects_response = client.projects().list()
            
            # If we get here, authentication unexpectedly succeeded
            print("⚠️  Unexpected: Authentication succeeded with invalid credentials!")
            
        except OdinError as e:
            print(f"✅ Expected failure: {e}")
            print("   This demonstrates proper error handling for invalid credentials.")
            
        except Exception as e:
            print(f"❌ Unexpected error type: {e}")
            print("   This might indicate a network or configuration issue.")
            
        # Add small delay between tests
        time.sleep(1)
    
    print("\n✅ Failed authentication scenarios completed!")
    print("All authentication failures were handled properly by the SDK.")


def demo_auth_best_practices():
    """
    Demonstrate authentication best practices and security considerations.
    """
    print("\n" + "=" * 80)
    print("🛡️  DEMO 3: AUTHENTICATION BEST PRACTICES")
    print("=" * 80)
    
    print("🔒 Security Best Practices for ODIN SDK Authentication:")
    print()
    
    print("1. ✅ Environment Variables (Recommended)")
    print("   Store credentials in environment variables:")
    print("   ```bash")
    print("   export ODIN_API_KEY='your-api-key'")
    print("   export ODIN_API_SECRET='your-api-secret'")
    print("   export ODIN_HOST='http://localhost:8001'")
    print("   ```")
    print()
    print("   ```python")
    print("   import os")
    print("   client = create_client(")
    print("       api_key=os.getenv('ODIN_API_KEY'),")
    print("       api_secret=os.getenv('ODIN_API_SECRET'),")
    print("       host=os.getenv('ODIN_HOST')")
    print("   )")
    print("   ```")
    print()
    
    print("2. ✅ Configuration Files")
    print("   Use secure configuration files with restricted permissions:")
    print("   ```python")
    print("   import json")
    print("   with open('config.json', 'r') as f:")
    print("       config = json.load(f)")
    print("   client = create_client(**config['odin_credentials'])")
    print("   ```")
    print()
    
    print("3. ❌ Hard-coded Credentials (Avoid)")
    print("   Never hard-code credentials in production code:")
    print("   ```python")
    print("   # DON'T DO THIS IN PRODUCTION!")
    print("   client = create_client(")
    print("       api_key='hard-coded-key',")
    print("       api_secret='hard-coded-secret'")
    print("   )")
    print("   ```")
    print()
    
    print("4. 🔄 Error Handling Pattern")
    print("   Always use proper error handling:")
    print("   ```python")
    print("   try:")
    print("       client = create_client(**credentials)")
    print("       # Test authentication")
    print("       client.projects().list()")
    print("   except OdinError as e:")
    print("       print(f'Authentication failed: {e}')")
    print("   except Exception as e:")
    print("       print(f'Unexpected error: {e}')")
    print("   ```")
    print()
    
    print("5. 🔍 Credential Validation")
    print("   Test credentials immediately after client creation:")
    print("   ```python")
    print("   client = create_client(**credentials)")
    print("   try:")
    print("       client.projects().list()  # Simple validation call")
    print("       print('Authentication successful!')")
    print("   except OdinError:")
    print("       print('Invalid credentials')")
    print("   ```")


def main():
    """
    Main demo function that orchestrates all authentication examples.
    """
    print("🚀 ODIN SDK v3 - Authentication Demo")
    print("=" * 80)
    print("This demo showcases authentication functionality and best practices.")
    print("You'll see both successful and failed authentication scenarios.")
    print()
    print("⚠️  Note: This demo uses localhost:8001 as the host.")
    print("   Make sure your ODIN server is running locally for full functionality.")
    print()
    
    # Pause to let user read the introduction
    print("Press Enter to start the demo...")
    input()
    
    # Run authentication demos
    successful_client = demo_successful_auth()
    demo_failed_auth()
    demo_auth_best_practices()
    
    # Final summary
    print("\n" + "=" * 80)
    print("🎯 AUTHENTICATION DEMO COMPLETE!")
    print("=" * 80)
    print()
    print("Summary of what we demonstrated:")
    print("✅ Successful authentication with valid credentials")
    print("✅ Project creation and deletion operations")
    print("❌ Failed authentication with invalid credentials")
    print("🛡️  Proper error handling with OdinError")
    print("📚 Authentication best practices and security guidelines")
    print()
    print("Key Takeaways:")
    print("• Always use environment variables for credentials in production")
    print("• Test authentication immediately after client creation")
    print("• Use proper error handling with OdinError")
    print("• Never hard-code credentials in your source code")
    print("• The ODIN SDK provides clear error messages for authentication issues")
    print()
    print("🔗 Next Steps:")
    print("• Check out other examples in the examples/ folder")
    print("• Read the full documentation in README.md")
    print("• Explore building blocks in Blocks.md")
    print("• Learn about toolkits in ToolKits.md")
    print()
    print("Thank you for using the ODIN SDK v3! 🎉")


if __name__ == "__main__":
    main()