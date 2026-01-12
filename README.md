# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_18:26:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,801 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 18:26:42 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:12:41 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.120 |  |
| 2026-01-12 18:11:29 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:11:21 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:08:44 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-12 18:07:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:07:06 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-01-12 18:06:43 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:06:42 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-01-12 18:06:07 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.028 |  |
| 2026-01-12 18:06:06 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-12 18:05:44 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-12 18:04:57 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-01-12 18:04:42 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.029 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:16 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:07 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:00 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:03:49 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-12 18:03:48 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-12 18:03:13 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.088 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:49 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-12 18:02:41 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 18:06:42 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-01-12 18:03:49 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-12 18:08:44 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-12 18:01:57 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-12 18:02:49 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-12 18:06:06 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-12 18:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-12 18:00:17 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-12 18:02:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:11:29 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:02:30 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:04:00 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:00:40 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:00:30 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:16 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:07 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:00:28 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:07:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:41 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:06:43 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:11:21 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:26:42 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:01:16 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:05:44 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-12 18:03:48 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-12 18:01:56 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.011 |  |
| 2026-01-12 18:07:06 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-01-12 18:04:57 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-01-12 18:06:07 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.028 |  |
| 2026-01-12 18:04:42 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.029 |  |
| 2026-01-12 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-01-12 18:03:13 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.088 |  |
| 2026-01-12 18:12:41 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.120 |  |
| 2026-01-12 18:01:18 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.121 |  |
| 2026-01-12 18:02:34 | Yaka Wewa (Ma Oya) | 2.38 | 🟢 Normal | -0.503 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)