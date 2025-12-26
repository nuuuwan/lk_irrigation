# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_19:10:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 19:10:25 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:10:11 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2025-12-26 19:07:52 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.019 |  |
| 2025-12-26 19:06:43 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.042 |  |
| 2025-12-26 19:06:23 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:06:09 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:05:57 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:05:49 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:04:50 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.048 |  |
| 2025-12-26 19:04:22 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:04:11 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-26 19:04:00 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:03:57 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:03:43 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:03:25 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.038 |  |
| 2025-12-26 19:03:17 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:03:01 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 19:02:59 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:02:33 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:02:26 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-26 19:02:16 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:02:11 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:01:54 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-26 19:01:41 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2025-12-26 19:01:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:01:30 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:01:30 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.031 |  |
| 2025-12-26 19:00:55 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-26 19:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:00:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:16:19 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.038 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:14:55 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-26 18:13:25 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 19:02:26 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-26 18:14:55 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-26 19:03:01 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 19:03:43 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:02:16 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:02:11 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 17:58:26 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:05:49 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:05:57 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:03:17 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:02:59 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:03:57 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:00:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:02:33 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:01:30 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:04:00 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:06:23 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:06:09 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:10:25 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:01:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:04:22 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 19:10:11 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2025-12-26 18:11:54 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2025-12-26 19:04:11 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-26 18:01:40 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-26 19:01:54 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-26 18:06:41 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-26 19:00:55 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-26 19:07:52 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.019 |  |
| 2025-12-26 19:01:41 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2025-12-26 18:05:51 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-26 19:01:30 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.031 |  |
| 2025-12-26 18:04:22 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.033 |  |
| 2025-12-26 19:03:25 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.038 |  |
| 2025-12-26 19:06:43 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.042 |  |
| 2025-12-26 19:04:50 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.048 |  |
| 2025-12-26 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)