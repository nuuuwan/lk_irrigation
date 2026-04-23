# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_09:12:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,726 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 09:12:24 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:10:17 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-23 09:08:41 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-23 09:08:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 09:08:29 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.070 |  |
| 2026-04-23 09:07:26 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.032 |  |
| 2026-04-23 09:06:22 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:05:27 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.019 |  |
| 2026-04-23 09:05:24 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 09:05:04 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.188 |  |
| 2026-04-23 09:04:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-23 09:04:21 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.032 |  |
| 2026-04-23 09:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.048 |  |
| 2026-04-23 09:03:28 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 09:03:27 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.231 |  |
| 2026-04-23 09:03:19 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-23 09:03:14 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.019 |  |
| 2026-04-23 09:03:10 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-23 09:03:08 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-23 09:03:04 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:03:03 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-04-23 09:02:59 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-23 09:02:58 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-23 09:02:56 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:02:55 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.101 |  |
| 2026-04-23 09:02:45 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-04-23 09:02:22 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:01:59 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-04-23 09:01:57 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.098 |  |
| 2026-04-23 09:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:01:21 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-23 09:01:11 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-23 09:01:01 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.022 |  |
| 2026-04-23 09:00:38 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-23 09:00:21 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:00:15 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.108 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 09:03:08 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-23 09:02:58 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-23 09:03:10 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-23 09:01:11 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-23 09:08:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 09:05:24 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 09:08:41 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-23 09:03:28 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 08:04:57 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 09:00:21 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:02:56 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:06:22 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 08:10:31 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:12:24 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:02:22 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:03:04 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 09:01:21 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-23 09:03:19 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-23 09:10:17 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-23 09:00:38 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-23 09:03:03 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-04-23 09:05:27 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.019 |  |
| 2026-04-23 09:03:14 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.019 |  |
| 2026-04-23 09:02:59 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-23 09:04:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-23 09:01:01 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.022 |  |
| 2026-04-23 09:02:45 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-04-23 09:07:26 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.032 |  |
| 2026-04-23 09:04:21 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.032 |  |
| 2026-04-23 08:01:37 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-04-23 09:01:59 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-04-23 09:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.048 |  |
| 2026-04-23 09:08:29 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.070 |  |
| 2026-04-23 09:01:57 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.098 |  |
| 2026-04-23 09:02:55 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.101 |  |
| 2026-04-23 09:00:15 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.108 |  |
| 2026-04-23 09:05:04 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.188 |  |
| 2026-04-23 09:03:27 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.231 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)