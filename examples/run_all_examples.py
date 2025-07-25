"""
ODIN SDK - Comprehensive CRUD Examples Runner (Fixed & Updated)
Runs all CRUD examples for Projects, Knowledge Base, Agents, and Chats
Demonstrates the complete capabilities of the ODIN SDK using localhost:8001
"""
import sys
import time
import subprocess
import os

def run_example(script_name, description):
    """Run a single example script"""
    print("=" * 80)
    print(f"🚀 RUNNING: {description}")
    print(f"📝 Script: {script_name}")
    print("=" * 80)
    
    try:
        # Run the script and capture output
        result = subprocess.run(
            [sys.executable, script_name], 
            cwd=os.path.dirname(os.path.abspath(__file__)),
            capture_output=True, 
            text=True, 
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            print("✅ SUCCESS: Example completed successfully!")
            print("\n📊 EXAMPLE OUTPUT:")
            print("-" * 60)
            # Show last 30 lines of output to avoid overwhelming
            output_lines = result.stdout.split('\n')
            for line in output_lines[-30:]:
                if line.strip():
                    print(line)
            print("-" * 60)
        else:
            print("❌ FAILED: Example failed with errors!")
            print(f"Exit code: {result.returncode}")
            print("\n🔴 ERROR OUTPUT:")
            print("-" * 60)
            print(result.stderr)
            if result.stdout:
                print("\n📝 STDOUT OUTPUT:")
                print(result.stdout)
            print("-" * 60)
            
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏰ TIMEOUT: Example took too long to complete (>5 minutes)")
        return False
    except Exception as e:
        print(f"💥 EXCEPTION: Unexpected error running example: {e}")
        return False

def main():
    """Run all CRUD examples in sequence"""
    print("🚀 ODIN SDK - Comprehensive CRUD Examples Runner")
    print("=" * 80)
    print("📋 Running all CRUD examples for Projects, Knowledge Base, Agents, and Chats")
    print("🏠 Using localhost:8001 with local API keys")
    print("⏱️  Each example has a 5-minute timeout")
    print("=" * 80)
    
    # Define all examples to run
    examples = [
        ("projects_crud.py", "Projects CRUD Operations"),
        ("knowledgebase_crud.py", "Knowledge Base CRUD Operations"),
        ("agents_crud.py", "Agents CRUD Operations"),
        ("chats_crud.py", "Chats CRUD Operations")
    ]
    
    results = {}
    start_time = time.time()
    
    print(f"🎯 Starting execution of {len(examples)} examples...")
    print()
    
    # Run each example
    for i, (script, description) in enumerate(examples, 1):
        print(f"\n🔄 [{i}/{len(examples)}] Starting: {description}")
        
        example_start_time = time.time()
        success = run_example(script, description)
        example_duration = time.time() - example_start_time
        
        results[script] = {
            "success": success,
            "duration": example_duration,
            "description": description
        }
        
        if success:
            print(f"✅ [{i}/{len(examples)}] Completed in {example_duration:.1f}s: {description}")
        else:
            print(f"❌ [{i}/{len(examples)}] Failed after {example_duration:.1f}s: {description}")
        
        # Brief pause between examples
        if i < len(examples):
            time.sleep(2)
    
    # Print comprehensive summary
    total_duration = time.time() - start_time
    successful_examples = sum(1 for r in results.values() if r["success"])
    
    print("\n" + "=" * 80)
    print("📊 COMPREHENSIVE RESULTS SUMMARY")
    print("=" * 80)
    
    print(f"⏱️  Total execution time: {total_duration:.1f} seconds")
    print(f"✅ Successful examples: {successful_examples}/{len(examples)}")
    print(f"❌ Failed examples: {len(examples) - successful_examples}/{len(examples)}")
    print()
    
    print("📋 DETAILED RESULTS:")
    print("-" * 80)
    for script, result in results.items():
        status = "✅ SUCCESS" if result["success"] else "❌ FAILED"
        duration = result["duration"]
        description = result["description"]
        print(f"{status:<12} | {duration:>6.1f}s | {script:<25} | {description}")
    print("-" * 80)
    
    # Overall assessment
    if successful_examples == len(examples):
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("✨ The ODIN SDK is working perfectly with all CRUD operations")
        print("🚀 You can now use these examples as templates for your own applications")
    elif successful_examples > 0:
        print(f"⚡ {successful_examples} out of {len(examples)} examples completed successfully")
        print("💡 Review the failed examples and check your API server status")
        print("🔧 Most issues are typically related to server connectivity or configuration")
    else:
        print("🚨 ALL EXAMPLES FAILED!")
        print("🔧 Please check:")
        print("   - API server is running on localhost:8001")
        print("   - API key and secret are correct")
        print("   - Network connectivity is working")
        print("   - ODIN SDK dependencies are installed")
    
    print()
    print("📖 For more information, check individual example files:")
    for script, _ in examples:
        print(f"   📄 {script}")
    
    print("\n" + "=" * 80)
    return successful_examples == len(examples)

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n🛑 Execution interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error in main runner: {e}")
        sys.exit(1) 