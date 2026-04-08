# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_14:28:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,567 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 14:28:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:15:16 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-08 14:11:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.018 |  |
| 2026-04-08 14:09:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-04-08 14:09:02 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:08:16 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:07:50 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:07:27 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:07:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-08 14:07:04 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:06:28 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:06:22 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:05:55 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:05:45 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:05:39 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:04:59 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:04:17 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:03:51 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-08 14:03:49 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:03:40 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:03:30 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:03:18 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:03:16 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:03:16 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.068 |  |
| 2026-04-08 14:03:10 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:03:04 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-04-08 14:02:22 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:02:21 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:02:16 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.049 |  |
| 2026-04-08 14:01:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 14:01:44 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-08 14:01:34 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:01:29 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 14:00:52 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:00:29 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.189 |  |
| 2026-04-08 14:00:23 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:00:12 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:41:47 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.325 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 14:09:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-04-08 14:07:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-08 14:15:16 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-08 14:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 14:01:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 14:01:29 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:01:34 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:00:12 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:28:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:06:22 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:03:16 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 13:11:53 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:08:16 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:05:39 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:02:21 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:02:22 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:05:55 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:03:40 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:07:27 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:06:28 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:05:45 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:03:18 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:07:50 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:09:02 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:04:59 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:04:17 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:03:10 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:03:30 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:00:52 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:00:23 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:03:49 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-08 14:03:04 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-04-08 14:11:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.018 |  |
| 2026-04-08 14:01:44 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-08 14:03:51 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-08 14:02:16 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.049 |  |
| 2026-04-08 14:03:16 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.068 |  |
| 2026-04-08 14:00:29 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.189 |  |
| 2026-04-08 13:05:58 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)