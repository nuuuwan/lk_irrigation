# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_13:23:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,381 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 13:23:16 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.016 |  |
| 2026-02-09 13:20:58 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-02-09 13:17:57 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.095 |  |
| 2026-02-09 13:16:22 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.008 |  |
| 2026-02-09 13:12:53 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.026 |  |
| 2026-02-09 13:09:13 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:09:04 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:08:33 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 13:08:06 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.003 |  |
| 2026-02-09 13:08:04 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:06:10 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:05:36 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.026 |  |
| 2026-02-09 13:04:38 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:04:16 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-02-09 13:04:11 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:04:05 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:47 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-02-09 13:03:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:39 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:17 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:05 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:03 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:02:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:02:25 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:02:09 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:02:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-02-09 13:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-09 13:01:56 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-09 13:01:49 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 13:01:47 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:01:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:01:12 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:00:53 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:00:46 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:00:19 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-09 13:00:08 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:00:08 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 13:01:56 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-09 13:00:19 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-09 13:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-09 13:08:33 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 13:01:49 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 13:08:06 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.003 |  |
| 2026-02-09 13:01:47 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:02:09 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:00:08 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:08:04 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:09:04 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:01:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:17 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:09:13 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:39 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:01:12 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:00:08 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:05 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:03:03 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:04:38 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:00:53 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:04:11 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:04:05 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 13:20:58 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-02-09 13:16:22 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.008 |  |
| 2026-02-09 13:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:02:25 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:02:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:06:10 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:00:46 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-09 13:02:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-02-09 13:23:16 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.016 |  |
| 2026-02-09 13:04:16 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-02-09 13:05:36 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.026 |  |
| 2026-02-09 13:12:53 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.026 |  |
| 2026-02-09 13:03:47 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-02-09 12:05:47 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-02-09 13:17:57 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)