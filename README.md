# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_22:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 22:10:18 | Panadugama (Nilwala Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:08:37 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:08:27 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:07:41 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-04-08 22:07:21 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:06:28 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:05:40 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:05:39 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:04:43 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 22:04:26 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:03:45 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-08 22:03:35 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:03:32 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-04-08 22:03:30 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-04-08 22:03:27 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-04-08 22:03:18 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-08 22:02:46 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:02:45 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-08 22:02:37 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.144 |  |
| 2026-04-08 22:02:30 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:02:21 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-08 22:02:17 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-08 22:02:17 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 22:02:12 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:01:54 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:01:39 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-04-08 22:01:39 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:01:22 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:01:19 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:00:50 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:00:09 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 18:05:20 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 5.983 | 🔺 Rising |
| 2026-04-08 22:03:30 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-04-08 22:02:17 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-08 22:02:17 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 22:03:18 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-08 22:04:43 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 22:01:39 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:00:09 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 21:06:19 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:01:19 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:03:35 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:02:30 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:02:12 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:05:40 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:08:27 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:07:21 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:10:18 | Panadugama (Nilwala Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:04:26 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:00:50 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 21:17:58 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:02:46 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:05:39 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:01:54 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:06:28 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:08:37 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-08 22:01:22 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-08 21:08:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:20 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-08 22:03:45 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-08 22:02:21 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-08 22:02:45 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-08 21:07:27 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.011 |  |
| 2026-04-08 21:03:27 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-04-08 22:03:32 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-04-08 22:03:27 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-04-08 22:01:39 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-04-08 22:07:41 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-04-08 22:02:37 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)