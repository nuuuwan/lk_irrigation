# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_21:14:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 21:14:47 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-25 21:13:34 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-25 21:11:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.017 |  |
| 2025-12-25 21:11:04 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.562 | 🔺 Rising |
| 2025-12-25 21:09:57 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.027 |  |
| 2025-12-25 21:09:11 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2025-12-25 21:08:57 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-25 21:08:48 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2025-12-25 21:08:46 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.011 |  |
| 2025-12-25 21:07:59 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:07:30 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.009 |  |
| 2025-12-25 21:07:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:07:03 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.084 |  |
| 2025-12-25 21:06:30 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-25 21:05:37 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 21:05:26 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.039 |  |
| 2025-12-25 21:05:22 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 21:05:17 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.060 |  |
| 2025-12-25 21:05:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:05:14 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 21:04:46 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2025-12-25 21:04:42 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.052 |  |
| 2025-12-25 21:04:11 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-25 21:03:59 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2025-12-25 21:03:39 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:03:14 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.037 |  |
| 2025-12-25 21:03:06 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 21:02:49 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:02:36 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:02:13 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:01:45 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-25 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:01:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:00:51 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 21:00:46 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -0.011 |  |
| 2025-12-25 21:00:19 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.012 |  |
| 2025-12-25 20:26:53 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 21:11:04 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.562 | 🔺 Rising |
| 2025-12-25 21:06:30 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 21:08:57 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-25 21:05:37 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 21:00:51 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 21:03:06 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 21:05:14 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 21:05:22 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 21:02:13 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:02:36 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:02:49 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:01:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:05:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:07:59 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:03:39 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:07:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:14:47 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-25 21:09:11 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-25 21:07:30 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.009 |  |
| 2025-12-25 21:04:11 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-25 21:01:45 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-25 21:03:59 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2025-12-25 21:04:46 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2025-12-25 21:08:46 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.011 |  |
| 2025-12-25 21:00:46 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -0.011 |  |
| 2025-12-25 21:00:19 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.012 |  |
| 2025-12-25 21:13:34 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-25 21:11:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.017 |  |
| 2025-12-25 21:09:57 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.027 |  |
| 2025-12-25 21:03:14 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.037 |  |
| 2025-12-25 21:05:26 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.039 |  |
| 2025-12-25 21:04:42 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.052 |  |
| 2025-12-25 21:05:17 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.060 |  |
| 2025-12-25 21:07:03 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.084 |  |
| 2025-12-25 21:08:48 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)