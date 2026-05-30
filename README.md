# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_00:16:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 00:16:08 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.025 |  |
| 2026-05-31 00:13:59 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.017 |  |
| 2026-05-31 00:13:09 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.143 |  |
| 2026-05-31 00:10:29 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:09:18 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:08:13 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-05-31 00:07:57 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-05-31 00:07:01 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:06:24 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-31 00:06:12 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.030 |  |
| 2026-05-31 00:06:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-05-31 00:06:01 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:05:51 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-31 00:05:43 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:05:42 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-31 00:05:17 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.029 |  |
| 2026-05-31 00:04:57 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 00:04:37 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-05-31 00:04:32 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-31 00:03:54 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-31 00:03:15 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-31 00:02:56 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:02:54 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-05-31 00:02:47 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:02:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:02:28 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.072 |  |
| 2026-05-31 00:01:42 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-31 00:01:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:01:17 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:00:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-30 23:55:55 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:28:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.072 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 00:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.072 |  |
| 2026-05-31 00:00:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-31 00:04:32 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-31 00:05:51 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-31 00:06:24 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-31 00:04:57 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 00:05:42 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-31 00:06:01 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:07:01 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:01:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:01:17 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:02:56 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:02:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:05:43 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:09:18 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:02:47 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:01:42 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:10:29 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-31 00:02:28 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:08:41 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-05-31 00:08:13 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-05-31 00:03:15 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-31 00:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-31 00:02:54 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-05-31 00:06:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-05-31 00:13:59 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.017 |  |
| 2026-05-31 00:03:54 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-31 00:07:57 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-05-31 00:16:08 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.025 |  |
| 2026-05-31 00:05:17 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.029 |  |
| 2026-05-31 00:06:12 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.030 |  |
| 2026-05-30 22:03:51 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-05-31 00:04:37 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-05-31 00:13:09 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.143 |  |
| 2026-05-30 18:02:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -30.857 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)