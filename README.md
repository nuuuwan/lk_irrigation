# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_07:22:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,364 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 07:22:35 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.038 |  |
| 2025-12-15 07:19:31 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.045 |  |
| 2025-12-15 07:09:51 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:09:44 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.035 |  |
| 2025-12-15 07:08:17 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 07:07:58 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.049 |  |
| 2025-12-15 07:07:10 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:06:46 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.040 |  |
| 2025-12-15 07:06:29 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:06:15 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2025-12-15 07:05:47 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2025-12-15 07:05:45 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-15 07:05:34 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.032 |  |
| 2025-12-15 07:05:14 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2025-12-15 07:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.064 |  |
| 2025-12-15 07:05:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.070 |  |
| 2025-12-15 07:04:54 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:04:44 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2025-12-15 07:04:08 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 07:03:48 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-15 07:03:42 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.011 |  |
| 2025-12-15 07:02:48 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-15 07:02:42 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.030 |  |
| 2025-12-15 07:02:37 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:02:31 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.035 |  |
| 2025-12-15 07:02:18 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 07:02:08 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-15 07:02:04 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-15 07:01:53 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:01:20 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-15 07:01:09 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-15 07:01:04 | Horowpothana (Yan Oya) | 4.12 | 🟢 Normal | -0.021 |  |
| 2025-12-15 07:01:00 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.003 |  |
| 2025-12-15 07:00:28 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-15 07:00:26 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-15 07:00:11 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.021 |  |
| 2025-12-15 06:32:52 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 06:10:00 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2025-12-15 07:05:45 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-15 07:00:26 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-15 07:01:20 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-15 07:01:09 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-15 07:02:48 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-15 07:04:08 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 07:08:17 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 07:02:18 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 07:01:00 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.003 |  |
| 2025-12-15 07:07:10 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:09:51 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:04:54 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:02:37 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:06:29 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:01:53 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:32:52 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.007 |  |
| 2025-12-15 07:02:04 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-15 07:04:44 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2025-12-15 07:00:28 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-15 07:03:42 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.011 |  |
| 2025-12-15 07:06:15 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2025-12-15 07:02:08 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-15 07:03:48 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-15 07:05:47 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2025-12-15 07:01:04 | Horowpothana (Yan Oya) | 4.12 | 🟢 Normal | -0.021 |  |
| 2025-12-15 07:00:11 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.021 |  |
| 2025-12-15 07:02:42 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.030 |  |
| 2025-12-15 07:05:14 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2025-12-15 07:05:34 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.032 |  |
| 2025-12-15 07:02:31 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.035 |  |
| 2025-12-15 07:09:44 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.035 |  |
| 2025-12-15 07:22:35 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.038 |  |
| 2025-12-15 07:06:46 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.040 |  |
| 2025-12-15 07:19:31 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.045 |  |
| 2025-12-15 07:07:58 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.049 |  |
| 2025-12-15 07:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.064 |  |
| 2025-12-15 07:05:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.070 |  |
| 2025-12-15 06:07:34 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)