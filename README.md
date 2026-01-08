# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_05:16:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,593 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 05:16:20 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 05:14:50 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 05:14:19 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-01-09 05:13:23 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -36.000 |  |
| 2026-01-09 05:13:21 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -36.000 |  |
| 2026-01-09 05:12:33 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-01-09 05:11:14 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-09 05:09:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.057 |  |
| 2026-01-09 05:09:21 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-09 05:09:15 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.081 |  |
| 2026-01-09 05:09:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-09 05:07:55 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:07:25 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:07:11 | Moragaswewa (Deduru Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:06:58 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:06:43 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:06:32 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-09 05:06:28 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:06:10 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-09 05:05:58 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:05:37 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.043 |  |
| 2026-01-09 05:04:54 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:04:44 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.013 |  |
| 2026-01-09 05:04:13 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 05:03:38 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:03:18 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:03:11 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:45 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-09 05:02:37 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:36 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:29 | Moragaswewa (Deduru Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:24 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:01 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.177 |  |
| 2026-01-09 05:01:41 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 05:00:43 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 04:55:51 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-01-09 04:39:19 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 04:37:49 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 05:12:33 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-01-09 05:09:21 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-09 05:06:32 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-09 05:09:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-09 05:04:13 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 05:16:20 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 05:11:14 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 05:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 05:14:50 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 05:02:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:03:18 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:07:11 | Moragaswewa (Deduru Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 04:01:55 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:06:28 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:24 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:37 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:03:11 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:01:41 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:07:55 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:02:36 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:03:38 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:04:54 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:06:43 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:00:43 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 04:01:34 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 05:14:19 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-01-09 05:02:45 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 05:06:10 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-09 05:04:44 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.013 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-09 05:05:37 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.043 |  |
| 2026-01-09 05:09:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.057 |  |
| 2026-01-09 05:09:15 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.081 |  |
| 2026-01-09 05:02:01 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.177 |  |
| 2026-01-09 05:13:23 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -36.000 |  |
| 2026-01-09 03:06:30 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)