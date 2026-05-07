# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_01:34:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,756 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 01:34:40 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-08 01:12:04 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.005 |  |
| 2026-05-08 01:09:26 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.278 |  |
| 2026-05-08 01:07:45 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.246 |  |
| 2026-05-08 01:07:17 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-05-08 01:07:16 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -6.300 |  |
| 2026-05-08 01:07:04 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-05-08 01:06:43 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.054 |  |
| 2026-05-08 01:06:36 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -6.300 |  |
| 2026-05-08 01:06:28 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-08 01:05:42 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.139 |  |
| 2026-05-08 01:05:21 | Pitabeddara (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 01:05:19 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.131 |  |
| 2026-05-08 01:04:43 | Thanamalwila (Kirindi Oya) | 3.51 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-08 01:04:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.016 |  |
| 2026-05-08 01:04:03 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -1.800 |  |
| 2026-05-08 01:04:00 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 01:03:43 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -1.800 |  |
| 2026-05-08 01:03:32 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-05-08 01:03:23 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-05-08 01:03:10 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | -0.226 |  |
| 2026-05-08 01:03:10 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-05-08 01:02:55 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 01:02:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-08 01:02:21 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.064 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 23:00:34 | Weraganthota (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.746 | 🔺 Rising |
| 2026-05-08 01:07:04 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-05-08 01:03:32 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-05-08 01:03:23 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-05-08 01:02:13 | Thawalama (Gin Ganga) | 3.44 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-05-08 01:03:10 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-05-08 01:01:31 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-08 01:02:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-08 01:04:43 | Thanamalwila (Kirindi Oya) | 3.51 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-08 00:06:27 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-08 01:34:40 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-08 01:05:21 | Pitabeddara (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 01:04:00 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 01:06:28 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-08 01:02:01 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 01:01:08 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-08 01:02:55 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:00:30 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 01:12:04 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.005 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 01:01:19 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-05-08 01:01:22 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-08 01:04:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.016 |  |
| 2026-05-08 01:07:17 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-05-08 01:00:56 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.031 |  |
| 2026-05-08 01:06:43 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.054 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-08 01:02:21 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.064 |  |
| 2026-05-08 01:05:19 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.131 |  |
| 2026-05-08 01:05:42 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.139 |  |
| 2026-05-08 01:01:12 | Kuda Oya (Kirindi Oya) | 3.52 | 🟢 Normal | -0.215 |  |
| 2026-05-08 01:01:08 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.226 |  |
| 2026-05-08 01:03:10 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | -0.226 |  |
| 2026-05-08 01:07:45 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.246 |  |
| 2026-05-08 01:09:26 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.278 |  |
| 2026-05-08 01:04:03 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -1.800 |  |
| 2026-05-08 01:07:16 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -6.300 |  |
| 2026-05-08 00:17:05 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)