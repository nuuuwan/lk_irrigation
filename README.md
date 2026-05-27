# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_19:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,269 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 19:03:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:02:58 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 19:02:41 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:02:39 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-27 19:02:35 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:02:27 | Deraniyagala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-05-27 19:02:25 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-27 19:02:20 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-05-27 19:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-05-27 19:02:13 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-27 19:01:58 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 19:01:57 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:01:20 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:01:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:01:11 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 19:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.39 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-05-27 19:00:45 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:00:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:00:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:00:26 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 19:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.39 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-05-27 19:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-05-27 18:04:34 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-27 19:02:13 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-27 19:02:39 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-27 19:00:26 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-27 18:05:46 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 18:04:41 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-27 19:01:11 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 19:02:58 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 18:02:17 | Ellagawa (Kalu Ganga) | 8.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 19:01:58 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 19:02:35 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:00:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:00:21 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:00:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:12 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:00:45 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:02:41 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:03:52 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:04:13 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:03:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:08 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:05:00 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:03:26 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:01:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:04:11 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:08:31 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:01:57 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-27 19:01:20 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-27 19:02:25 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-27 18:06:50 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-05-27 19:02:27 | Deraniyagala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-05-27 19:02:20 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-05-27 18:08:25 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-05-27 18:05:58 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)