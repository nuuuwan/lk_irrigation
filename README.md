# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_16:14:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,441 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 16:14:18 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-30 16:13:17 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:12:47 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:12:25 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:12:21 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:07:09 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-30 16:06:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:06:41 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.028 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 16:14:18 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-30 16:06:41 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-30 16:05:05 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-30 16:02:11 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-30 16:04:22 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 16:05:03 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-30 15:00:33 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:04:01 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:02:43 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:01:03 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:04:00 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:04:28 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:04:44 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:06:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:12:47 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:12:21 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:03:43 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:04:21 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:04:14 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:13:17 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:04:51 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:05:44 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:01:19 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:00:50 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:12:25 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:01:59 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:01:11 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 16:01:32 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -0.005 |  |
| 2026-07-30 16:06:24 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-07-30 16:04:20 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-30 16:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-07-30 16:03:07 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-07-30 16:04:03 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-07-30 16:07:09 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-30 16:01:32 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-07-30 16:03:18 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.020 |  |
| 2026-07-30 16:01:19 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2026-07-30 16:02:26 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.063 |  |
| 2026-07-30 16:00:38 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)