```c++
/*
 * FamilyApi.h
 *
 * Basic API Specification
 */

#ifndef FAMILYAPI_FAMILYAPI_H_
#define FAMILYAPI_FAMILYAPI_H_

#include "ApiClient.h"
#include "ModelBase.h"
#include <boost/optional.hpp>

namespace familyapi {

using namespace familyapi::model;

class FamilyApi {
public:
    FamilyApi(std::shared_ptr<const ApiClient> apiClient);
    virtual ~FamilyApi();

    /**
     * Adds a new child
     * 
     * @param body Child object that needs to be added to the store
     * @return void
     */
    pplx::task<void> addChild(std::shared_ptr<Child> body) const;

    /**
     * Returns all available children
     * 
     * @return std::vector<std::shared_ptr<Child>>
     */
    pplx::task<std::vector<std::shared_ptr<Child>>> getChildren() const;

    /**
     * Returns the child with the provided id
     * 
     * @param cid Child id
     * @return std::shared_ptr<Child>
     */
    pplx::task<std::shared_ptr<Child>> getChildById(int32_t cid) const;

    /**
     * Updates the child with the provided id
     * 
     * @param cid Child id
     * @param body Child object that needs to be updated
     * @return std::shared_ptr<Child>
     */
    pplx::task<std::shared_ptr<Child>> updateChild(int32_t cid, std::shared_ptr<Child> body) const;

    /**
     * Deletes the child with the provided id
     * 
     * @param cid Child id
     * @return void
     */
    pplx::task<void> deleteChild(int32_t cid) const;

    /**
     * Returns the parent with the provided id
     * 
     * @param pid Parent id
     * @return std::shared_ptr<Parent>
     */
    pplx::task<std::shared_ptr<Parent>> getParent(int32_t pid) const;

protected:
    std::shared_ptr<const ApiClient> m_ApiClient;
};

}

#endif /* FAMILYAPI_FAMILYAPI_H_ */

```