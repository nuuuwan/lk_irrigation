# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_18:14:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,407 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 18:14:39 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.009 |  |
| 2026-01-06 18:10:01 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-01-06 18:09:10 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:08:12 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-06 18:07:55 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 18:06:46 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.014 |  |
| 2026-01-06 18:05:41 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-06 18:05:02 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:04:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-01-06 18:04:10 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | -0.034 |  |
| 2026-01-06 18:03:56 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | -0.107 |  |
| 2026-01-06 18:03:55 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:29 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.024 |  |
| 2026-01-06 18:03:21 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:02:56 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 18:02:47 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-06 18:02:46 | Siyambalanduwa (Heda Oya) | 4.14 | 🟢 Normal | -0.598 |  |
| 2026-01-06 18:02:44 | Thaldena (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-01-06 18:02:33 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-06 18:02:20 | Manampitiya (Mahaweli Ganga) | 3.83 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-01-06 18:02:20 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.031 |  |
| 2026-01-06 18:02:18 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:02:15 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 18:02:15 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-06 18:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.070 |  |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:01:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:01:37 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 18:01:31 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.010 |  |
| 2026-01-06 18:01:26 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-06 18:01:25 | Nakkala (Kumbukkan Oya) | 1.98 | 🟢 Normal | -0.134 |  |
| 2026-01-06 18:01:14 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-06 18:01:08 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 18:00:24 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-06 17:24:25 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.014 |  |
| 2026-01-06 17:22:46 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:19:27 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.148 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 18:02:20 | Manampitiya (Mahaweli Ganga) | 3.83 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-01-06 18:08:12 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-06 18:00:24 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-06 18:02:15 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-06 18:05:41 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-06 18:02:47 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-06 18:01:14 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-06 18:01:37 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 18:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 18:02:15 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 18:01:08 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:07:55 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 18:03:13 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:02:18 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:55 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:05:02 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:02:56 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:01:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:21 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:09:10 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:14:39 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.009 |  |
| 2026-01-06 18:02:33 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-06 17:16:30 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-06 18:01:31 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.010 |  |
| 2026-01-06 18:01:26 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-06 18:06:46 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.014 |  |
| 2026-01-06 18:10:01 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-01-06 18:03:29 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.024 |  |
| 2026-01-06 18:02:44 | Thaldena (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-01-06 18:02:20 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.031 |  |
| 2026-01-06 18:04:10 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | -0.034 |  |
| 2026-01-06 18:04:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-01-06 18:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.070 |  |
| 2026-01-06 18:03:56 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | -0.107 |  |
| 2026-01-06 18:01:25 | Nakkala (Kumbukkan Oya) | 1.98 | 🟢 Normal | -0.134 |  |
| 2026-01-06 18:02:46 | Siyambalanduwa (Heda Oya) | 4.14 | 🟢 Normal | -0.598 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)