# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_03:16:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 03:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-02-09 03:14:09 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.028 |  |
| 2026-02-09 03:14:00 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-09 03:11:26 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:08:54 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:08:52 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:07:57 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.194 |  |
| 2026-02-09 03:07:52 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-02-09 03:06:58 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 03:05:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:05:47 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:05:45 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:04:22 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:04:17 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-09 03:04:16 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-09 03:04:15 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-09 03:04:14 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-09 03:04:12 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:04:12 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-09 03:03:34 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:03:25 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-09 03:03:07 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:02:54 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-09 03:02:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-02-09 03:02:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.050 |  |
| 2026-02-09 03:02:03 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:01:33 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:01:13 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:01:09 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:01:04 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:00:59 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:00:51 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:00:46 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:00:38 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:55:51 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:54:20 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:54:18 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:52:25 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-02-09 02:34:34 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:34:06 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 03:04:17 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-09 02:21:12 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 11.058 | 🔺 Rising |
| 2026-02-09 03:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-02-09 03:02:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-02-09 02:24:17 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-09 03:14:00 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-09 03:06:58 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 03:02:54 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-09 03:00:51 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:01:39 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:07:24 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:04:12 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:34:34 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:01:04 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:03:34 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:00:59 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:02:03 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:03:07 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:04:22 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:05:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:08:52 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:11:26 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:04:45 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:01:33 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:08:54 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:01:13 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-09 03:03:25 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-09 03:00:38 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-09 01:00:49 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:07:43 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.013 |  |
| 2026-02-09 01:13:08 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.018 |  |
| 2026-02-09 03:07:52 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-02-09 02:02:20 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-02-09 03:14:09 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.028 |  |
| 2026-02-09 03:02:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.050 |  |
| 2026-02-08 18:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.187 |  |
| 2026-02-09 03:07:57 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)