# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_20:09:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,266 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 20:09:52 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 20:09:24 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.038 |  |
| 2026-02-22 20:08:41 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.038 |  |
| 2026-02-22 20:08:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.124 |  |
| 2026-02-22 20:08:15 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.145 |  |
| 2026-02-22 20:08:04 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-22 20:07:39 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.105 |  |
| 2026-02-22 20:07:10 | Manampitiya (Mahaweli Ganga) | 3.36 | 🟡 Alert | -0.163 |  |
| 2026-02-22 20:07:00 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.051 |  |
| 2026-02-22 20:06:22 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.038 |  |
| 2026-02-22 20:06:11 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.044 |  |
| 2026-02-22 20:05:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:05:01 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:04:55 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.041 |  |
| 2026-02-22 20:04:44 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:04:10 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-22 20:04:04 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-02-22 20:04:01 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:03:17 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 20:03:16 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-02-22 20:03:08 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-22 20:02:55 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.105 |  |
| 2026-02-22 20:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.99 | 🟢 Normal | -0.020 |  |
| 2026-02-22 20:02:37 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:02:35 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.005 |  |
| 2026-02-22 20:02:32 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.102 |  |
| 2026-02-22 20:02:26 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.060 |  |
| 2026-02-22 20:01:54 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:01:47 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-02-22 20:01:36 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:01:24 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.022 |  |
| 2026-02-22 20:01:15 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-22 19:18:49 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.088 |  |
| 2026-02-22 19:15:26 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 20:07:10 | Manampitiya (Mahaweli Ganga) | 3.36 | 🟡 Alert | -0.163 |  |
| 2026-02-22 19:01:30 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-02-22 20:08:04 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 20:09:52 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 20:03:17 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 20:01:36 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:01:54 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:05:01 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:04:01 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:04:44 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:05:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:01:34 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:02:35 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.005 |  |
| 2026-02-22 20:04:10 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-22 20:01:15 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-22 20:01:47 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-02-22 20:03:08 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-22 19:07:39 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-02-22 20:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.99 | 🟢 Normal | -0.020 |  |
| 2026-02-22 20:01:24 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.022 |  |
| 2026-02-22 18:57:12 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.022 |  |
| 2026-02-22 20:04:04 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-02-22 20:09:24 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.038 |  |
| 2026-02-22 20:08:41 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.038 |  |
| 2026-02-22 20:06:22 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.038 |  |
| 2026-02-22 20:03:16 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-02-22 20:04:55 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.041 |  |
| 2026-02-22 20:06:11 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.044 |  |
| 2026-02-22 20:07:00 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.051 |  |
| 2026-02-22 20:02:26 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.060 |  |
| 2026-02-22 19:18:49 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.088 |  |
| 2026-02-22 20:02:32 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.102 |  |
| 2026-02-22 20:07:39 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.105 |  |
| 2026-02-22 20:02:55 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.105 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-22 20:08:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.124 |  |
| 2026-02-22 20:08:15 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)