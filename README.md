# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_17:06:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,397 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 17:06:34 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:05:42 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.117 |  |
| 2026-07-12 17:05:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:05:09 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-07-12 17:05:08 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:04:44 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-12 17:04:39 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:04:36 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:04:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.034 |  |
| 2026-07-12 17:04:22 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-07-12 17:03:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:30 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.138 |  |
| 2026-07-12 17:03:24 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:18 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:14 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:07 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:02:45 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2026-07-12 17:02:29 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.031 |  |
| 2026-07-12 17:02:16 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:02:13 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:02:09 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-12 17:01:47 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:33 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:31 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:17 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 17:01:15 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:15 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:05 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 17:00:58 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-12 17:00:50 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:00:42 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:00:38 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:46:59 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.034 |  |
| 2026-07-12 16:36:42 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:22:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 17:00:58 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-12 17:02:09 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-12 16:22:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-12 17:04:44 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-12 17:01:17 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 17:01:05 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 17:01:31 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:24 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:47 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:04:36 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:05:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:17:14 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:14 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:18 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:33 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:15 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:03:07 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:06:34 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:00:38 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:04:39 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:05:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:00:42 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:00:50 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:05:13 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:05:08 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:02:13 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:02:16 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 17:01:15 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:07:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-12 17:05:09 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-07-12 17:04:22 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-07-12 17:02:45 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2026-07-12 16:04:23 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-07-12 17:02:29 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.031 |  |
| 2026-07-12 17:04:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.034 |  |
| 2026-07-12 17:05:42 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.117 |  |
| 2026-07-12 17:03:30 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)