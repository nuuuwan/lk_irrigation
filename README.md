# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_10:38:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,843 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 10:38:36 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:16:05 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:16:01 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:13:39 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.041 |  |
| 2026-04-13 10:13:07 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:12:20 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:11:30 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-04-13 10:10:31 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.036 |  |
| 2026-04-13 10:10:19 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-13 10:09:39 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.053 |  |
| 2026-04-13 10:08:09 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.122 |  |
| 2026-04-13 10:07:18 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:06:45 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.057 |  |
| 2026-04-13 10:06:40 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.184 |  |
| 2026-04-13 10:05:50 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-04-13 10:05:27 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-13 10:05:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 10:05:25 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-04-13 10:04:54 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.022 |  |
| 2026-04-13 10:04:50 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:04:39 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:04:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-13 10:04:04 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-13 10:03:57 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:03:44 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.051 |  |
| 2026-04-13 10:03:40 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-13 10:03:32 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-13 10:02:53 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-13 10:02:50 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.012 |  |
| 2026-04-13 10:02:50 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.123 |  |
| 2026-04-13 10:02:47 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:02:22 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.011 |  |
| 2026-04-13 10:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 10:01:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:01:18 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:01:16 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-04-13 10:01:07 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.031 |  |
| 2026-04-13 10:00:23 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 10:05:27 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-13 10:03:32 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-13 10:03:40 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-13 10:02:53 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-13 10:04:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-13 10:05:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 10:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 10:00:23 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:38:36 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:16:05 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:12:20 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:03:57 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:04:39 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:02:47 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:16:01 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:01:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:07:18 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:13:07 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:04:50 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:01:18 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-13 10:11:30 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-04-13 10:10:19 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-13 10:02:22 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.011 |  |
| 2026-04-13 10:02:50 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.012 |  |
| 2026-04-13 10:05:25 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-04-13 10:04:04 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-13 10:05:50 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-04-13 10:01:16 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-04-13 10:04:54 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.022 |  |
| 2026-04-13 10:01:07 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.031 |  |
| 2026-04-13 10:10:31 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.036 |  |
| 2026-04-13 10:13:39 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.041 |  |
| 2026-04-13 10:03:44 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.051 |  |
| 2026-04-13 10:09:39 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.053 |  |
| 2026-04-13 10:06:45 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.057 |  |
| 2026-04-13 10:08:09 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.122 |  |
| 2026-04-13 10:02:50 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.123 |  |
| 2026-04-13 10:06:40 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.184 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)