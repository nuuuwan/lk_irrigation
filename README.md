# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_17:05:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,523 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 17:05:07 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:04:52 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:04:34 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:04:27 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.011 |  |
| 2026-01-14 17:04:22 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:04:02 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.058 |  |
| 2026-01-14 17:03:52 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-01-14 17:03:11 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-01-14 17:03:07 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-14 17:02:49 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:02:47 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:02:40 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-01-14 17:02:38 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-14 17:02:29 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:02:26 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.031 |  |
| 2026-01-14 17:02:21 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:02:16 | Dunamale (Aththanagalu Oya) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-01-14 17:02:14 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-14 17:02:12 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-01-14 17:02:12 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:01:59 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-01-14 17:01:58 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.199 |  |
| 2026-01-14 17:01:38 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:01:38 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-01-14 17:01:34 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:01:14 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:01:12 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:24:31 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-14 16:17:48 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:12:32 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:11:16 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-01-14 16:10:22 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:09:29 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-01-14 16:08:56 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:08:52 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 17:02:12 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-01-14 17:02:14 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-14 16:24:31 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-14 17:01:38 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:01:12 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:04:22 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:04:34 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:10:22 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:17:48 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:02:29 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:02:12 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:08:23 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:04:52 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:05:07 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:02:49 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:07 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:05:52 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 17:01:34 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:02:47 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:01:14 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:01:30 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:02:21 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:04:27 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.011 |  |
| 2026-01-14 17:03:52 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-01-14 17:01:59 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-01-14 17:02:16 | Dunamale (Aththanagalu Oya) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-01-14 16:01:34 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.020 |  |
| 2026-01-14 17:03:07 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-14 17:03:11 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-01-14 17:02:38 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-14 17:02:40 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-01-14 17:02:26 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.031 |  |
| 2026-01-14 17:01:38 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-01-14 17:04:02 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.058 |  |
| 2026-01-14 16:02:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.111 |  |
| 2026-01-14 17:01:58 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)