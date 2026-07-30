# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_02:22:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,783 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 02:22:02 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-07-31 02:20:29 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:19:10 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-31 02:11:17 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:11:09 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-07-31 02:08:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:08:10 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:08:08 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:07:38 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-07-31 02:07:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:06:49 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.029 |  |
| 2026-07-31 02:06:46 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:05:31 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-31 02:05:26 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:05:18 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-07-31 02:05:11 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 02:04:33 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.005 |  |
| 2026-07-31 02:04:06 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-31 02:03:59 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 02:03:20 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:59 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:53 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:51 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-07-31 02:02:50 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 02:02:47 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:46 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:45 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:40 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:30 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.030 |  |
| 2026-07-31 02:02:08 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-31 02:01:46 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.178 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 02:22:02 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-07-31 02:07:38 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-07-31 02:05:18 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-07-31 02:04:06 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-31 02:02:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-31 02:02:50 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 01:04:23 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 02:05:11 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 02:03:59 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 02:19:10 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-31 02:02:59 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:47 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:03:20 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:05:26 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 23:24:53 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 01:08:11 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:08:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:40 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:53 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:20:29 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:45 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:07:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:11:17 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:08 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:02:46 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-31 01:07:10 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-31 01:02:07 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 02:04:33 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.005 |  |
| 2026-07-31 00:04:28 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:01:03 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-31 02:02:51 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-07-31 02:05:31 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-31 02:11:09 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-07-31 02:06:49 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.029 |  |
| 2026-07-31 02:02:30 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.030 |  |
| 2026-07-30 21:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-07-30 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.060 |  |
| 2026-07-31 02:01:46 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)