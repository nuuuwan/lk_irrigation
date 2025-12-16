# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_22:23:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,846 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 22:23:42 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:14:39 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:12:18 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-16 22:10:18 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:09:53 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2025-12-16 22:08:28 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2025-12-16 22:08:10 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:07:49 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 22:07:39 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-16 22:06:10 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-16 22:05:25 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2025-12-16 22:05:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-16 22:05:09 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-16 22:04:47 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 22:04:34 | Peradeniya (Mahaweli Ganga) | 2.77 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-16 22:04:02 | Yaka Wewa (Ma Oya) | 1.41 | 🟢 Normal | -0.038 |  |
| 2025-12-16 22:03:58 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.025 |  |
| 2025-12-16 22:03:48 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:03:22 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:03:19 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:03:18 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:49 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:33 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:31 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 22:02:23 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:23 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-16 22:02:01 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:01:31 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:01:10 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.013 |  |
| 2025-12-16 22:00:43 | Horowpothana (Yan Oya) | 6.04 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2025-12-16 22:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:00:27 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:00:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 22:00:43 | Horowpothana (Yan Oya) | 6.04 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2025-12-16 22:02:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-16 22:04:34 | Peradeniya (Mahaweli Ganga) | 2.77 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-16 22:12:18 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-16 22:05:09 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-16 21:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-16 22:02:31 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 22:04:47 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 22:07:39 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-16 22:07:49 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 22:02:23 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:23 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:01:31 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:23:42 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:49 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:03:18 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:33 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:00:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:10:18 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:03:22 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:08:10 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:02:01 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:14:39 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:03:48 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:00:27 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:03:19 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:08:28 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2025-12-16 22:06:10 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-16 22:05:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-16 21:05:09 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2025-12-16 22:09:53 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2025-12-16 22:01:10 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.013 |  |
| 2025-12-16 22:05:25 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2025-12-16 22:03:58 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.025 |  |
| 2025-12-16 22:04:02 | Yaka Wewa (Ma Oya) | 1.41 | 🟢 Normal | -0.038 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)