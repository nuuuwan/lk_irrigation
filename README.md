# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_13:55:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,101 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 13:55:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-09 13:22:44 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.016 |  |
| 2026-05-09 13:20:10 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.008 |  |
| 2026-05-09 13:14:07 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.018 |  |
| 2026-05-09 13:13:04 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:13:02 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.079 |  |
| 2026-05-09 13:10:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.69 | 🟢 Normal | -0.054 |  |
| 2026-05-09 13:09:35 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.018 |  |
| 2026-05-09 13:09:08 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.037 |  |
| 2026-05-09 13:09:07 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:08:49 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:07:41 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.037 |  |
| 2026-05-09 13:07:34 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 13:06:50 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-09 13:06:05 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-09 13:55:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-09 13:08:49 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:04:44 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:01:07 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:59:46 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:01:10 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:13:04 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:09:07 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:01:04 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:20:10 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.008 |  |
| 2026-05-09 13:05:35 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-05-09 13:06:15 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-05-09 13:02:22 | Thanamalwila (Kirindi Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-05-09 13:04:03 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.014 |  |
| 2026-05-09 13:22:44 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.016 |  |
| 2026-05-09 13:14:07 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.018 |  |
| 2026-05-09 13:09:35 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.018 |  |
| 2026-05-09 13:00:20 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-05-09 13:04:49 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-05-09 13:03:16 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-05-09 13:02:04 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.031 |  |
| 2026-05-09 13:09:08 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.037 |  |
| 2026-05-09 13:07:41 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.037 |  |
| 2026-05-09 13:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.040 |  |
| 2026-05-09 13:03:57 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.044 |  |
| 2026-05-09 13:07:34 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.047 |  |
| 2026-05-09 13:06:49 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.047 |  |
| 2026-05-09 13:02:58 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.051 |  |
| 2026-05-09 13:10:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.69 | 🟢 Normal | -0.054 |  |
| 2026-05-09 13:00:51 | Galgamuwa (Mee Oya) | 2.55 | 🟢 Normal | -0.059 |  |
| 2026-05-09 13:00:37 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.067 |  |
| 2026-05-09 13:04:55 | Kuda Oya (Kirindi Oya) | 2.53 | 🟢 Normal | -0.076 |  |
| 2026-05-09 13:13:02 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.079 |  |
| 2026-05-09 13:04:14 | Katharagama (Menik Ganga) | 2.30 | 🟢 Normal | -0.079 |  |
| 2026-05-09 13:06:43 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.086 |  |
| 2026-05-09 13:06:32 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.211 |  |
| 2026-05-09 13:01:17 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -1.166 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)