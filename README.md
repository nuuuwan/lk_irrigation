# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_20:17:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,596 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 20:17:13 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:13:59 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:11:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.045 |  |
| 2026-01-05 20:11:18 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 20:10:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-01-05 20:08:44 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:08:39 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:07:50 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.048 |  |
| 2026-01-05 20:07:41 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:06:55 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:06:53 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 20:05:39 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-05 20:05:35 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-05 20:04:57 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:04:44 | Padiyathalawa (Maduru Oya) | 2.80 | 🟢 Normal | 0.858 | 🔺 Rising |
| 2026-01-05 20:04:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-01-05 20:04:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.011 |  |
| 2026-01-05 20:04:31 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-01-05 20:04:25 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:04:06 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.093 |  |
| 2026-01-05 20:03:33 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 20:03:28 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-05 20:03:14 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-05 20:03:07 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-05 20:03:06 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-01-05 20:02:35 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-01-05 20:02:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:02:24 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 20:02:23 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:02:07 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-05 20:01:57 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 20:01:55 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:01:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-05 20:00:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:00:08 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 20:04:44 | Padiyathalawa (Maduru Oya) | 2.80 | 🟢 Normal | 0.858 | 🔺 Rising |
| 2026-01-05 20:02:35 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-05 20:05:35 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-05 20:02:24 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 20:03:07 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-05 20:05:39 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-05 20:03:14 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-05 20:06:53 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 20:01:57 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 20:03:33 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 20:11:18 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 20:02:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:00:08 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:17:13 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:02:23 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:08:44 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:13:59 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:00:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:04:25 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:04:57 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:01:55 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:08:39 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:07:41 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:06:55 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:01:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:04:31 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-01-05 20:02:07 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-05 20:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-05 20:03:28 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-05 20:04:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.011 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-05 20:03:06 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-01-05 20:04:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-01-05 20:10:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-01-05 20:11:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.045 |  |
| 2026-01-05 20:07:50 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.048 |  |
| 2026-01-05 20:04:06 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)