# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_19:26:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,590 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 19:26:12 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:15:32 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:13:39 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:12:11 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-31 19:12:02 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:09:46 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-31 19:09:16 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-31 19:08:27 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:07:20 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:06:09 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-31 19:05:38 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:05:30 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 19:02:31 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-03-31 19:09:46 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-31 19:09:16 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-31 19:12:11 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-31 19:04:04 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-31 19:02:08 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 19:02:07 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:02:21 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:05:08 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:04:22 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:26:12 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:03:56 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:02:14 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:04:31 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:08:27 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:15:32 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:02:27 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:07:20 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:12:02 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:00:31 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:05:38 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:02:22 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:02:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:03:07 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:02:26 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:01:51 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:13:39 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:03:45 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:04:01 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:01:25 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 19:05:30 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:49 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-03-31 19:06:09 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-31 19:01:20 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-03-31 19:04:22 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-03-31 18:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-03-31 19:03:57 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.047 |  |
| 2026-03-31 19:00:28 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-03-31 18:01:04 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)