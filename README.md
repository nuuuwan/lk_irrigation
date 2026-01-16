# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_02:12:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 02:12:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-17 02:12:41 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:07:25 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:05:58 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:05:48 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2026-01-17 02:05:21 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:04:44 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:04:25 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:03:46 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:03:42 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.735 |  |
| 2026-01-17 02:03:32 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-17 02:03:21 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:03:11 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:53 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.735 |  |
| 2026-01-17 02:02:52 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-17 02:02:32 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:27 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:17 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:13 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.147 |  |
| 2026-01-17 02:02:11 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:01:53 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.010 |  |
| 2026-01-17 02:01:23 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 02:01:06 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-17 02:00:45 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:00:15 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.090 |  |
| 2026-01-17 01:26:14 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.015 |  |
| 2026-01-17 01:25:48 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 02:02:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-17 02:03:32 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-16 18:00:22 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-17 02:01:06 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-17 02:12:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-17 02:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 01:20:04 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-17 02:05:21 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:01:23 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:17 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:11 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:07:25 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-16 18:06:10 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-17 01:01:17 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:04:25 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 00:12:55 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:12:41 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-17 01:11:04 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:03:21 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:03:46 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-17 01:04:15 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:00:45 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:04:44 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:03:11 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:05:58 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:27 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-17 01:05:08 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:52 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:06:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:02:32 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 01:02:21 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-17 02:01:53 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.010 |  |
| 2026-01-17 01:11:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-01-17 02:05:48 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2026-01-16 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-01-17 00:07:15 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.028 |  |
| 2026-01-17 02:00:15 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.090 |  |
| 2026-01-17 02:02:13 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.147 |  |
| 2026-01-17 02:03:42 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.735 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)