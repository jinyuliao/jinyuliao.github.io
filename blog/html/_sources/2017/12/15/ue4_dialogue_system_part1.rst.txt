UE4 Dialogue System Part1
=========================

Introduction
------------

This tutorial create a simple dialogue system in UE4 with my GenericGraph_ plugin.

Prerequisite:

* UE4 version: 4.18.2 or higher
* C++ development enviroment(Visual Studio on Windows or Xcode on Mac)
* Some experience with UE4, can make simple UI with UMG

In this part, we wiil create project and compile the plugin.

Step 1
------

Create a blueprint project with the TopDown template.

.. thumbnail:: images/create_project.png

Step 2
------

Open your porject's root folder, create a folder named "**Plugins**", clone GenericGraph_ into the "**Plugins**" folder.

.. image:: images/clone_plugin.png

Step 3
------

In your editor, click "File->New C++ Class".

.. image:: images/new_cpp.png

Click "Next".

.. thumbnail:: images/class_wizard_01.png

Set the class name to "Placeholder"

.. thumbnail:: images/class_wizard_02.png

Click "Create Class".

Now we create a c++ class: Placeholder, as the name implies, it's a placeholder, we don't need it anymore, we just need a c++ class to generate a c++ project.

Right click your "YourProject.uproject" file, click "Generate Visual Studio project files".

.. image:: images/generate_project.png

Open YourPorject.sln file, you should see the GenericGraph plugin's files now.

.. thumbnail:: images/sln.png

**Close your project editor**, then compile the c++ solution(F7).

Step 4
------

If compile succussed, open your editor again, right click in your content browser, you can create GenericGraph asset now.

.. thumbnail:: images/generic_graph_asset.png

Done
----

That’s all in this part, you have created a project and compiled the GenericGraph plugin, we will add a "DialogueSession" asset in the next part, then say goodbye to c++ and dive into blueprint.

.. _GenericGraph: https://github.com/jinyuliao/GenericGraph

.. author:: default
.. categories:: UE4 Dialogue System
.. tags:: UE4, Tutorial
.. comments::
