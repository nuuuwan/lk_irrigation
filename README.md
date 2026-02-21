# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_02:35:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,579 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 02:35:32 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:17:39 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-02-22 02:16:46 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-02-22 02:11:37 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:11:09 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-22 02:10:06 | Urawa (Nilwala Ganga) | 2.92 | 🟡 Alert | 10.421 | 🔺 Rising |
| 2026-02-22 02:09:28 | Urawa (Nilwala Ganga) | 2.81 | 🟡 Alert | 10.421 | 🔺 Rising |
| 2026-02-22 02:09:27 | Pitabeddara (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-22 02:08:34 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -0.044 |  |
| 2026-02-22 02:08:00 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-22 02:07:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-22 02:07:27 | Rathnapura (Kalu Ganga) | 5.13 | 🟢 Normal | -0.147 |  |
| 2026-02-22 02:07:21 | Dunamale (Aththanagalu Oya) | 1.45 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-22 02:07:13 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-22 02:06:56 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-02-22 02:06:34 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.104 |  |
| 2026-02-22 02:05:55 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | -0.051 |  |
| 2026-02-22 02:05:11 | Wellawaya (Kirindi Oya) | 2.34 | 🟢 Normal | -0.496 |  |
| 2026-02-22 02:05:09 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:04:43 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-02-22 02:04:38 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.261 |  |
| 2026-02-22 02:04:37 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-02-22 02:04:19 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.457 |  |
| 2026-02-22 02:04:09 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.095 |  |
| 2026-02-22 02:03:59 | Manampitiya (Mahaweli Ganga) | 3.72 | 🟡 Alert | 0.339 | 🔺 Rising |
| 2026-02-22 02:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 8.757 | 🔺 Rising |
| 2026-02-22 02:03:21 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.062 |  |
| 2026-02-22 02:03:17 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 8.757 | 🔺 Rising |
| 2026-02-22 02:02:34 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:02:32 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:02:30 | Kuda Oya (Kirindi Oya) | 2.88 | 🟢 Normal | 0.613 | 🔺 Rising |
| 2026-02-22 02:02:29 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.141 |  |
| 2026-02-22 02:02:28 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | 0.658 | 🔺 Rising |
| 2026-02-22 02:01:50 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-22 02:01:22 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-22 02:01:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 02:10:06 | Urawa (Nilwala Ganga) | 2.92 | 🟡 Alert | 10.421 | 🔺 Rising |
| 2026-02-22 02:03:59 | Manampitiya (Mahaweli Ganga) | 3.72 | 🟡 Alert | 0.339 | 🔺 Rising |
| 2026-02-22 02:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 8.757 | 🔺 Rising |
| 2026-02-22 02:02:28 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | 0.658 | 🔺 Rising |
| 2026-02-22 02:02:30 | Kuda Oya (Kirindi Oya) | 2.88 | 🟢 Normal | 0.613 | 🔺 Rising |
| 2026-02-22 02:04:37 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-02-22 02:16:46 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-02-22 02:17:39 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-02-22 02:06:56 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-02-22 02:04:43 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-02-22 02:07:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-22 02:07:13 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-22 02:07:21 | Dunamale (Aththanagalu Oya) | 1.45 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-22 01:07:43 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-22 02:08:00 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-22 02:11:09 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-22 02:09:27 | Pitabeddara (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 02:02:34 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:11:37 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:03:17 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:35:32 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:02:32 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:01:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:05:09 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:01:22 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-22 02:01:50 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-22 02:08:34 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -0.044 |  |
| 2026-02-22 02:05:55 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | -0.051 |  |
| 2026-02-22 02:03:21 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.062 |  |
| 2026-02-22 02:04:09 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.095 |  |
| 2026-02-22 02:06:34 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.104 |  |
| 2026-02-22 02:02:29 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.141 |  |
| 2026-02-22 02:07:27 | Rathnapura (Kalu Ganga) | 5.13 | 🟢 Normal | -0.147 |  |
| 2026-02-22 02:04:38 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.261 |  |
| 2026-02-22 02:04:19 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.457 |  |
| 2026-02-22 02:05:11 | Wellawaya (Kirindi Oya) | 2.34 | 🟢 Normal | -0.496 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)