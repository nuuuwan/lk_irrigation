# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_04:05:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 04:05:02 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-28 04:04:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-04-28 04:03:44 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.005 |  |
| 2026-04-28 04:03:36 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.059 |  |
| 2026-04-28 04:03:23 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-04-28 04:03:06 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.035 |  |
| 2026-04-28 04:02:58 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.417 | 🔺 Rising |
| 2026-04-28 04:02:52 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-28 04:01:45 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-04-28 04:01:41 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-28 04:01:38 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-04-28 04:01:13 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.031 |  |
| 2026-04-28 04:01:11 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-28 04:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.040 |  |
| 2026-04-28 04:01:00 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 03:42:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-04-28 03:42:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-04-28 03:18:19 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -6.207 |  |
| 2026-04-28 03:17:50 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -6.207 |  |
| 2026-04-28 03:14:14 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 03:42:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-04-28 04:02:58 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.417 | 🔺 Rising |
| 2026-04-28 03:06:02 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-04-28 03:09:04 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-04-28 04:01:41 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-28 03:04:52 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-28 04:02:52 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-28 04:01:00 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 03:02:27 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-28 04:01:11 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-28 03:01:20 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 03:04:41 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 03:04:20 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:01:12 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:08:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:01:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:36 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:03:49 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:27 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:40 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:06:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-28 04:03:44 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.005 |  |
| 2026-04-28 03:10:13 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-28 04:01:45 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-04-28 04:05:02 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-28 04:03:23 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-04-28 04:04:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-04-28 04:01:13 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.031 |  |
| 2026-04-28 04:03:06 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.035 |  |
| 2026-04-28 04:01:38 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-04-28 04:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.040 |  |
| 2026-04-28 03:14:14 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-04-28 03:05:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.057 |  |
| 2026-04-28 04:03:36 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.059 |  |
| 2026-04-28 01:03:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.075 |  |
| 2026-04-28 03:18:19 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -6.207 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)