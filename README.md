# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_14:09:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,762 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 14:09:24 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:08:21 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.027 |  |
| 2026-01-01 14:08:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-01-01 14:07:10 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:07:02 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:06:54 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.038 |  |
| 2026-01-01 14:06:12 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-01-01 14:04:37 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 14:04:36 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.114 |  |
| 2026-01-01 14:04:06 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:03:32 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:03:28 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:03:18 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-01 14:03:07 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:02:49 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:02:42 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-01 14:02:41 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:02:27 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 14:02:25 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.031 |  |
| 2026-01-01 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:39 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:31 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-01 14:01:26 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:25 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-01 14:01:21 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:13 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.013 |  |
| 2026-01-01 14:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:07 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:02 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-01-01 14:00:55 | Siyambalanduwa (Heda Oya) | 1.40 | 🟢 Normal | -0.057 |  |
| 2026-01-01 14:00:53 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 14:00:52 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.081 |  |
| 2026-01-01 14:00:13 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:59:55 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:14:54 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 14:01:25 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-01 13:11:59 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-01 14:02:27 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 14:00:53 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 14:04:37 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 13:07:35 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 14:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:01:51 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:09:24 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:05:17 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:07:10 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:07 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:02:41 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:21 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:39 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:02:53 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:07:02 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:03:28 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:02:49 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:59:55 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:26 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:03:32 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:03:07 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:04:06 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-01-01 14:01:31 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-01 14:02:42 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-01 14:00:13 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-01 14:03:18 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-01 14:01:02 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-01-01 14:01:13 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.013 |  |
| 2026-01-01 14:06:12 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-01-01 14:08:21 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.027 |  |
| 2026-01-01 14:02:25 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.031 |  |
| 2026-01-01 14:06:54 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.038 |  |
| 2026-01-01 14:00:55 | Siyambalanduwa (Heda Oya) | 1.40 | 🟢 Normal | -0.057 |  |
| 2026-01-01 14:08:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-01-01 14:00:52 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.081 |  |
| 2026-01-01 14:04:36 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)