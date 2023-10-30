package InMemoryModel;

import java.util.ArrayList;
import java.util.List;

import ModelEliments.Camera;
import ModelEliments.Flash;
import ModelEliments.PoligonalModel;
import ModelEliments.Scena;

public class ModelStore implements IModelChanger{
    public List<PoligonalModel> Models;
    public List<Scena> Scenes;
    public List<Flash> Flashes;
    public List<Camera> Cameras;
    private IModelChangeObserver[] changeObservers;

    public ModelStore(IModelChangeObserver[] changeObservers) {
        this.changeObservers = changeObservers;
        this.Models = new ArrayList<>();
        this.Scenes = new ArrayList<>();
        this.Flashes = new ArrayList<>();
        this.Cameras = new ArrayList<>();


    }

    public Scena GetScena(int id){
        return Scenes.get(id);
    }

    @Override
    public void NotifyChange(IModelChanger sender) {
       
    }

    
     
}
