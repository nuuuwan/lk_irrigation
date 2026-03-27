# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_21:01:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,061 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 21:01:20 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-27 21:01:17 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:59:36 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-27 20:35:48 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-27 20:25:50 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:17:50 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:17:00 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:11:38 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:09:44 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-27 20:09:17 | Ellagawa (Kalu Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:08:21 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:07:43 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 20:59:36 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-27 20:01:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-27 20:09:44 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-27 20:05:10 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-27 20:35:48 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-27 21:01:20 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:07:05 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:01:51 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:07:10 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-27 21:01:17 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:05:32 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:03:55 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 18:01:51 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:11:38 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:01:37 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:17:50 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:03:18 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:09:17 | Ellagawa (Kalu Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:08:21 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:25:50 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:04:21 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:02:50 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:01:47 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:03:09 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:04:10 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:03:05 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:07:43 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:04:38 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-27 18:00:28 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:17:00 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:01:25 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 20:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-03-27 20:01:59 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-03-27 20:04:08 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.010 |  |
| 2026-03-27 20:03:45 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-03-27 20:01:42 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-27 20:04:58 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-03-27 20:04:09 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-03-27 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)