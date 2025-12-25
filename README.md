# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_06:10:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,244 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **50** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 06:10:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-25 06:08:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:08:34 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-25 06:07:57 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.013 |  |
| 2025-12-25 06:06:37 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-25 06:06:09 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.111 |  |
| 2025-12-25 06:06:05 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.028 |  |
| 2025-12-25 06:06:04 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-25 06:06:01 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:05:48 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2025-12-25 06:05:46 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:05:35 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-25 06:05:22 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.012 |  |
| 2025-12-25 06:05:19 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 06:05:14 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:05:05 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:05:05 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2025-12-25 06:05:01 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:04:55 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-25 06:04:16 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 06:03:46 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-25 06:03:23 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2025-12-25 06:03:12 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.052 |  |
| 2025-12-25 06:03:10 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-25 06:02:39 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:02:37 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 06:02:05 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:01:49 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-25 06:01:41 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.030 |  |
| 2025-12-25 06:01:34 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.030 |  |
| 2025-12-25 06:01:27 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.175 |  |
| 2025-12-25 06:01:25 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-25 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2025-12-25 06:00:54 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2025-12-25 06:00:36 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.196 |  |
| 2025-12-25 06:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:59:43 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:51:31 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2025-12-25 05:51:05 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2025-12-25 05:48:21 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.196 |  |
| 2025-12-25 05:47:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-25 05:22:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-25 05:20:13 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.175 |  |
| 2025-12-25 05:17:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-25 05:17:17 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-25 05:17:16 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-25 05:17:14 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-25 05:17:00 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.052 |  |
| 2025-12-25 05:14:23 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-25 05:13:40 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.034 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 06:03:23 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2025-12-25 06:05:48 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2025-12-25 06:03:10 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-25 06:01:49 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-25 06:04:55 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-25 06:08:34 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-25 06:01:25 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-25 06:10:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-25 06:06:37 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-25 06:06:04 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-25 06:05:19 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 06:04:16 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 06:05:35 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-25 06:02:37 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 06:06:01 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:59:43 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:08:00 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:05:14 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:02:39 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:05:46 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:08:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:05:05 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:02:05 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-25 06:03:46 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-25 06:05:22 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.012 |  |
| 2025-12-25 06:07:57 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.013 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 06:00:54 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2025-12-25 06:06:05 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.028 |  |
| 2025-12-25 06:05:05 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2025-12-25 06:01:41 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.030 |  |
| 2025-12-25 06:01:34 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.030 |  |
| 2025-12-25 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2025-12-25 06:03:12 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.052 |  |
| 2025-12-25 06:06:09 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.111 |  |
| 2025-12-25 06:01:27 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.175 |  |
| 2025-12-25 06:00:36 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)