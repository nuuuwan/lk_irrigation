# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_02:08:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 02:08:17 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:07:40 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:06:54 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-01-29 02:05:47 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:05:36 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:05:13 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.162 |  |
| 2026-01-29 02:04:22 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-01-29 02:03:52 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-29 02:03:38 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-29 02:03:34 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-29 02:03:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:03:12 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 02:03:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 02:02:52 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:46 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:37 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:22 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-01-29 02:02:07 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:07 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:00 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:56 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:45 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:37 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:23 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:19 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:15 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:12 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-01-29 02:01:00 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-01-29 02:00:39 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 01:31:45 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 01:16:22 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 02:01:12 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-01-29 02:03:52 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-29 01:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-29 02:02:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 02:03:38 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-29 02:03:12 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 18:04:28 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 02:02:46 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:23 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:05:36 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-28 23:10:05 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:15 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:05:47 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:19 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:03:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-29 01:11:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:37 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 00:05:30 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:52 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:56 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:45 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:00 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:07 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:08:17 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:07:40 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:03:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:07 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:00:39 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:02:22 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-01-29 02:03:34 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-29 01:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-29 01:01:01 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-01-28 18:00:30 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-01-29 02:04:22 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-01-29 02:06:54 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-01-29 02:01:00 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-01-28 18:05:41 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.084 |  |
| 2026-01-29 02:05:13 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.162 |  |
| 2026-01-29 01:15:12 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)