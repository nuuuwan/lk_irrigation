# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_15:19:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,553 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 15:19:12 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:10:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:10:50 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:08:51 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:07:38 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-09 15:05:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-09 15:05:54 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.105 |  |
| 2026-03-09 15:05:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-09 15:04:54 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 15:02:39 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-03-09 15:03:33 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-09 15:05:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-09 15:07:38 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-09 15:03:23 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-09 15:05:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-09 15:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 15:01:13 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:01:42 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:00:25 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:01:54 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:10:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:03:16 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:10:50 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:03:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:19:12 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:02:34 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:08:51 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:00:09 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:04:35 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:02:31 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:01:27 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:02:00 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:03:51 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:02:34 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:03:23 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:00:52 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:04:17 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:02:46 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:03:06 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:04:54 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-09 15:03:28 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-09 15:01:32 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-09 15:03:15 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-03-09 15:01:47 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | -0.020 |  |
| 2026-03-09 15:01:47 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.051 |  |
| 2026-03-09 15:02:46 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.060 |  |
| 2026-03-09 15:05:54 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)