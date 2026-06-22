# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_19:19:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,537 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 19:19:16 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:19:15 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-06-22 19:10:37 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-22 19:10:13 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 19:09:42 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:09:16 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:08:11 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-22 19:07:03 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-22 19:07:02 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:06:40 | Putupaula (Kalu Ganga) | 1.86 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-22 19:06:20 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:05:22 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-06-22 19:04:37 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.012 |  |
| 2026-06-22 19:04:34 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-06-22 19:04:20 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-22 19:04:08 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-06-22 19:03:56 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:03:51 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:03:49 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-22 19:03:47 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 19:03:46 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-22 19:03:20 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:03:12 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 19:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-06-22 19:01:50 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-06-22 19:19:15 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-06-22 19:04:08 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-06-22 19:04:34 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-06-22 19:07:03 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-22 19:05:22 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-06-22 19:02:31 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-22 19:03:46 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-22 19:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-22 19:06:40 | Putupaula (Kalu Ganga) | 1.86 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-22 19:08:11 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-22 19:03:12 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-22 19:02:52 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-22 19:01:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 19:10:37 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-22 19:03:47 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 19:10:13 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 19:01:48 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:03:49 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:09:16 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:02:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:01:00 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:09:42 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:07:02 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:06:20 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:19:16 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:03:56 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:00:09 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:03:20 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:03:51 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:00:40 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-22 19:04:20 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-22 19:04:37 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.012 |  |
| 2026-06-22 19:02:07 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.017 |  |
| 2026-06-22 19:00:57 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)