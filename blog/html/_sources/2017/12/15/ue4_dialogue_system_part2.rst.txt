UE4 Dialogue System Part2
=========================

Part1_

In this part, we will create a new asset type: **DialogueSession**.

Step 1
------

* Create header files: "DialogueSession.h", "DialogueSessionNode.h", "DialogueSessionEdge.h" in your {ProjectRoot}/Source/{ProjectName}/Public folder
* Create source files: "DialogueSession.cpp", "DialogueSessionNode.cpp" in your {ProjectRoot}/Source/{ProjectName}/Private folder
* Regenerate solution file
* Open solution file

now your solution should looks like this:

.. image:: images/sln_with_dialogue_session.png

Step 2
------

Edit {YourProject}.Build.cs, add a dependency: **GenericGraphRuntime**

.. code-block:: c#

    PrivateDependencyModuleNames.AddRange(new string[] { "GenericGraphRuntime" });

Step 3
------

Implement class: UDialogueSessionNode

DialogueSessionNode.h

.. code-block:: c++

    #pragma once

    #pragma once

    #include "CoreMinimal.h"
    #include "GenericGraphNode.h"
    #include "DialogueSessionNode.generated.h"

    UENUM(BlueprintType)
    enum class EDialoguerPostion : uint8
    {
        Left,
        Right
    };

    UCLASS(Blueprintable)
    class UDialogueSessionNode : public UGenericGraphNode
    {
        GENERATED_BODY()
    public:
        UDialogueSessionNode();

        UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DialogueSession")
        FText Paragraph;

        UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DialogueSession")
        EDialoguerPostion DialoguerPostion;

    #if WITH_EDITOR
        virtual FText GetNodeTitle() const override;

        virtual void SetNodeTitle(const FText& NewTitle) override;

        virtual FLinearColor GetBackgroundColor() const override;
    #endif
    };

DialogueSessionNode.cpp

.. code-block:: c++

    #include "DialogueSessionNode.h"
    #include "DialogueSession.h"

    #define LOCTEXT_NAMESPACE "DialogueSessionNode"

    UDialogueSessionNode::UDialogueSessionNode()
    {
    #if WITH_EDITORONLY_DATA
        CompatibleGraphType = UDialogueSession::StaticClass();

        ContextMenuName = LOCTEXT("ConextMenuName", "Dialogue Session Node");
    #endif
    }

    #if WITH_EDITOR

    FText UDialogueSessionNode::GetNodeTitle() const
    {
        return Paragraph.IsEmpty() ? LOCTEXT("EmptyParagraph", "(Empty paragraph)") : Paragraph;
    }

    void UDialogueSessionNode::SetNodeTitle(const FText& NewTitle)
    {
        Paragraph = NewTitle;
    }

    FLinearColor UDialogueSessionNode::GetBackgroundColor() const
    {
        UDialogueSession* Graph = Cast<UDialogueSession>(GetGraph());

        if (Graph == nullptr)
            return Super::GetBackgroundColor();

        switch (DialoguerPostion)
        {
        case EDialoguerPostion::Left:
            return Graph->LeftDialoguerBgColor;
        case EDialoguerPostion::Right:
            return Graph->RightDialoguerBgColor;
        default:
            return FLinearColor::Black;
        }
    }

    #endif

    #undef LOCTEXT_NAMESPACE

We extended the *UGenericGraphNode*, added two properties to the node:

* *Paragraph*: the dialogue content
* *DialoguerPostion*: indicate the dialoguer's position(left or right).

Override the *GetNodeTitle* and *SetNodeTitle* method to use the Paragraph property as the node title.

Override the *GetBackgroundColor* method, change the node's background color by dialoguer's position

Step 4
------

Implement class: UDialogueSessionEdge

DialogueSessionEdge.h

.. code-block:: c++

    #pragma once

    #include "CoreMinimal.h"
    #include "GenericGraphEdge.h"
    #include "DialogueSessionEdge.generated.h"


    UCLASS(Blueprintable)
    class UDialogueSessionEdge: public UGenericGraphEdge
    {
        GENERATED_BODY()

    public:
        UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "DialogueSession")
        FText Selection;
    };

We extended the *UDialogueSessionEdge*, added a *Selection* property, this will be used to implment dialogue branch.

Step 5
------

Implement class: UDialogueSession

DialogueSession.h:

.. code-block:: c++

    #pragma once

    #include "CoreMinimal.h"
    #include "GenericGraph.h"
    #include "DialogueSession.generated.h"

    UCLASS(Blueprintable)
    class DIALOGUESYSTEM_API UDialogueSession: public UGenericGraph
    {
        GENERATED_BODY()

    public:
        UDialogueSession();

        UPROPERTY(EditDefaultsOnly, Category = "DialogueSession")
        FLinearColor LeftDialoguerBgColor;

        UPROPERTY(EditDefaultsOnly, Category = "DialogueSession")
        FLinearColor RightDialoguerBgColor;
    };

DialogueSession.cpp

.. code-block:: c++

    #include "DialogueSession.h"
    #include "DialogueSessionNode.h"
    #include "DialogueSessionEdge.h"

    #define LOCTEXT_NAMESPACE "DialogueSession"

    UDialogueSession::UDialogueSession()
    {
        NodeType = UDialogueSessionNode::StaticClass();
        EdgeType = UDialogueSessionEdge::StaticClass();

        LeftDialoguerBgColor = FLinearColor::Black;
        RightDialoguerBgColor = FLinearColor(0.93f, 0.93f, 0.93f, 1.f);

        Name = "DialogueSession";
    }

    #undef LOCTEXT_NAMESPACE

We created a class *UDialogueSession* which inherit from *UGenericGraph*, this class will be the new asset type.

.. warning:: DIALOGUESYSTEM_API should changed to {YOURPROJECT}_API.

Step 6
------

We need to create an asset factory which inherit from *UFactory*, but this class can't add to your game project directly, because *UFactory* are in the module **UnrealEd**, this is an editor module,
you can't pass the Shipping build if your game depends on any editor module.

Solution: creating an editor module for your game project, here is an tutorial_.

After created an editor module, creating "DialogueSessionFactory.h" and "DialogueSessionFactory.cpp" in {YourProject}/Source/{YourProjectEditor}/Private and regenerate solution file.

Your solution should looks like this now:

.. image:: images/sln_with_editor.png

Step 7
------

Edit the {YourProjectEditor}.Build.cs, add dependency module: *UnrealEd*, *GenericGraphRuntime*, *{YourGameProject}* and include path: *{YourGameProject}/Public*

.. code-block:: c#

    PublicIncludePaths.AddRange(new string[]{"DialogueSystem/Public"});

    PrivateDependencyModuleNames.AddRange(new string[] { "UnrealEd", "GenericGraphRuntime", "DialogueSystem" });

Step 8
------

Implement DialogueSessionFactory

DialogueSessionFactory.h

.. code-block:: c++

    #pragma once

    #include "CoreMinimal.h"
    #include "Factories/Factory.h"
    #include "DialogueSessionFactory.generated.h"

    UCLASS()
    class UDialogueSessionFactory : public UFactory
    {
        GENERATED_BODY()

    public:
        UDialogueSessionFactory();

        virtual UObject* FactoryCreateNew(UClass* Class, UObject* InParent, FName Name, EObjectFlags Flags, UObject* Context, FFeedbackContext* Warn) override;
        virtual FText GetDisplayName() const override;
        virtual FString GetDefaultNewAssetName() const override;
    };

DialogueSessionFactory.cpp

.. code-block:: c++

    #include "DialogueSessionFactory.h"
    #include "DialogueSession.h"

    #define LOCTEXT_NAMESPACE "DialogueSessionFactory"

    UDialogueSessionFactory::UDialogueSessionFactory()
    {
        bCreateNew = true;
        bEditAfterNew = true;
        SupportedClass = UDialogueSession::StaticClass();
    }

    UObject* UDialogueSessionFactory::FactoryCreateNew(UClass* Class, UObject* InParent, FName Name, EObjectFlags Flags, UObject* Context, FFeedbackContext* Warn)
    {
        return NewObject<UObject>(InParent, Class, Name, Flags | RF_Transactional);
    }

    FText UDialogueSessionFactory::GetDisplayName() const
    {
        return LOCTEXT("FactoryName", "Dialogue Session");
    }

    FString UDialogueSessionFactory::GetDefaultNewAssetName() const
    {
        return "DialogueSession";
    }

    #undef LOCTEXT_NAMESPACE 

Step 9
------

Compile the solution, open the editor if compile succeeded. right click in your content browser, you can create DialogueSession asset now.

.. thumbnail:: images/dialogue_session_asset.png

Done
----

That’s all in this part, you have created a new asset type [#f1]_ **DialogueSession** and extended GenericGraph's node and edge type.

In the next part, we will dive into blueprint :)

.. [#f1] a new graph type with GenericGraph editor

.. _Part1: https://jinyuliao.github.io/blog/html/2017/12/15/ue4_dialogue_system_part1.html
.. _tutorial: https://wiki.unrealengine.com/Creating_an_Editor_Module

.. author:: default
.. categories:: UE4 Dialogue System
.. tags:: UE4, Tutorial
.. comments::