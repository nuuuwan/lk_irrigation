# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_21:20:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,794 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 21:20:33 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:13:08 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:12:47 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:10:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-13 21:09:25 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:08:21 | Horowpothana (Yan Oya) | 3.86 | 🟢 Normal | -0.045 |  |
| 2026-01-13 21:07:59 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-13 21:07:57 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2026-01-13 21:07:46 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-13 21:07:09 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:06:49 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-13 21:06:24 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:06:06 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:05:05 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 21:04:56 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 21:04:11 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-13 21:03:59 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-13 21:03:40 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-01-13 21:03:39 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:03:30 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:03:15 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:02:59 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-13 21:02:57 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:02:51 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:02:43 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-13 21:02:15 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 21:02:08 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:01:58 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:01:25 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 21:01:23 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-01-13 21:01:03 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 21:00:50 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:00:36 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:00:31 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:00:23 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 21:01:23 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-01-13 21:03:59 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-13 21:10:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-13 21:04:11 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-13 21:00:23 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 21:02:43 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-13 21:02:15 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 21:07:59 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-13 21:01:03 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 21:01:25 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 21:04:56 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 21:05:05 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 21:03:30 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:02:08 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:06:24 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:01:58 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:02:57 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:00:36 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:20:33 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:06:06 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:02:51 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:00:50 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:00:31 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:09:25 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:03:39 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:07:09 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:13:08 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:03:15 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 21:06:49 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-13 21:02:59 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-13 21:07:46 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-13 21:07:57 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2026-01-13 20:12:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.018 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-13 21:03:40 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-01-13 21:08:21 | Horowpothana (Yan Oya) | 3.86 | 🟢 Normal | -0.045 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)