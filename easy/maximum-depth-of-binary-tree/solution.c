/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if (root == NULL)
        return 0;
    
    int depthLeft = 0;
    int depthRight = 0;

    depthLeft += maxDepth(root->left);
    depthRight += maxDepth(root->right);
    
    if (depthLeft >= depthRight)
        return depthLeft + 1;
    else
        return depthRight + 1;
}