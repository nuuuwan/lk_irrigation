# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_10:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,608 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 10:10:24 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 10:09:31 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-01 10:09:05 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:08:07 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-01-01 10:07:59 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:07:23 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-01 10:06:59 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.022 |  |
| 2026-01-01 10:06:30 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-01 10:05:30 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-01 10:05:19 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:04:54 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:04:32 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-01 10:04:05 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:03:58 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 10:03:44 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-01-01 10:03:38 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-01 10:03:23 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.089 |  |
| 2026-01-01 10:03:22 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.051 |  |
| 2026-01-01 10:02:58 | Siyambalanduwa (Heda Oya) | 1.60 | 🟢 Normal | -0.116 |  |
| 2026-01-01 10:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:02:12 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.081 |  |
| 2026-01-01 10:02:11 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.119 |  |
| 2026-01-01 10:02:06 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-01 10:01:58 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:01:19 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-01 10:01:08 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 10:01:05 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:00:54 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-01 10:00:40 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-01 10:00:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.012 |  |
| 2026-01-01 10:00:19 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:00:09 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.984 | 🔺 Rising |
| 2026-01-01 09:34:47 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.025 |  |
| 2026-01-01 09:19:45 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:19:17 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.024 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 10:00:09 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.984 | 🔺 Rising |
| 2026-01-01 10:06:30 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-01 10:04:32 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-01 09:15:36 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-01 10:01:19 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-01 10:00:54 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-01 10:01:08 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 09:01:07 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 10:03:58 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 10:05:30 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-01 10:09:31 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-01 10:10:24 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 10:01:05 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:07:59 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:01:58 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:09:05 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:03:22 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:05:19 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:04:05 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:00:19 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:04:54 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:12:34 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-01-01 10:08:07 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-01-01 10:02:06 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:02:04 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-01 10:00:40 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-01 10:07:23 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-01 10:00:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.012 |  |
| 2026-01-01 09:07:58 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.014 |  |
| 2026-01-01 10:03:38 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-01 10:06:59 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.022 |  |
| 2026-01-01 09:34:47 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.025 |  |
| 2026-01-01 10:03:44 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-01-01 10:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.051 |  |
| 2026-01-01 10:02:12 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.081 |  |
| 2026-01-01 10:03:23 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.089 |  |
| 2026-01-01 10:02:58 | Siyambalanduwa (Heda Oya) | 1.60 | 🟢 Normal | -0.116 |  |
| 2026-01-01 10:02:11 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)