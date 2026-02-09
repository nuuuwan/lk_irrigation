# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_19:12:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,615 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 19:12:48 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:07:48 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:07:37 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 19:06:53 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:06:53 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:06:39 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:05:54 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:05:46 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 19:05:45 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-09 19:05:25 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-09 19:05:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:05:13 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:05:00 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:04:47 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 19:04:15 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:04:12 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:03:54 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 19:03:53 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 19:03:30 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:03:02 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:02:39 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:02:36 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-09 19:02:28 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-02-09 19:02:27 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:02:15 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-09 19:02:12 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:01:40 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:01:38 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:01:31 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-02-09 19:01:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.063 |  |
| 2026-02-09 19:01:12 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.010 |  |
| 2026-02-09 19:00:56 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:00:32 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:00:22 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 19:02:28 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-02-09 18:04:30 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-09 19:05:25 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-09 19:03:53 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 19:05:45 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-09 19:05:46 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 19:07:37 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 19:04:47 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 19:03:54 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 19:01:40 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:02:27 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:03:02 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:01:38 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:05:00 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:06:53 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:07:48 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:03:30 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:04:12 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:00:56 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:12:48 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:00:22 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:05:54 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:02:39 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:06:53 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:05:13 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:02:12 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:06:39 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:05:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:04:15 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-09 19:02:36 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-09 19:01:12 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-09 19:02:15 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-02-09 19:01:31 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-02-09 19:01:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.063 |  |
| 2026-02-09 18:01:51 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)