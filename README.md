# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_09:12:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,977 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 09:12:11 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:08:20 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:08:15 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:08:09 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-07-13 09:07:23 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:07:06 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.064 |  |
| 2026-07-13 09:05:56 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:05:35 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:05:35 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-07-13 09:05:28 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:05:18 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-07-13 09:04:40 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-13 09:04:32 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-13 09:04:23 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 09:04:17 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:04:15 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-07-13 09:03:50 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:03:25 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.013 |  |
| 2026-07-13 09:03:23 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:03:21 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:03:15 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.054 |  |
| 2026-07-13 09:03:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:02:50 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:02:47 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:02:25 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:02:17 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:02:10 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:01:58 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:48 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:37 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.053 |  |
| 2026-07-13 09:01:28 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:20 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:06 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-13 09:00:32 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:00:21 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.074 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 09:00:21 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-07-13 09:04:40 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-13 09:01:06 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-13 09:04:32 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-13 08:05:28 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 09:04:23 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 09:00:32 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:20 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:03:50 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:12:11 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:05:28 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:04:17 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:58 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:02:50 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:05:35 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:07:06 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:48 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:03:21 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:07:23 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:01:28 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:02:17 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:05:56 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 09:05:35 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-07-13 09:08:20 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:02:47 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:02:25 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:03:23 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:02:10 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:03:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:08:15 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-07-13 09:03:25 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.013 |  |
| 2026-07-13 09:08:09 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-07-13 09:05:18 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-07-13 09:04:15 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-07-13 09:01:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.053 |  |
| 2026-07-13 09:03:15 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.054 |  |
| 2026-07-13 09:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)