# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_19:19:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,839 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 19:19:10 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:13:21 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.017 |  |
| 2026-02-07 19:13:09 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:12:34 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.009 |  |
| 2026-02-07 19:08:59 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:08:46 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-02-07 19:08:30 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 19:08:04 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.044 |  |
| 2026-02-07 19:07:58 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-02-07 19:06:59 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:05:58 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:05:43 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:05:20 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 19:05:04 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:04:48 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-02-07 19:04:26 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:04:25 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:04:22 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-07 19:04:08 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 19:04:08 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:04:06 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.025 |  |
| 2026-02-07 19:03:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:03:36 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:03:25 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:03:23 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-02-07 19:03:11 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-07 19:02:31 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-07 19:02:26 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-07 19:02:15 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-07 19:02:00 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:01:53 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:01:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.095 |  |
| 2026-02-07 19:01:24 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:32 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:09 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 19:03:23 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-02-07 19:04:22 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-07 19:08:30 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 19:05:20 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 19:04:08 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 19:04:25 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:01:24 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:04:08 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:04:26 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:03:36 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:13:09 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:07:47 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:19:10 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:08:59 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:32 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:03:25 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:09 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:03:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:06:59 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:02:00 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:05:58 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:05:04 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-07 19:12:34 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.009 |  |
| 2026-02-07 19:02:31 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-07 19:03:11 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-07 19:02:15 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-07 19:13:21 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.017 |  |
| 2026-02-07 19:02:26 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-07 19:04:48 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-02-07 19:04:06 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.025 |  |
| 2026-02-07 19:08:46 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-02-07 19:07:58 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-02-07 18:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.039 |  |
| 2026-02-07 19:08:04 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.044 |  |
| 2026-02-07 19:01:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)