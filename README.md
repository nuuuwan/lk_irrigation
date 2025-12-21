# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_17:24:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,108 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 17:24:51 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:22:39 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:13:17 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.018 |  |
| 2025-12-21 17:11:13 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2025-12-21 17:09:06 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2025-12-21 17:06:39 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2025-12-21 17:05:58 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2025-12-21 17:05:41 | Horowpothana (Yan Oya) | 4.71 | 🟢 Normal | -0.065 |  |
| 2025-12-21 17:05:24 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.272 |  |
| 2025-12-21 17:05:10 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2025-12-21 17:05:01 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | -0.020 |  |
| 2025-12-21 17:04:50 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2025-12-21 17:04:28 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:04:26 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.020 |  |
| 2025-12-21 17:04:16 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.148 |  |
| 2025-12-21 17:04:03 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:03:55 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:03:40 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:03:35 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 17:03:18 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 17:02:48 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:02:47 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2025-12-21 17:02:44 | Manampitiya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-21 17:02:43 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.033 |  |
| 2025-12-21 17:02:38 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-21 17:02:23 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:02:19 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:02:05 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.011 |  |
| 2025-12-21 17:01:49 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:36 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:30 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:17 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.086 |  |
| 2025-12-21 17:01:17 | Thanthirimale (Malwathu Oya) | 5.00 | 🟡 Alert | -0.032 |  |
| 2025-12-21 17:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:09 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | -0.051 |  |
| 2025-12-21 17:00:57 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2025-12-21 17:00:16 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:00:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 17:01:17 | Thanthirimale (Malwathu Oya) | 5.00 | 🟡 Alert | -0.032 |  |
| 2025-12-21 17:02:38 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-21 17:02:44 | Manampitiya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-21 17:03:18 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 17:03:35 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 17:01:30 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:04:16 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:24:51 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:02:23 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:03:55 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:02:48 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:02:19 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:36 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:03:40 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:04:03 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:01:49 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:11:13 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2025-12-21 17:04:50 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2025-12-21 17:22:39 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:04:28 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:00:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:00:16 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-21 17:02:05 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.011 |  |
| 2025-12-21 17:05:10 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2025-12-21 17:13:17 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.018 |  |
| 2025-12-21 17:05:58 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2025-12-21 17:04:26 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.020 |  |
| 2025-12-21 17:05:01 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | -0.020 |  |
| 2025-12-21 17:06:39 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2025-12-21 17:09:06 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2025-12-21 17:02:47 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2025-12-21 17:00:57 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2025-12-21 17:02:43 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.033 |  |
| 2025-12-21 17:01:09 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | -0.051 |  |
| 2025-12-21 17:05:41 | Horowpothana (Yan Oya) | 4.71 | 🟢 Normal | -0.065 |  |
| 2025-12-21 17:01:17 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.086 |  |
| 2025-12-21 17:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.148 |  |
| 2025-12-21 17:05:24 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.272 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)