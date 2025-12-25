# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_05:22:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,203 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 05:22:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.008 |  |
| 2025-12-25 05:20:13 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-25 05:17:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:17:17 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:17:16 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:17:14 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:17:00 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.034 |  |
| 2025-12-25 05:14:23 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-25 05:13:40 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.005 |  |
| 2025-12-25 05:08:37 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | 26.069 | 🔺 Rising |
| 2025-12-25 05:08:32 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:08:08 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 26.069 | 🔺 Rising |
| 2025-12-25 05:08:00 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:06:46 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.018 |  |
| 2025-12-25 05:06:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 05:06:13 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 05:05:58 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:05:30 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:05:13 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2025-12-25 05:05:12 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2025-12-25 05:04:57 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2025-12-25 05:04:19 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.022 |  |
| 2025-12-25 05:03:58 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:50 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:44 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 05:03:34 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:17 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.033 |  |
| 2025-12-25 05:02:22 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:02:13 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:02:12 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:02:07 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:01:55 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 05:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.033 |  |
| 2025-12-25 05:01:23 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.032 |  |
| 2025-12-25 05:01:19 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2025-12-25 05:01:17 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:00:36 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:59:28 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:45:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 19.286 | 🔺 Rising |
| 2025-12-25 04:45:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 19.286 | 🔺 Rising |
| 2025-12-25 04:45:29 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-25 04:45:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 19.286 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 05:05:13 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2025-12-25 05:08:37 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | 26.069 | 🔺 Rising |
| 2025-12-25 04:45:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 19.286 | 🔺 Rising |
| 2025-12-25 05:14:23 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-25 03:02:44 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 05:20:13 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-25 05:06:13 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 05:03:44 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 05:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 05:06:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 05:13:40 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.005 |  |
| 2025-12-25 05:02:12 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:58 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:50 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:01:55 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:08:00 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:05:58 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:00:36 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:05:30 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:17:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:34 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:08:32 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:02:13 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:22:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.008 |  |
| 2025-12-25 05:02:07 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:01:17 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:02:22 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:06:46 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.018 |  |
| 2025-12-25 05:04:57 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 05:04:19 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.022 |  |
| 2025-12-25 05:01:23 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.032 |  |
| 2025-12-25 05:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.033 |  |
| 2025-12-25 05:03:17 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.033 |  |
| 2025-12-25 05:17:00 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.034 |  |
| 2025-12-25 04:18:18 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.041 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-25 05:01:19 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)