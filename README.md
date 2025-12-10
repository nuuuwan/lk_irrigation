# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_05:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,683 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 05:03:30 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:10 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:07 | Horowpothana (Yan Oya) | 4.75 | 🟢 Normal | -0.158 |  |
| 2025-12-11 05:02:21 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2025-12-11 05:02:09 | Yaka Wewa (Ma Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-11 05:01:44 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.030 |  |
| 2025-12-11 05:01:25 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 05:01:11 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:01:04 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:00:31 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:45:40 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 04:32:37 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.008 |  |
| 2025-12-11 04:26:04 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.017 |  |
| 2025-12-11 04:21:08 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:17:01 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.025 |  |
| 2025-12-11 04:16:35 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2025-12-11 04:15:09 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:12:32 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:10:59 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.032 |  |
| 2025-12-11 04:08:04 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:07:41 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.011 |  |
| 2025-12-11 04:06:36 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-11 04:06:26 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.039 |  |
| 2025-12-11 04:05:59 | Horowpothana (Yan Oya) | 4.90 | 🟢 Normal | -0.158 |  |
| 2025-12-11 04:04:52 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-11 04:04:49 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:04:36 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 04:00:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-11 04:06:36 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-11 04:04:52 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 04:45:40 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-11 05:01:25 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 04:01:31 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 05:00:31 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:01:11 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:30 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:03:10 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:06:56 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:07:09 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:15:09 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:02:05 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:04:49 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:01:04 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:21:08 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:01:18 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:08:55 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:32:37 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.008 |  |
| 2025-12-11 04:16:35 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2025-12-11 03:19:35 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-11 05:02:09 | Yaka Wewa (Ma Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-11 04:04:36 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-11 05:02:21 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2025-12-11 04:26:04 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.017 |  |
| 2025-12-11 04:17:01 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.025 |  |
| 2025-12-11 05:01:44 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.030 |  |
| 2025-12-11 04:10:59 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.032 |  |
| 2025-12-11 04:06:26 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.039 |  |
| 2025-12-11 04:03:26 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.066 |  |
| 2025-12-11 05:03:07 | Horowpothana (Yan Oya) | 4.75 | 🟢 Normal | -0.158 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)