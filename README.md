# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_19:19:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,595 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 19:19:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-07-11 19:18:04 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:13:39 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.008 |  |
| 2026-07-11 19:11:42 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:10:59 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:10:55 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:10:12 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:09:15 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-07-11 19:08:55 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-11 19:08:53 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.018 |  |
| 2026-07-11 19:08:40 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-07-11 19:07:10 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-07-11 19:06:53 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:05:56 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:05:43 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | -0.105 |  |
| 2026-07-11 19:05:15 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:04:10 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 19:02:27 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-07-11 19:02:32 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 17:01:05 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 19:02:23 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 19:04:10 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 19:02:33 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:01:55 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:06:53 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:01:59 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:03:08 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:03:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:28 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:10:59 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:02:35 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:11:42 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:03:13 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:01:37 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:05:15 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:00:15 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:03:00 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:02:12 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:00:48 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:18:04 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:10:12 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:01:59 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:05:56 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-11 19:13:39 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.008 |  |
| 2026-07-11 19:08:40 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-07-11 19:07:10 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-07-11 19:09:15 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-07-11 19:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-07-11 19:08:55 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-11 19:08:53 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.018 |  |
| 2026-07-11 19:19:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-07-11 19:03:24 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.049 |  |
| 2026-07-11 19:03:26 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.100 |  |
| 2026-07-11 19:05:43 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)