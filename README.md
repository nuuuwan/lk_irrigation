# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_00:36:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,197 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 00:36:07 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:28:53 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.015 |  |
| 2026-03-28 00:25:54 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.081 |  |
| 2026-03-28 00:17:58 | Rathnapura (Kalu Ganga) | 0.35 | 🟢 Normal | -0.017 |  |
| 2026-03-28 00:11:11 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:10:50 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:09:57 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:09:54 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:09:23 | Norwood (Kelani Ganga) | 0.31 | 🟢 Normal | -0.005 |  |
| 2026-03-28 00:08:36 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:08:12 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:06:22 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:05:53 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 00:04:09 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-03-28 00:03:40 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-28 00:09:54 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:00:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:36:07 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:01:24 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:03:52 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-27 23:00:45 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 18:01:51 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:05:53 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:11:11 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:04:05 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:01:29 | Ellagawa (Kalu Ganga) | 3.69 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:09:57 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:08:12 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 23:05:11 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 23:01:17 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:04:50 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:02:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-27 23:17:24 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:03:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:06:22 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-27 23:05:30 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 18:00:28 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:10:50 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 23:14:59 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:01:56 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:08:36 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:01:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-28 00:09:23 | Norwood (Kelani Ganga) | 0.31 | 🟢 Normal | -0.005 |  |
| 2026-03-28 00:02:39 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-28 00:01:26 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.011 |  |
| 2026-03-28 00:28:53 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.015 |  |
| 2026-03-28 00:17:58 | Rathnapura (Kalu Ganga) | 0.35 | 🟢 Normal | -0.017 |  |
| 2026-03-28 00:04:57 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.028 |  |
| 2026-03-28 00:03:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-03-28 00:03:04 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.069 |  |
| 2026-03-28 00:25:54 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.081 |  |
| 2026-03-27 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)