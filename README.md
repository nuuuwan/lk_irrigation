# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_15:15:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 15:15:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-21 15:13:14 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:08:26 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-21 15:07:54 | Padiyathalawa (Maduru Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-02-21 15:07:09 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:07:06 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-02-21 15:06:43 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-21 15:06:29 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:05:02 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:04:34 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:04:26 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:04:21 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:03:56 | Deraniyagala (Kelani Ganga) | 8.16 | 🔴 Major Flood | 7.776 | 🔺 Rising |
| 2026-02-21 15:03:53 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:03:41 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.041 |  |
| 2026-02-21 15:03:33 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:03:31 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-02-21 15:03:23 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 15:03:10 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-02-21 15:03:09 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-02-21 15:03:06 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:47 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:46 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:36 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:31 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:31 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.039 |  |
| 2026-02-21 15:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.074 |  |
| 2026-02-21 15:02:28 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:20 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 15:02:13 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:02:01 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:01:58 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:01:37 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:01:36 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:01:35 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.041 |  |
| 2026-02-21 15:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:01:15 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:01:00 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.070 |  |
| 2026-02-21 15:00:47 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 15:03:56 | Deraniyagala (Kelani Ganga) | 8.16 | 🔴 Major Flood | 7.776 | 🔺 Rising |
| 2026-02-21 15:03:10 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-02-21 15:08:26 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-21 15:15:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-21 15:06:43 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-21 15:02:20 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 15:03:23 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 15:01:37 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:04:21 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:01:36 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:36 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:01:15 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:03:53 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:04:26 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:03:06 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:13:14 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:07:09 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:04:34 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:47 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:06:29 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:28 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:31 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:03:33 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:02:46 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:07:06 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-02-21 15:07:54 | Padiyathalawa (Maduru Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-02-21 15:05:02 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:02:13 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:01:58 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:02:01 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.010 |  |
| 2026-02-21 15:03:31 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-02-21 15:00:47 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.030 |  |
| 2026-02-21 15:02:31 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.039 |  |
| 2026-02-21 15:03:09 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-02-21 15:03:41 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.041 |  |
| 2026-02-21 15:01:35 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.041 |  |
| 2026-02-21 15:01:00 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.070 |  |
| 2026-02-21 15:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)