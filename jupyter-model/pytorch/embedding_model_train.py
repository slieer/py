import os
import numpy as np
import pandas as pd
from torch.utils.data import Dataset,DataLoader
import torch
import torch.nn as nn
import logging
from tqdm import trange
import transformer_utils
 
logger = logging.getLogger('Transformer.Embedding')
 
class EmbeddingTrainDataset(Dataset):
    def __init__(self, matrix_data):
        self.train_data = matrix_data
        self.train_len = len(matrix_data)
 
    def __len__(self):
        return self.train_len
 
    def __getitem__(self, index):
        return self.train_data[index], self.train_data[index]
 
 
class AutoEncoder(nn.Module):
    def __init__(self, input_dim, embedding_dim):
        super(AutoEncoder, self).__init__()
 
 
 
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, input_dim // 2),
            nn.Tanh(),
            nn.Linear(input_dim // 2, input_dim // 4),
            nn.Tanh(),
            nn.Linear(input_dim // 4, embedding_dim),
 
        )
        self.decoder = nn.Sequential(
 
            nn.Linear(embedding_dim, input_dim // 4),
            nn.Tanh(),
            nn.Linear(input_dim // 4, input_dim // 2),
            nn.Tanh(),
            nn.Linear(input_dim // 2, input_dim),
        )
 
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded
 
 
if __name__ == '__main__':
    embedding_dim = 100
    epochs = 10000
    lr = 0.001
    gamma = 0.95
    batch_size = 1000
 
    transformer_utils.log(os.path.join(os.getcwd(), 'train.log'))
    data_frame = pd.read_csv(os.path.join(os.getcwd(), 'data', 'abs_sku_to_Car_classfication_onehot_detail.csv'), header=None,
                             names=['sku_code', 'car_model', 'car_id', 'cat_id'], dtype={0: str, 1: str, 2: int, 3: int})
    sku_code_set = set(data_frame['sku_code'].drop_duplicates())
    sku2idx_dict = {}
 
    for i, sku_code in enumerate(sku_code_set):
        sku2idx_dict[sku_code] = i
    car_id_num = max(data_frame['car_id'])
    sku_code_num = len(sku_code_set)
    sku_code_car_matrix = np.zeros((sku_code_num, car_id_num), dtype='float32')
    np.save(os.path.join(os.getcwd(), 'data', 'sku2idx_dict'), sku2idx_dict)
 
 
 
    for i in trange(len(data_frame)):
        sku_code = data_frame.loc[i, 'sku_code']
        car_id = data_frame.loc[i, 'car_id']
 
        sku_code_idx = sku2idx_dict[sku_code]
        sku_code_car_matrix[sku_code_idx, car_id - 1] = 1
 
    train_set = EmbeddingTrainDataset(sku_code_car_matrix)
    train_loader = DataLoader(train_set, batch_size=batch_size, num_workers=0, shuffle=False)
 
    device = "cuda" if torch.cuda.is_available() else "cpu"
    autoencoder_model = AutoEncoder(car_id_num, embedding_dim).to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.AdamW(autoencoder_model.parameters(), lr=lr)
 
    train_loss_summary = np.zeros(epochs)
    best_evaluate_loss = 100.0
    for epoch in trange(epochs):
 
        train_total_loss = 0
        sku_encoder_embedding = np.zeros((sku_code_num, embedding_dim), dtype='float32')
        train_loader_len = len(train_loader)
 
        for i, (x_input, x_label) in enumerate(train_loader):
            x_input = x_input.to(device)
            x_label = x_label.to(device)
 
            encoded, decoded = autoencoder_model(x_input)
            loss = criterion(decoded, x_label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            train_total_loss += loss.item()
 
            sku_encoder_embedding[(i * batch_size) : (i * batch_size + x_input.shape[0])] = encoded.detach().to('cpu').numpy()
 
        train_avg_loss = train_total_loss / train_loader_len
        logger.info(f'epoch: {epoch + 1}, train_loss: {train_avg_loss}')
 
        is_best = False
        if train_avg_loss < best_evaluate_loss:
            is_best = True
            best_evaluate_loss = train_avg_loss
            np.save(os.path.join(os.getcwd(), 'data', 'sku2embedding'), sku_encoder_embedding)
            logger.info(f'best embedding at: {epoch + 1}')
 
        if epoch >= 10:  # 太前面的去掉，免得影响后面曲线的可观测性
            train_loss_summary[epoch] = train_avg_loss
        if epoch % 10 == 1:
            transformer_utils.plot_all_epoch(train_loss_summary, train_loss_summary, epoch, 'embedding_train_loss_summary.png')
 
    print('finish!')