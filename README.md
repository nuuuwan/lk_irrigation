# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_01:09:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **214,499 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 01:09:15 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:06:43 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-24 01:06:06 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-24 01:05:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:04:35 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:04:05 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.059 |  |
| 2026-07-24 01:04:03 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:02:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:02:24 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:02:20 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:02:09 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-07-24 01:02:00 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:01:33 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:01:17 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:01:14 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:01:09 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:00:55 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:00:45 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:00:21 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-07-24 01:00:14 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:32:19 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 01:06:43 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-24 00:32:19 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-24 01:02:24 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:01:09 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:01:33 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:02:00 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:05:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:01:14 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:00:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:06:16 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:04:37 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:01:17 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:02:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:00:14 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:03:37 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-23 21:02:38 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:09:15 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:02:20 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:04:35 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:00:55 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:04:53 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:01:54 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:02:28 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:04:03 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:00:45 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:01:46 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-23 20:53:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:18:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.004 |  |
| 2026-07-24 00:04:24 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.005 |  |
| 2026-07-24 00:08:30 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-07-24 01:06:06 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-24 01:00:21 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-07-24 00:04:14 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-07-24 01:02:09 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-07-24 01:04:05 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.059 |  |
| 2026-07-24 00:01:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.061 |  |
| 2026-07-23 18:06:44 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)