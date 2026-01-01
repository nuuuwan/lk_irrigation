# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_23:15:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 23:15:22 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:13:35 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:12:46 | Katharagama (Menik Ganga) | 1.26 | 🟢 Normal | -0.062 |  |
| 2026-01-01 23:10:34 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-01 23:10:31 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:07:55 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-01 23:07:27 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:07:04 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-01-01 23:07:02 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:06:40 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 23:05:50 | Horowpothana (Yan Oya) | 3.74 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-01 23:05:29 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-01 23:05:29 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:05:16 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-01 23:05:01 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-01 23:04:31 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:04:14 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-01 23:03:45 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:03:24 | Padiyathalawa (Maduru Oya) | 4.35 | 🟡 Alert | 0.764 | 🔺 Rising |
| 2026-01-01 23:03:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-01 23:02:50 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 23:02:48 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:02:48 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:02:28 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 23:02:24 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-01-01 23:02:12 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.042 |  |
| 2026-01-01 23:02:11 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-01 23:01:58 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-01 23:01:42 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-01-01 23:01:38 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | 45.570 | 🔺 Rising |
| 2026-01-01 23:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 23:00:33 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-01 23:00:25 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:00:19 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 45.570 | 🔺 Rising |
| 2026-01-01 22:47:44 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:43:06 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:33:39 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.042 |  |
| 2026-01-01 22:30:57 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 23:03:24 | Padiyathalawa (Maduru Oya) | 4.35 | 🟡 Alert | 0.764 | 🔺 Rising |
| 2026-01-01 23:01:38 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | 45.570 | 🔺 Rising |
| 2026-01-01 23:02:24 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-01-01 23:07:04 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-01-01 23:05:16 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-01 23:07:55 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-01 23:00:33 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-01 23:04:14 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-01 23:03:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-01 23:01:58 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-01 23:05:50 | Horowpothana (Yan Oya) | 3.74 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-01 23:02:50 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 23:10:34 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-01 23:06:40 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 23:02:28 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 23:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 23:02:48 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:07:27 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:03:45 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:02:48 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:00:25 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:10:31 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:13:35 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:04:31 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:07:02 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:05:29 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:15:22 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:01:42 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:04:20 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-01 23:05:29 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-01 23:02:11 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-01 23:05:01 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-01 20:14:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-01 23:02:12 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.042 |  |
| 2026-01-01 23:12:46 | Katharagama (Menik Ganga) | 1.26 | 🟢 Normal | -0.062 |  |
| 2026-01-01 22:10:15 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)