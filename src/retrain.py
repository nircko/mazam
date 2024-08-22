from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader

# Noralize the RGB channels based on recomended value pytorch


def load_spectrogram(image_path):
    # Load the spectrogram image
    image = Image.open(image_path).convert('RGB')

    # Preprocess the image for the model (e.g., resize, normalize)
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    image = preprocess(image)
    return image


#Prepare a dataset of spectrograms with corresponding speaker labels and create a DataLoader for training

class SpectrogramDataset(Dataset):
    def __init__(self, image_paths, labels):
        self.image_paths = image_paths
        self.labels = labels

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image = load_spectrogram(self.image_paths[idx])
        label = self.labels[idx]
        return image, label



# Assuming you have lists of image paths and labels
image_paths = [] # train spectrogram png files
labels = [0, 1]  # corresponding labels for each singer, Joni Mitchell is 1 in my example

# Create dataset and data loader
batch_size=16
dataset = SpectrogramDataset(image_paths, labels)
train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Retrain the model
num_classes = len(set(labels))  # Number of speakers
model = retrain_model(train_loader, num_classes)
def predict_speaker(model, image_path):
    model.eval()
    image = load_spectrogram(image_path)
    image = image.unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)

    return predicted.item()



predicted_speaker = predict_speaker(model, 'test_spectrogram.png')
print(f"Predicted Speaker ID: {predicted_speaker}")