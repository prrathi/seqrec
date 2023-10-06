import argparse

def parse():

    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', required=True, help='amazon/amazon_tool | amazon/amazon_office | douban/douban_movie | douban/douban_music | epinions/epinions')
    parser.add_argument('--train_dir', default='test', type=str, help='directory to write model to')
    parser.add_argument('--batch_size', default=128, type=int)
    parser.add_argument('--lr', default=0.001, type=float)
    parser.add_argument('--wd', default=1e-5, type=float)
    parser.add_argument('--maxlen', default=200, type=int)
    parser.add_argument('--hidden_units', default=50, type=int)
    parser.add_argument('--num_blocks', default=2, type=int)
    parser.add_argument('--num_epochs', default=80, type=int)
    parser.add_argument('--epoch_test', default=4, type=int)
    parser.add_argument('--num_heads', default=1, type=int)
    parser.add_argument('--dropout_rate', default=0.2, type=float)
    parser.add_argument('--l2_emb', default=0.0, type=float, help = 'weight of l2 loss of embedding')
    parser.add_argument('--device', default='cuda', type=str)
    parser.add_argument('--train_only',  action='store_true')
    parser.add_argument('--inference_only',  action='store_true')
    parser.add_argument('--save_neg',  action='store_true')
    parser.add_argument('--mode', default='test', type=str, help='valid | test')
    parser.add_argument('--prev_time',  action='store_true')
    parser.add_argument('--no_valid_in_test',  action='store_true')
    parser.add_argument('--state_dict_path', default=None, type=str)
    parser.add_argument('--model', default='newrec', type=str, help='newrec | mostpop | sasrec | bert4rec | bprmf')
    parser.add_argument('--monthpop', default='wtembed', type=str, help='format of month popularity: wtembed (time-weighted) | currembed (current month) | cumembed (cumulative)')
    parser.add_argument('--weekpop', default='week_embed2', type=str, help='format of week popularity: current is 4-week popularity')
    parser.add_argument('--use_week_eval',  action='store_true')
    parser.add_argument('--week_eval_pop', default='week_wt_embed_adj', type=str, help='modified week popularity for evaluation only')
    parser.add_argument('--rawpop', default='rawpop', type=str, help='format of popularity for mostpop model: rawpop (cumulative) | rawcurrpop (current)')
    parser.add_argument('--userpop', default='lastuserpop', type=str, help='ultimate user popularity used if eval_quality true')
    parser.add_argument('--base_dim1', default=11, type=int, help='dimension of month popularity vector, newrec only')
    parser.add_argument('--input_units1', default=132, type=int, help='base_dim1 * number of months considered, newrec only')
    parser.add_argument('--base_dim2', default=6, type=int, help='dimension of week popularity vector, newrec only')
    parser.add_argument('--input_units2', default=6, type=int, help='base_dim2 * number of 4 week groups considered, newrec only')
    parser.add_argument('--mask_prob', default=0, type=float, help='cloze task, bert4rec only')
    parser.add_argument('--seed', default=2023, type=int)
    parser.add_argument('--topk','--list', nargs='+', default=[10, 5, 1], type=int, help='# items for evaluation')
    parser.add_argument('--augment', action='store_true', help='use data augmentation, newrec only')
    parser.add_argument('--augfulllen', default=0, type=int, help='length of full user history then split into augmented parts, 0 indicates no cutoff')
    parser.add_argument('--transfer', action='store_true', help='zero-shot transfer, newrec only')
    parser.add_argument('--fs_transfer', action='store_true', help='few-shot transfer, newrec only')
    parser.add_argument('--fs_num_epochs', default=1, type=int, help='number of training  epochs for few-shot transfer')
    parser.add_argument('--fs_prop', default=1.0, type=float, help='percent of target data for few shot, newrec only')
    parser.add_argument('--loss_size', default=250, type=int, help='ratio of items used in loss, newb4rec only')
    parser.add_argument('--max_split_size', default=-1.0, type=float)
    parser.add_argument('--no_emb', action='store_true', help='for now, available in newrec only')
    parser.add_argument('--no_fixed_emb', action='store_true', help='for now, available in newrec only')
    parser.add_argument('--eval_method', default=1, type=int, help='1: random 100-size subset, 2: popularity 100-size subset, 3: full set')
    parser.add_argument('--eval_quality', action='store_true', help='evaluate across groups of user popularity')
    parser.add_argument('--quality_size', default=20, type=int, help='percentile size of group if eval_quality is True')
    parser.add_argument('--triplet_loss', action='store_true', help='triplet regularization loss on user final embeddings using trajectory')
    parser.add_argument('--cos_loss', action='store_true', help='cosine regularization loss on user final embeddings using trajectory')
    parser.add_argument('--reg_file', default='userhist', type=str, help='user vectors used in reg loss')
    parser.add_argument('--reg_num', default=10, type=int, help='# of positive and negative examples per user per batch for reg loss')
    parser.add_argument('--reg_coef', default=1.0, type=float, help='weight for regularization loss')
    parser.add_argument('--only_reg', action='store_true', help='only reg loss')
    parser.add_argument('--itemgrp', action='store_true', help='use item co-occurrence')
    parser.add_argument('--itemgrp_file', default='copca', type=str, help='features for item co-occurrence')
    parser.add_argument('--traj_form', default='', type=str, help='model form to use for traj_form, default is no model: mlp (separate model gated after) | attention (incorporated into sequence)')
    parser.add_argument('--traj_file', default='userhist', type=str, help='user trajectories used for gating')
    parser.add_argument('--traj_dim', default=100, type=int, help='original size of trajectory')
    parser.add_argument('--traj_perc', default=100, type=int, help='scale from 1 to traj_perc to use for user percentile encoding')
    parser.add_argument('--traj_enc_type', default='sin', help='type of encoding to use for trajectory if traj_form = attention, sin (sinusoidal) | lin (linear bin)')
    parser.add_argument('--comb', action='store_true', help='combine user info for ground truth embedding comparison')
    parser.add_argument('--pause', action='store_true', help='pause')
    parser.add_argument('--dataset2', default='', type=str, help='second dataset to train on, newrec only')
    parser.add_argument('--lag', default=1, type=int, help='time lag for prediction, newrec only')
    parser.add_argument('--time_embed', action='store_true', help='add relative time-based embedding, similar to positional')
    parser.add_argument('--time_no_fixed_embed', action='store_true', help='learnable positional embedding, same as no_fixed_emb but for time')
    parser.add_argument('--time_embed_concat', action='store_true', help='concatenate (not add) time embed')
    parser.add_argument('--save_scores', action='store_true', help='save raw scores')
    parser.add_argument('--use_scores', action='store_true', help='use saved scores')
    parser.add_argument('--use_score_dir', default='', type=str, help='dir for use saved scores')
    parser.add_argument('--alphas', nargs='+', default=[0.2, 0.4, 0.5, 0.6, 0.8], type=float, help='use saved scores')
    parser.add_argument('--pause_size', action='store_true', help='pause to check size')
    parser.add_argument('--sparse', action='store_true', help='pause to check size')
    parser.add_argument('--save_ranks', action='store_true', help='save user prediction ranks and exit')
    parser.add_argument('--ranks_name', default='ranks', type=str, help='file name that save_ranks goes to')

    args = parser.parse_args()
    return args