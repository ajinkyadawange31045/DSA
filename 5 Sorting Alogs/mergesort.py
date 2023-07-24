class solution:
    def mergesort(self,arr,low,hi):
        if low>=hi:
            return
        mid = (low+hi)//2
        self.mergesort(arr,low,mid)
        self.mergesort(arr,mid+1,hi)
        self.merge(arr,low,mid,hi)
        return arr
    
    def merge(self,arr,low,mid,hi):
        left = low
        temp = []
        right = mid+1
        while left<=mid and right<=hi:
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left +=1
            else:
                temp.append(arr[right])
                right += 1
        while left<=mid:
            temp.append(arr[left])
            left += 1
        while right<=hi:
            temp.append(arr[right])
            right += 1
        for i in range(low,hi+1):
            arr[i] = temp[i-low]
a = solution()
arr = [3,1,2,10,5,22,6,4]

low = 0
hi = len(arr)-1
print(a.mergesort(arr,low,hi))