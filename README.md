# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_13:17:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,468 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 13:17:28 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2025-12-08 13:16:22 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2025-12-08 13:14:31 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2025-12-08 13:13:38 | Galgamuwa (Mee Oya) | 1.42 | 🟢 Normal | -0.017 |  |
| 2025-12-08 13:13:17 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.027 |  |
| 2025-12-08 13:11:53 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:10:17 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.021 |  |
| 2025-12-08 13:09:07 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.040 |  |
| 2025-12-08 13:08:08 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2025-12-08 13:07:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2025-12-08 13:07:41 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2025-12-08 13:07:34 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.029 |  |
| 2025-12-08 13:07:17 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2025-12-08 13:06:12 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:05:26 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-08 13:05:11 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:05:10 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.019 |  |
| 2025-12-08 13:04:59 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:04:41 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.070 |  |
| 2025-12-08 13:04:04 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:03:57 | Nawalapitiya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 45.290 | 🔺 Rising |
| 2025-12-08 13:03:42 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:03:26 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:03:22 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 13:03:03 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:02:53 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | -0.085 |  |
| 2025-12-08 13:02:29 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:02:27 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:02:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-08 13:02:05 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:02:00 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:01:57 | Weraganthota (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2025-12-08 13:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 45.290 | 🔺 Rising |
| 2025-12-08 13:01:40 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 13:01:36 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:01:24 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.042 |  |
| 2025-12-08 13:01:22 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:01:21 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:01:12 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 13:01:03 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 13:03:57 | Nawalapitiya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 45.290 | 🔺 Rising |
| 2025-12-08 13:17:28 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2025-12-08 13:08:08 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2025-12-08 13:01:57 | Weraganthota (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2025-12-08 13:02:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-08 13:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 13:05:26 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-08 13:01:40 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 13:03:22 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 13:01:22 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:02:29 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:03:42 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:01:21 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:02:27 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:05:11 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:04:59 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:04:04 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:11:53 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:03:03 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:01:12 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 13:14:31 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2025-12-08 13:02:00 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:01:36 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:03:26 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:02:05 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-08 13:13:38 | Galgamuwa (Mee Oya) | 1.42 | 🟢 Normal | -0.017 |  |
| 2025-12-08 13:07:41 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2025-12-08 13:05:10 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.019 |  |
| 2025-12-08 13:10:17 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.021 |  |
| 2025-12-08 13:13:17 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.027 |  |
| 2025-12-08 13:07:34 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.029 |  |
| 2025-12-08 12:08:41 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.031 |  |
| 2025-12-08 13:09:07 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.040 |  |
| 2025-12-08 13:01:24 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.042 |  |
| 2025-12-08 13:01:03 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.043 |  |
| 2025-12-08 13:04:41 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.070 |  |
| 2025-12-08 13:02:53 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)