# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_05:06:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,675 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 05:06:55 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:06:12 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:06:11 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 05:05:43 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:05:30 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-20 05:05:25 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:05:13 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-20 05:04:48 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-05-20 05:04:28 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.050 |  |
| 2026-05-20 05:04:15 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-20 05:04:10 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-20 05:04:05 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2026-05-20 05:03:30 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.027 |  |
| 2026-05-20 05:03:22 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.011 |  |
| 2026-05-20 05:03:05 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-20 05:02:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-05-20 05:02:54 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:02:51 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 05:02:04 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-20 05:01:57 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:01:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.124 |  |
| 2026-05-20 05:01:28 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-20 05:01:16 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:01:02 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:00:42 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-20 05:00:27 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:49:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:49:09 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:42:00 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:21:58 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.015 |  |
| 2026-05-20 04:18:53 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.027 |  |
| 2026-05-20 04:17:35 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 05:02:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-05-20 05:02:04 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-20 05:03:05 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-20 04:11:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-20 05:04:15 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-20 05:05:30 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-20 05:02:51 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 05:06:11 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:05:43 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:05:25 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:01:57 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:02:54 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:01:02 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:06:55 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:04:05 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:00:27 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:02:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:01:16 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 05:06:12 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:11:26 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-20 03:04:46 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-05-20 05:05:13 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-20 05:01:28 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-20 05:00:42 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-20 04:02:19 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-20 05:04:48 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-05-20 05:03:22 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.011 |  |
| 2026-05-20 04:21:58 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.015 |  |
| 2026-05-20 05:04:10 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-20 04:05:31 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-05-20 05:03:30 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.027 |  |
| 2026-05-20 04:03:29 | Moragaswewa (Deduru Oya) | 1.62 | 🟢 Normal | -0.039 |  |
| 2026-05-20 05:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2026-05-20 05:04:28 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.050 |  |
| 2026-05-20 05:01:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)