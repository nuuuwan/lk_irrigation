# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_19:35:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,837 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 19:35:10 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:20:37 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:20:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-01-12 19:17:19 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-12 19:10:13 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-01-12 19:08:11 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-12 19:07:39 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-01-12 19:07:21 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-12 19:07:07 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:06:38 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:06:37 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 19:06:16 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-12 19:06:07 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.009 |  |
| 2026-01-12 19:05:55 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:05:49 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.039 |  |
| 2026-01-12 19:05:02 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-12 19:05:01 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-12 19:04:48 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:04:24 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-12 19:03:40 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.492 | 🔺 Rising |
| 2026-01-12 19:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:03:23 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:03:04 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.050 |  |
| 2026-01-12 19:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:02:54 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-01-12 19:02:52 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-12 19:02:41 | Yaka Wewa (Ma Oya) | 1.78 | 🟢 Normal | -0.599 |  |
| 2026-01-12 19:02:28 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:02:22 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:02:04 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-01-12 19:01:45 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:01:18 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-12 19:01:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-12 19:01:10 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-01-12 19:00:40 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 19:00:36 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.100 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 19:03:40 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.492 | 🔺 Rising |
| 2026-01-12 19:02:54 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-01-12 19:02:04 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-01-12 19:04:24 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-12 19:00:36 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-12 19:05:01 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-12 19:01:18 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-12 19:06:16 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-12 19:08:11 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-12 19:17:19 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-12 19:00:40 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 19:06:37 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 19:01:45 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:20:37 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:05:55 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:02:28 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:02:22 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:35:10 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:03:23 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:04:48 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:07:07 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:06:38 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:07:39 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-01-12 19:06:07 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.009 |  |
| 2026-01-12 19:07:21 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-12 19:01:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-12 19:05:02 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-12 19:02:52 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-12 19:10:13 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-01-12 19:20:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-01-12 19:05:49 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.039 |  |
| 2026-01-12 19:03:04 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.050 |  |
| 2026-01-12 19:01:10 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-01-12 19:02:41 | Yaka Wewa (Ma Oya) | 1.78 | 🟢 Normal | -0.599 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)