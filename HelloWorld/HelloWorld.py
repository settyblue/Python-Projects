print 'Hello World'
import math

def computeEntropy(cluster_labels, topics):
    number_of_clusters = max(cluster_labels)
    number_of_docs = len(topics)
    count = 0
    entropy = [0]*number_of_clusters
    cluster_size = [0]*number_of_clusters
    for i in range(0,len(cluster_labels)):
        if cluster_labels[i] !=  -1:
            count += 1;
            cluster_size[cluster_labels[i]-1] += 1
    print 'number of clusters : ',number_of_clusters
    print 'cluster sizes : ', cluster_size
    number_of_topics = len(set(topics))
    print 'number of docs : ',number_of_docs
    print 'number of topics : ',number_of_topics
    for i in range(0,number_of_clusters):
        topics_count = {}
        print 'iterating for the cluster : ',i+1
        for j in range(0,number_of_docs):
            if cluster_labels[j] == i+1:
                if topics_count.has_key(topics[j]) == False:
                    topics_count[topics[j]] = 0
                topics_count[topics[j]] += 1
        print topics_count
        for key in topics_count:
            p = topics_count[key]/float(cluster_size[i])
            print 'probability = ',p
            entropy[i] += (-1)*p*math.log(p,2)

    total_entropy = 0;
    for i in range(0,number_of_clusters):
        print 'entropy of cluster ',i,' is ',entropy[i]
        total_entropy += entropy[i]*cluster_size[i]

    print 'number of documents : ',count
    return total_entropy/count

##main starts here
topics_count = {}
topics_count['Hello'] = 'World';
print topics_count
m = computeEntropy([1,2,1,2,1],['hello','hello','world','world','yo'])
print 'entropy is ', m
