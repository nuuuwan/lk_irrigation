# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_16:16:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,101 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 16:16:01 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:15:20 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-01-18 16:13:29 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-18 16:10:21 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-01-18 16:09:57 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:08:33 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-18 16:07:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 16:07:01 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:49 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:38 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:16 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-18 16:06:09 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:05 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:05:41 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:05:02 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:04:44 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:04:43 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:04:32 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:04:27 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-01-18 16:04:15 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:03:54 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-18 16:03:52 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:03:44 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 16:03:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-01-18 16:03:42 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:03:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-18 16:03:28 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-01-18 16:02:51 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-01-18 16:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:20 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:20 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:05 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:01:47 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-18 16:01:38 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-18 16:01:15 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-01-18 16:01:12 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:00:38 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.042 |  |
| 2026-01-18 15:24:31 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.037 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 16:02:51 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-01-18 16:06:16 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-18 16:13:29 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-18 16:03:44 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 16:07:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 16:03:42 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:04:44 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:28 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:04:15 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:05 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:01:12 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:38 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:04:43 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:49 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:10:59 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:20 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:07:01 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:05:02 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:09:57 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:05 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:16:01 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:09 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:05:41 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:20 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:02:31 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:04:32 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:15:20 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-01-18 16:08:33 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-18 16:10:21 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-01-18 16:03:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-18 16:01:47 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-18 16:01:38 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-18 16:03:28 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-01-18 16:01:15 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-01-18 16:03:54 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-18 16:04:27 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-01-18 16:00:38 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.042 |  |
| 2026-01-18 16:03:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)