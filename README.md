# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_15:03:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 15:03:24 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:03:14 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:03:13 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:03:12 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 15:03:04 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:02:44 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.085 |  |
| 2025-12-13 15:02:42 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.079 |  |
| 2025-12-13 15:02:41 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:02:32 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.015 |  |
| 2025-12-13 15:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:02:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-13 15:01:50 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:01:42 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:30 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:01:17 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:14 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2025-12-13 15:01:14 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.061 |  |
| 2025-12-13 15:01:09 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:09 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:59 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:44 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:42 | Horowpothana (Yan Oya) | 5.71 | 🟢 Normal | -0.051 |  |
| 2025-12-13 14:22:24 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.015 |  |
| 2025-12-13 14:13:23 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.085 |  |
| 2025-12-13 14:11:37 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.017 |  |
| 2025-12-13 14:09:59 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2025-12-13 14:09:43 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:09:35 | Weraganthota (Mahaweli Ganga) | -1.08 | 🟢 Normal | -0.079 |  |
| 2025-12-13 14:08:29 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:08:23 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.024 |  |
| 2025-12-13 14:08:01 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:07:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.026 |  |
| 2025-12-13 14:05:53 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 14:05:28 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 14:02:59 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 15:02:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-13 15:03:12 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 15:01:42 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:44 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:09 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:17 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:03:35 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:03:13 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:09 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:01:30 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:08:29 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:00:59 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 15:03:13 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:03:04 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:02:41 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:09:43 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:02:12 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:03:14 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.010 |  |
| 2025-12-13 15:01:50 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2025-12-13 15:03:24 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-13 14:01:49 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2025-12-13 15:02:32 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.015 |  |
| 2025-12-13 14:11:37 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.017 |  |
| 2025-12-13 14:08:23 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.024 |  |
| 2025-12-13 14:01:30 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.025 |  |
| 2025-12-13 14:07:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.026 |  |
| 2025-12-13 14:03:25 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2025-12-13 14:02:59 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2025-12-13 15:01:14 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2025-12-13 14:01:09 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.032 |  |
| 2025-12-13 15:00:42 | Horowpothana (Yan Oya) | 5.71 | 🟢 Normal | -0.051 |  |
| 2025-12-13 15:01:14 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.061 |  |
| 2025-12-13 15:02:42 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.079 |  |
| 2025-12-13 15:02:44 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.085 |  |
| 2025-12-13 14:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.091 |  |
| 2025-12-13 14:02:53 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)