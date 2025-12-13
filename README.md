# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_20:24:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,054 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 20:24:50 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:12:29 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.028 |  |
| 2025-12-13 20:10:43 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:10:25 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.039 |  |
| 2025-12-13 20:09:17 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:08:17 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-13 20:07:59 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:07:06 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:07:02 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:05:20 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:04:52 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:04:46 | Ellagawa (Kalu Ganga) | 5.37 | 🟢 Normal | -0.028 |  |
| 2025-12-13 20:04:45 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.080 |  |
| 2025-12-13 20:04:43 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-13 20:04:43 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:04:38 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-13 20:04:34 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 20:04:14 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:04:10 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-13 20:04:01 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.048 |  |
| 2025-12-13 20:03:59 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.039 |  |
| 2025-12-13 20:03:42 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -0.039 |  |
| 2025-12-13 20:03:16 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2025-12-13 20:02:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-13 20:02:45 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.131 |  |
| 2025-12-13 20:02:38 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-13 20:02:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:02:24 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-13 20:02:15 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:02:06 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:02:01 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 20:01:48 | Horowpothana (Yan Oya) | 5.49 | 🟢 Normal | -0.039 |  |
| 2025-12-13 20:01:46 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-13 20:01:37 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:01:35 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:01:21 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:55:32 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 20:08:17 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-13 20:04:43 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-13 20:02:24 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 20:04:10 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-13 20:02:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-13 20:02:38 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-13 20:04:34 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 20:01:21 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:24:50 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:04:52 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:01:35 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:04:14 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:05:20 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:02:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:10:43 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:07:02 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:02:15 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:07:59 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:04:43 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:09:17 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:01:37 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-13 20:07:06 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:05:55 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2025-12-13 20:04:38 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-13 20:03:16 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2025-12-13 20:02:01 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 20:01:46 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-13 20:12:29 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.028 |  |
| 2025-12-13 20:04:46 | Ellagawa (Kalu Ganga) | 5.37 | 🟢 Normal | -0.028 |  |
| 2025-12-13 20:10:25 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.039 |  |
| 2025-12-13 20:01:48 | Horowpothana (Yan Oya) | 5.49 | 🟢 Normal | -0.039 |  |
| 2025-12-13 20:03:59 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.039 |  |
| 2025-12-13 20:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -0.039 |  |
| 2025-12-13 20:04:01 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.048 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-13 20:04:45 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.080 |  |
| 2025-12-13 20:02:45 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)