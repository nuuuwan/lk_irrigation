# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--19_07:23:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,639 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 07:23:37 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:13:30 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:11:24 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-19 07:10:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.053 |  |
| 2026-01-19 07:09:38 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:08:37 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.027 |  |
| 2026-01-19 07:08:33 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:08:21 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.009 |  |
| 2026-01-19 07:08:13 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.001 |  |
| 2026-01-19 07:07:07 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-19 07:06:41 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:06:11 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:06:06 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-01-19 07:05:48 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-01-19 07:05:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:05:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.143 |  |
| 2026-01-19 07:04:48 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:04:23 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:04:06 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:04:03 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:45 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.019 |  |
| 2026-01-19 07:03:43 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.029 |  |
| 2026-01-19 07:03:39 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:31 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:15 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:11 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:09 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-01-19 07:03:08 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:02:35 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.058 |  |
| 2026-01-19 07:02:17 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-19 07:02:11 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:01:10 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:01:08 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-19 06:40:47 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.137 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 07:11:24 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-19 07:02:17 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-19 06:01:45 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-19 07:07:07 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-19 07:08:13 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.001 |  |
| 2026-01-19 07:05:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:11 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:08:33 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 06:02:47 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:09:38 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:06:41 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:08 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:23:37 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:15 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:04:03 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:39 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-19 06:03:49 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:02:11 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:02:35 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:04:23 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:04:48 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:06:11 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:03:31 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:04:06 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:13:30 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-19 06:04:37 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:01:10 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:01:08 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-19 07:08:21 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.009 |  |
| 2026-01-19 07:03:45 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.019 |  |
| 2026-01-19 07:03:09 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-01-19 06:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-01-19 07:08:37 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.027 |  |
| 2026-01-19 07:03:43 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.029 |  |
| 2026-01-19 07:05:48 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-01-19 07:06:06 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-01-19 07:10:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.053 |  |
| 2026-01-19 07:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.058 |  |
| 2026-01-19 07:05:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)