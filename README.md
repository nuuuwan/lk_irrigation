# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_01:24:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 01:24:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.008 |  |
| 2025-12-22 01:17:39 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -36.000 |  |
| 2025-12-22 01:17:38 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -36.000 |  |
| 2025-12-22 01:17:36 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -36.000 |  |
| 2025-12-22 01:15:45 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.047 |  |
| 2025-12-22 01:09:10 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.003 |  |
| 2025-12-22 01:08:35 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:08:33 | Horowpothana (Yan Oya) | 4.35 | 🟢 Normal | 10.286 | 🔺 Rising |
| 2025-12-22 01:08:19 | Horowpothana (Yan Oya) | 4.31 | 🟢 Normal | 10.286 | 🔺 Rising |
| 2025-12-22 01:07:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 01:07:23 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.039 |  |
| 2025-12-22 01:07:15 | Horowpothana (Yan Oya) | 4.36 | 🟢 Normal | 10.286 | 🔺 Rising |
| 2025-12-22 01:05:38 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:05:36 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:04:54 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:03:41 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:03:28 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-22 01:03:06 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:03:01 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-22 01:02:54 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-22 01:02:35 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:02:32 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-22 01:02:20 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.041 |  |
| 2025-12-22 01:02:16 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.031 |  |
| 2025-12-22 01:02:15 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:02:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-22 01:01:44 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.045 |  |
| 2025-12-22 01:01:27 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:01:13 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-22 01:01:08 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 01:08:33 | Horowpothana (Yan Oya) | 4.35 | 🟢 Normal | 10.286 | 🔺 Rising |
| 2025-12-22 01:03:01 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-22 01:02:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-22 01:02:32 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-22 00:18:19 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-22 00:03:54 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 01:07:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 01:01:27 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:02:35 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 00:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:08:35 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:04:54 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:02:15 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:03:06 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:05:38 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:03:06 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 00:11:59 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-22 00:25:33 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:01:08 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:09:10 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.003 |  |
| 2025-12-22 01:24:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.008 |  |
| 2025-12-22 01:02:54 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-22 00:03:10 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-22 01:01:13 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-22 01:03:28 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-22 00:09:31 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-22 01:02:16 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.031 |  |
| 2025-12-21 22:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2025-12-22 01:07:23 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.039 |  |
| 2025-12-22 01:02:20 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.041 |  |
| 2025-12-22 01:01:44 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.045 |  |
| 2025-12-22 01:15:45 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.047 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-22 00:03:37 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.098 |  |
| 2025-12-22 00:02:19 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -8.471 |  |
| 2025-12-22 01:17:39 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)