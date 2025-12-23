# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_17:13:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,878 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 17:13:28 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:09:15 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-23 17:08:51 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:08:48 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.028 |  |
| 2025-12-23 17:08:39 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.019 |  |
| 2025-12-23 17:07:57 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2025-12-23 17:07:34 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2025-12-23 17:07:33 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:06:33 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:06:04 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:05:51 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:05:28 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-23 17:05:28 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.021 |  |
| 2025-12-23 17:05:20 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:05:08 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.069 |  |
| 2025-12-23 17:04:58 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:04:53 | Manampitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.049 |  |
| 2025-12-23 17:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.058 |  |
| 2025-12-23 17:04:16 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2025-12-23 17:04:02 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | -0.038 |  |
| 2025-12-23 17:03:55 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:44 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-23 17:03:40 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:31 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:15 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 17:03:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:02:46 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:02:21 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-23 17:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:50 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:15 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.041 |  |
| 2025-12-23 17:01:13 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:07 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:00:39 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -36.000 |  |
| 2025-12-23 17:00:38 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -36.000 |  |
| 2025-12-23 17:00:30 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 17:00:08 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-23 16:58:56 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 16:58:56 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-23 17:09:15 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-23 17:02:21 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 17:00:30 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 17:03:15 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 17:01:13 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:00:08 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:05:51 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:50 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:07:33 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:06:04 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:40 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:06:33 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:01:07 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:08:51 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:55 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:03:31 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:04:58 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:05:20 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 17:07:34 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2025-12-23 17:05:28 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-23 17:13:28 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:02:46 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:03:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2025-12-23 17:07:57 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2025-12-23 17:08:39 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.019 |  |
| 2025-12-23 17:04:16 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2025-12-23 17:03:44 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-23 17:05:28 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.021 |  |
| 2025-12-23 17:08:48 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.028 |  |
| 2025-12-23 17:04:02 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | -0.038 |  |
| 2025-12-23 17:01:15 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.041 |  |
| 2025-12-23 17:04:53 | Manampitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.049 |  |
| 2025-12-23 17:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.058 |  |
| 2025-12-23 17:05:08 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.069 |  |
| 2025-12-23 17:00:39 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)