# recommendation.py

from api.user.models import BusinessProfile, InfluencerProfile
import numpy as np

# Example constants
PLATFORM_LIST = ['Instagram', 'TikTok', 'YouTube']
AGE_LIST = ['13-17','18-24','25-34','35-44','45-54','55+']

def recommend_influencers(business: BusinessProfile, top_n=5):
    """
    Returns a list of top N influencers recommended for the given business
    using a scoring system based on profile matching.
    """
    influencers = InfluencerProfile.objects.all()
    recommendations = []

    for influencer in influencers:
        score = 0

        # 1. Industry/Niche match
        score += 2 if influencer.niche.lower() == business.industry.lower() else 0

        # 2. Platform overlap
        platform_overlap = len(set(influencer.platforms) & set(business.target_platforms))
        score += platform_overlap

        # 3. Audience age overlap
        age_overlap = len(set(influencer.audience_age) & set(business.target_age))
        score += age_overlap

        # 4. Location match
        score += 1 if influencer.audience_location.lower() == business.target_location.lower() else 0

        # 5. Engagement bonus (normalized)
        max_followers = max([inf.followers for inf in influencers]) or 1
        max_engagement = max([inf.engagement_rate for inf in influencers]) or 1
        engagement_score = 0.5 * (influencer.followers / max_followers + influencer.engagement_rate / max_engagement)
        score += engagement_score

        # 6. Optional: Reviews bonus
        # We'll create a simple review system where past reviews give +1 per positive review
        # For demo, we can mock random reviews
        positive_reviews = getattr(influencer, 'positive_reviews', 0)
        score += positive_reviews * 1

        recommendations.append((influencer, score))

    # Sort by score descending
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Return top N influencers
    return [inf for inf, s in recommendations[:top_n]]
