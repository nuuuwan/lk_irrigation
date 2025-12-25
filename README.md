# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_20:26:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,788 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 20:26:53 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:14:03 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.018 |  |
| 2025-12-25 20:11:56 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.040 |  |
| 2025-12-25 20:11:15 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:10:42 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:10:10 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:07:45 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2025-12-25 20:07:11 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.038 |  |
| 2025-12-25 20:07:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.056 |  |
| 2025-12-25 20:07:01 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-25 20:06:21 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-25 20:06:19 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-25 20:05:44 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-25 20:05:31 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 20:04:41 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2025-12-25 20:04:38 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:04:37 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:04:37 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.679 |  |
| 2025-12-25 20:04:16 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.052 |  |
| 2025-12-25 20:04:14 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2025-12-25 20:04:08 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-25 20:03:44 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.679 |  |
| 2025-12-25 20:03:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:03:30 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:03:26 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:03:05 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:49 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-25 20:02:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:45 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.072 |  |
| 2025-12-25 20:02:36 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:27 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:03 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:03 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:01 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-25 20:01:58 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.105 |  |
| 2025-12-25 20:01:25 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:01:25 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 20:06:21 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-25 20:07:01 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 20:04:08 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-25 20:05:44 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-25 20:06:19 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-25 20:05:31 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 20:03:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:36 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:27 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:03:30 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:01:58 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:10:42 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:26:53 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:04:37 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:01:25 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:03 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:02:03 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:11:15 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:04:38 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:03:26 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 20:03:05 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-25 20:07:45 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2025-12-25 20:02:49 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-25 20:04:14 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2025-12-25 20:02:01 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-25 20:04:41 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2025-12-25 20:14:03 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.018 |  |
| 2025-12-25 20:01:25 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.021 |  |
| 2025-12-25 20:07:11 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.038 |  |
| 2025-12-25 20:11:56 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.040 |  |
| 2025-12-25 20:04:16 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.052 |  |
| 2025-12-25 20:07:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.056 |  |
| 2025-12-25 20:02:45 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.072 |  |
| 2025-12-25 20:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.105 |  |
| 2025-12-25 20:04:37 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.679 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)