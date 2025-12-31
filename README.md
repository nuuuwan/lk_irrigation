# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_23:15:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 23:15:43 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:10:31 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:07:24 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:55 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:54 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2025-12-31 23:05:43 | Katharagama (Menik Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:33 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:14 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:09 | Katharagama (Menik Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:03 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-31 23:04:40 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-31 23:04:24 | Thanamalwila (Kirindi Oya) | 2.04 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 23:04:09 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:04:04 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 23:03:53 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-31 23:03:34 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:03:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-31 23:03:10 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-31 23:03:02 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:02:55 | Siyambalanduwa (Heda Oya) | 4.00 | 🟢 Normal | 0.395 | 🔺 Rising |
| 2025-12-31 23:02:45 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 23:02:43 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:02:32 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:02:18 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 23:02:14 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-31 23:02:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:01:31 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:01:23 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-31 23:01:15 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 23:00:35 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:00:29 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | -0.417 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 23:02:55 | Siyambalanduwa (Heda Oya) | 4.00 | 🟢 Normal | 0.395 | 🔺 Rising |
| 2025-12-31 23:05:03 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-31 23:04:40 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-31 23:02:14 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-31 22:35:10 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-31 23:03:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-31 23:04:24 | Thanamalwila (Kirindi Oya) | 2.04 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 23:03:10 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-31 22:07:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-31 23:03:53 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-31 22:29:56 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 23:02:18 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 23:04:04 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 23:01:15 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 23:02:45 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:10:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 23:02:43 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:04:09 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:15:43 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:03:02 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:01:23 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:33 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:14 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:02:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:07:24 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:03:34 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:43 | Katharagama (Menik Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:01:31 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:02:32 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:10:31 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:55 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:00:35 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-31 22:09:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.018 |  |
| 2025-12-31 23:05:54 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2025-12-31 23:00:29 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | -0.417 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)