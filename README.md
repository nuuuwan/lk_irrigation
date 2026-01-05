# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_05:13:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,895 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 05:13:48 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-06 05:12:31 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:11:44 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-06 05:10:39 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2026-01-06 05:09:40 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.027 |  |
| 2026-01-06 05:09:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2026-01-06 05:09:00 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-01-06 05:08:59 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-01-06 05:08:58 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-01-06 05:07:41 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-06 05:07:35 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-01-06 05:05:54 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:05:52 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-06 05:05:50 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-06 05:05:44 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-06 05:05:35 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:05:28 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-01-06 05:05:28 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:05:05 | Siyambalanduwa (Heda Oya) | 3.03 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-01-06 05:04:39 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.253 |  |
| 2026-01-06 05:03:51 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 05:03:34 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-06 05:03:12 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.171 |  |
| 2026-01-06 05:03:10 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.067 |  |
| 2026-01-06 05:02:45 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:02:30 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:02:27 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 05:02:12 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.013 |  |
| 2026-01-06 05:02:10 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-06 05:01:37 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:01:31 | Padiyathalawa (Maduru Oya) | 2.70 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-06 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:00:48 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-06 04:35:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 05:09:00 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-01-06 05:05:05 | Siyambalanduwa (Heda Oya) | 3.03 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-01-06 03:14:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-06 05:05:44 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-06 05:01:31 | Padiyathalawa (Maduru Oya) | 2.70 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-06 05:00:48 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-06 05:02:27 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 05:05:52 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-06 05:05:50 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-06 05:13:48 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-06 04:04:04 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 05:11:44 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-06 05:03:51 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 05:03:34 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-06 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:05:54 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:02:30 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:01:37 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:35:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:02:45 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:05:35 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:12:31 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 05:05:28 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:09:47 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.005 |  |
| 2026-01-06 05:02:10 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-06 05:07:41 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-06 05:02:12 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.013 |  |
| 2026-01-06 05:05:28 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-01-06 05:09:40 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.027 |  |
| 2026-01-06 05:09:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2026-01-06 05:10:39 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2026-01-06 05:07:35 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-01-06 05:03:10 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.067 |  |
| 2026-01-06 05:03:12 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.171 |  |
| 2026-01-06 04:07:23 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.173 |  |
| 2026-01-06 05:04:39 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)