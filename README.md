# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_18:09:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **201,745 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 18:09:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:07:29 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:06:42 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:06:38 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 18:05:57 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:05:25 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:37 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:29 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:21 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:18 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-09 18:04:15 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.079 |  |
| 2026-07-09 18:04:07 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:45 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:24 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:23 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-07-09 18:03:06 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:05 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:47 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 18:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.023 |  |
| 2026-07-09 18:02:37 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-09 18:02:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:27 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:27 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-09 18:02:23 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:22 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.040 |  |
| 2026-07-09 18:02:18 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:13 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:12 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-09 18:01:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:48 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:40 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:18 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.020 |  |
| 2026-07-09 18:01:18 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-09 18:01:16 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:00:20 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 18:01:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-09 18:02:12 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-09 18:02:27 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-09 18:04:18 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-09 18:06:38 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 18:02:47 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 18:00:20 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:48 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:23 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:07 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:45 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:21 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:27 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:06 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:24 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:29 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:37 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-09 17:03:50 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:18 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:02:13 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:23 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:16 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:05:25 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:05:57 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:07:29 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:40 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:09:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 17:01:51 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:18 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:06:42 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-07-09 18:02:37 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-09 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.011 |  |
| 2026-07-09 18:01:18 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.020 |  |
| 2026-07-09 18:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.023 |  |
| 2026-07-09 18:02:22 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.040 |  |
| 2026-07-09 18:04:15 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)