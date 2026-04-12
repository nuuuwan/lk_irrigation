# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_21:19:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 21:19:02 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.051 |  |
| 2026-04-12 21:09:05 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-12 21:08:04 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-12 21:08:03 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.902 | 🔺 Rising |
| 2026-04-12 21:07:46 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-12 21:07:33 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 21:07:29 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 21:07:25 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-04-12 21:07:18 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:07:07 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-04-12 21:06:10 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:06:02 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-04-12 21:05:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:05:18 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:04:56 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:04:41 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 21:04:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:03:44 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:03:06 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 21:03:02 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-12 21:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 21:02:44 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:02:30 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-04-12 21:02:30 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:02:29 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-12 21:02:29 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-12 21:02:28 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:02:13 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-04-12 21:02:01 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-12 21:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:01:39 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:01:36 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.082 |  |
| 2026-04-12 21:01:34 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 21:00:11 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 21:08:03 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.902 | 🔺 Rising |
| 2026-04-12 21:06:02 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-04-12 21:07:46 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-12 21:02:29 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-12 21:02:29 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-12 21:08:04 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-12 21:09:05 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-12 21:02:01 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-12 21:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 21:04:41 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 21:07:29 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 21:01:34 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 21:03:06 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 21:07:33 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 21:02:30 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:04:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:03:44 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:06:10 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:01:39 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:04:56 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:02:28 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:02:44 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:00:11 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:16:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:05:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:05:18 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:07:18 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 21:07:07 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-04-12 21:02:30 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-04-12 21:07:25 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-04-12 21:03:02 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-12 21:02:13 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-12 21:19:02 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.051 |  |
| 2026-04-12 21:01:36 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.082 |  |
| 2026-04-12 20:40:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)