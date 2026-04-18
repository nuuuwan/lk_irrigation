# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_09:11:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 09:11:15 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.027 |  |
| 2026-04-18 09:09:46 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:09:44 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-18 09:08:14 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-18 09:08:12 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:07:36 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-18 09:06:50 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:06:15 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.046 |  |
| 2026-04-18 09:05:48 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:05:47 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:05:16 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:05:00 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.040 |  |
| 2026-04-18 09:04:58 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:04:45 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:04:18 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.345 |  |
| 2026-04-18 09:04:13 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 09:04:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:03:12 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:02:59 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.010 |  |
| 2026-04-18 09:02:50 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-18 09:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.072 |  |
| 2026-04-18 09:02:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:02:23 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.136 |  |
| 2026-04-18 09:02:18 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-18 09:02:03 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.142 |  |
| 2026-04-18 09:01:20 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.044 |  |
| 2026-04-18 09:01:16 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:01:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:01:13 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:01:01 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-18 09:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-18 09:00:56 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-18 09:00:47 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 09:00:19 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:00:18 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-04-18 09:00:16 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:21:46 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 09:02:18 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-18 09:07:36 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-18 09:09:44 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-18 09:02:50 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-18 09:00:47 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 09:04:13 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 08:05:52 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 08:07:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-18 09:01:16 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:00:16 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:01:13 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:01:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:05:47 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:09:46 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:00:19 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:05:48 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:04:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:03:12 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:02:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:08:42 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:05:16 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:04:45 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:04:58 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:06:50 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:08:12 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:02:59 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.010 |  |
| 2026-04-18 09:01:01 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-18 09:00:18 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-04-18 09:08:14 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-18 09:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-18 09:00:56 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-18 09:11:15 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.027 |  |
| 2026-04-18 09:05:00 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.040 |  |
| 2026-04-18 09:01:20 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.044 |  |
| 2026-04-18 09:06:15 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.046 |  |
| 2026-04-18 09:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.072 |  |
| 2026-04-18 09:02:23 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.136 |  |
| 2026-04-18 09:02:03 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.142 |  |
| 2026-04-18 09:04:18 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.345 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)