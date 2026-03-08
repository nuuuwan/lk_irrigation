# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_13:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,560 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 13:10:18 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:08:58 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:06:53 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:06:44 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-03-08 13:06:43 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 13:06:13 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:06:03 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:05:05 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-03-08 13:05:05 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.028 |  |
| 2026-03-08 13:05:00 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-08 13:04:14 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:04:09 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:04:06 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-08 13:03:43 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:37 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-03-08 13:03:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:32 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-03-08 13:03:15 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:11 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:02:54 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:02:49 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:02:37 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 13:02:26 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:02:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:59 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:51 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 13:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:17 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.053 |  |
| 2026-03-08 13:01:11 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:07 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:07 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-03-08 13:00:57 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:00:40 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-08 13:00:07 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 12:22:29 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 13:01:07 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-03-08 13:05:05 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-03-08 13:03:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-08 13:00:07 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 13:01:51 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 13:00:40 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-08 13:02:37 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 13:06:43 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 13:02:49 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:59 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:00:57 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:08:58 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:04:09 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:15 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:11 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:00:27 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:07 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:04:14 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:01:33 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:02:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:10:18 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:02:54 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:06:53 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:43 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:01:11 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:06:03 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-08 11:07:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:06:13 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:04:06 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:02:26 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:05:00 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-08 13:03:32 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-03-08 12:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-03-08 13:05:05 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.028 |  |
| 2026-03-08 13:03:37 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-03-08 13:06:44 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-03-08 13:01:17 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)