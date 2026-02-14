# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_15:08:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 15:08:50 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:08:33 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-14 15:08:20 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:07:40 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 15:06:39 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-14 15:06:25 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:06:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:05:20 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:05:00 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-14 15:04:58 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-02-14 15:04:48 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:43 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.011 |  |
| 2026-02-14 15:04:21 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:11 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:10 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-14 15:04:07 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:04 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.047 |  |
| 2026-02-14 15:03:49 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:03:39 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.052 |  |
| 2026-02-14 15:03:27 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-02-14 15:03:19 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-02-14 15:03:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:03:01 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-14 15:02:57 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-14 15:02:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 15:02:43 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:02:42 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:02:34 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:02:28 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-02-14 15:02:27 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-02-14 15:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 15:01:55 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:01:54 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 15:01:51 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:01:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-14 15:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:01:35 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:01:34 | Padiyathalawa (Maduru Oya) | 4.15 | 🟡 Alert | 0.703 | 🔺 Rising |
| 2026-02-14 15:00:26 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:00:05 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:49:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 15:01:34 | Padiyathalawa (Maduru Oya) | 4.15 | 🟡 Alert | 0.703 | 🔺 Rising |
| 2026-02-14 15:02:28 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-02-14 15:02:57 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-14 15:08:33 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-14 15:07:40 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 15:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 15:01:54 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 15:02:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 15:02:42 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:00:05 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:03:49 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:01:55 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:21 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:05:20 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:02:43 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:11 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:48 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:03:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:01:51 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:06:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:07 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:08:50 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:00:26 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:08:20 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:02:34 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:05:00 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-14 15:03:01 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-14 15:04:10 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-14 15:06:39 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-14 15:04:43 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.011 |  |
| 2026-02-14 15:02:27 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-02-14 15:03:27 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-02-14 15:01:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-14 15:03:19 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-02-14 15:04:58 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-02-14 15:04:04 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.047 |  |
| 2026-02-14 15:03:39 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)