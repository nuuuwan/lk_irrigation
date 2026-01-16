# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_13:05:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,158 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 13:05:26 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:05:22 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:05:10 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:05:04 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:05:03 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.047 |  |
| 2026-01-16 13:05:01 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-01-16 13:04:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:04:22 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-01-16 13:03:18 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-01-16 13:03:16 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:03:11 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 13:03:10 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-16 13:02:58 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:02:53 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:45 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:02:45 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:42 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 13:02:22 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:18 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:01:58 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:01:54 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:01:51 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:01:23 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:01:13 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:01:11 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:01:00 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 13:00:55 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:00:34 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-16 12:23:40 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.015 |  |
| 2026-01-16 12:21:09 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:14:12 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-01-16 12:14:09 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.047 |  |
| 2026-01-16 12:09:52 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 13:05:01 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-01-16 13:03:10 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-16 13:03:11 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 13:01:00 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 12:03:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 13:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 13:01:58 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:01:11 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:42 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:00:34 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:05:04 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:01:13 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:05:22 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:22 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:03:16 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:05:10 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:04:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:45 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:53 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:05:26 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:01:23 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:58 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:01:29 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 13:02:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:01:51 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-16 12:01:16 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:02:18 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:01:54 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:02:45 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:00:55 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-16 13:04:22 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-01-16 12:23:40 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.015 |  |
| 2026-01-16 12:02:46 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-01-16 12:08:14 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-01-16 13:03:18 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-01-16 13:05:03 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.047 |  |
| 2026-01-16 12:00:23 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.057 |  |
| 2026-01-16 12:03:55 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)