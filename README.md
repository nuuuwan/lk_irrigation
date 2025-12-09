# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_14:20:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,362 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 14:20:27 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.017 |  |
| 2025-12-09 14:16:11 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-09 14:14:39 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:09:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-09 14:08:12 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | -0.048 |  |
| 2025-12-09 14:07:56 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:07:06 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-09 14:07:03 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:06:57 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:06:55 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -1.929 |  |
| 2025-12-09 14:06:01 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-09 14:05:59 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | -1.929 |  |
| 2025-12-09 14:05:13 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.051 |  |
| 2025-12-09 14:04:52 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.009 |  |
| 2025-12-09 14:04:43 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.122 |  |
| 2025-12-09 14:04:25 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-09 14:04:24 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2025-12-09 14:04:21 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.060 |  |
| 2025-12-09 14:03:38 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2025-12-09 14:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | -0.049 |  |
| 2025-12-09 14:03:27 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.042 |  |
| 2025-12-09 14:03:25 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 14:03:02 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.019 |  |
| 2025-12-09 14:02:44 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:02:42 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-09 14:02:19 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.050 |  |
| 2025-12-09 14:02:19 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 14:02:15 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:02:08 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 14:02:06 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:01:57 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.011 |  |
| 2025-12-09 14:01:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.075 |  |
| 2025-12-09 14:01:35 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-09 14:01:35 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 14:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:01:17 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:01:15 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 14:00:49 | Yaka Wewa (Ma Oya) | 1.72 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-09 14:00:45 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 14:06:01 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-09 14:09:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-09 14:00:49 | Yaka Wewa (Ma Oya) | 1.72 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-09 14:01:35 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 14:04:25 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-09 14:01:15 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 14:03:25 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 14:07:06 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-09 14:16:11 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-09 14:02:19 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 14:02:08 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 14:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:14:39 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:07:56 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:01:17 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:00:45 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:07:03 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:02:15 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:02:44 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:06:57 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:02:06 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:04:52 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.009 |  |
| 2025-12-09 14:02:42 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-09 14:01:35 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-09 14:01:57 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.011 |  |
| 2025-12-09 14:20:27 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.017 |  |
| 2025-12-09 14:03:02 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.019 |  |
| 2025-12-09 14:03:38 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2025-12-09 14:03:27 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.042 |  |
| 2025-12-09 14:08:12 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | -0.048 |  |
| 2025-12-09 14:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | -0.049 |  |
| 2025-12-09 14:02:19 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.050 |  |
| 2025-12-09 14:04:24 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2025-12-09 14:05:13 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.051 |  |
| 2025-12-09 14:04:21 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.060 |  |
| 2025-12-09 14:01:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.075 |  |
| 2025-12-09 14:04:43 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.122 |  |
| 2025-12-09 14:06:55 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -1.929 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)