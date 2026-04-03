# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_15:03:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,109 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 15:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-03 15:03:14 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:03:11 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:03:03 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-04-03 15:03:02 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 15:03:01 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-03 15:02:54 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-03 15:02:42 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-03 15:02:41 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:02:31 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:02:23 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.020 |  |
| 2026-04-03 15:02:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-03 15:02:11 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:02:10 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-03 15:02:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 15:02:04 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 15:02:01 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:01:45 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:01:20 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-03 15:01:00 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-03 15:00:53 | Thanthirimale (Malwathu Oya) | 3.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-03 15:00:15 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.192 |  |
| 2026-04-03 14:31:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-03 14:22:18 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:18:54 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.028 |  |
| 2026-04-03 14:15:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-03 14:14:13 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-03 14:11:14 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:10:32 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.058 |  |
| 2026-04-03 14:10:22 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:10:13 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.192 |  |
| 2026-04-03 14:09:54 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 15:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-03 15:02:54 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-03 15:02:42 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-03 14:31:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-03 15:00:53 | Thanthirimale (Malwathu Oya) | 3.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-03 14:01:35 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-03 15:02:10 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-03 15:02:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 15:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-03 15:02:04 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 15:03:02 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 14:14:13 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-03 15:02:01 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:01:20 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:06:11 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:06:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:10:22 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:02:42 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:05:23 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:06:50 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:03:11 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:03:14 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:02:17 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 14:04:12 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:01:45 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:02:41 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:02:31 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:02:11 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:02:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-03 14:02:55 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-03 15:03:01 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-03 15:02:23 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.020 |  |
| 2026-04-03 15:01:00 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-03 15:03:03 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-04-03 14:18:54 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.028 |  |
| 2026-04-03 14:06:56 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.031 |  |
| 2026-04-03 14:10:32 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.058 |  |
| 2026-04-03 15:00:15 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.192 |  |
| 2026-04-03 14:04:41 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.237 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)