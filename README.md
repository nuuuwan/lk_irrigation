# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_03:30:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,400 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 03:30:45 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.027 |  |
| 2025-12-13 03:25:12 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.050 |  |
| 2025-12-13 03:16:35 | Magura (Kalu Ganga) | 2.94 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2025-12-13 03:16:33 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2025-12-13 03:16:31 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2025-12-13 03:12:39 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-13 03:12:37 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:11:57 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:07:40 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:06:25 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.069 |  |
| 2025-12-13 03:06:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-13 03:06:02 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:05:51 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:05:50 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2025-12-13 03:05:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-13 03:05:36 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:05:34 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.019 |  |
| 2025-12-13 03:05:32 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:05:17 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:04:54 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:04:43 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 03:04:37 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:04:27 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-13 03:03:55 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-13 03:03:35 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:03:27 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-13 03:02:45 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:02:41 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2025-12-13 03:02:35 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 03:02:08 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-13 03:01:56 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:01:55 | Manampitiya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.040 |  |
| 2025-12-13 03:01:50 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-13 03:01:49 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 03:01:47 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.025 |  |
| 2025-12-13 03:01:42 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:01:19 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-13 03:00:36 | Horowpothana (Yan Oya) | 6.23 | 🟡 Alert | -0.051 |  |
| 2025-12-13 03:00:17 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 03:00:36 | Horowpothana (Yan Oya) | 6.23 | 🟡 Alert | -0.051 |  |
| 2025-12-13 03:16:35 | Magura (Kalu Ganga) | 2.94 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2025-12-13 03:06:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-13 03:04:27 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-13 03:02:35 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 03:05:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-13 03:01:49 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 03:04:43 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 03:12:39 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-13 03:06:02 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:03:35 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:05:32 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:02:45 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:05:36 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:05:51 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:05:17 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:01:42 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:12:37 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:07:40 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:06:14 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:01:56 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:03:27 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-13 03:00:17 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-13 03:01:19 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-13 03:02:08 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-13 03:01:50 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-13 03:05:50 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2025-12-13 03:03:55 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-13 01:43:26 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.014 |  |
| 2025-12-13 03:02:41 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2025-12-13 03:05:34 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.019 |  |
| 2025-12-13 03:01:47 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.025 |  |
| 2025-12-13 03:30:45 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.027 |  |
| 2025-12-13 03:01:55 | Manampitiya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.040 |  |
| 2025-12-13 03:25:12 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.050 |  |
| 2025-12-13 03:06:25 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.069 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)