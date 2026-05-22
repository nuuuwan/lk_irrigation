# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_04:31:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,309 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 04:31:32 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-23 04:17:40 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:15:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:09:55 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-23 04:07:26 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | 0.000 |  |
| 2026-05-23 04:06:19 | Hanwella (Kelani Ganga) | 7.48 | 🟡 Alert | -0.104 |  |
| 2026-05-23 04:06:11 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:05:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:05:49 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:05:38 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:04:40 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-23 04:04:36 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-05-23 04:04:19 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 04:03:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.061 |  |
| 2026-05-23 04:03:07 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:02:43 | Rathnapura (Kalu Ganga) | 6.60 | 🟡 Alert | -0.074 |  |
| 2026-05-23 04:02:24 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-23 04:02:07 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:01:55 | Ellagawa (Kalu Ganga) | 9.90 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-23 04:01:46 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 04:01:38 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.030 |  |
| 2026-05-23 04:01:33 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:01:32 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:01:22 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.031 |  |
| 2026-05-23 04:01:10 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:00:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:00:50 | Magura (Kalu Ganga) | 4.11 | 🟡 Alert | -0.053 |  |
| 2026-05-23 04:00:48 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.036 |  |
| 2026-05-23 04:00:28 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 04:01:46 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 04:07:26 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | 0.000 |  |
| 2026-05-23 03:15:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-05-23 04:00:50 | Magura (Kalu Ganga) | 4.11 | 🟡 Alert | -0.053 |  |
| 2026-05-23 04:02:43 | Rathnapura (Kalu Ganga) | 6.60 | 🟡 Alert | -0.074 |  |
| 2026-05-23 04:06:19 | Hanwella (Kelani Ganga) | 7.48 | 🟡 Alert | -0.104 |  |
| 2026-05-23 03:09:12 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.585 | 🔺 Rising |
| 2026-05-23 04:04:36 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-05-23 03:03:00 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-23 04:01:55 | Ellagawa (Kalu Ganga) | 9.90 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-23 04:04:40 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-23 03:07:46 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-23 04:31:32 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-23 04:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 04:05:38 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:01:33 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 01:03:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:02:07 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:06:11 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:01:10 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:04:19 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:03:07 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:00:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:01:38 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:15:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:05:49 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:17:40 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:01:32 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:09:55 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-23 03:00:54 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.017 |  |
| 2026-05-23 04:02:24 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-23 04:00:28 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.022 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-23 04:01:38 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.030 |  |
| 2026-05-23 04:01:22 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.031 |  |
| 2026-05-23 04:00:48 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.036 |  |
| 2026-05-23 04:03:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)