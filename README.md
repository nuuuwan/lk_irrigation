# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_11:07:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,600 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 11:07:30 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:07:25 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:07:17 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-03-28 11:06:11 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:04:40 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.058 |  |
| 2026-03-28 11:04:00 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:03:53 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:03:50 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:03:24 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-28 11:03:11 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-03-28 11:03:00 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-03-28 11:02:35 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:32 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:24 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:20 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:16 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:14 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-28 11:02:08 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:58 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:55 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:43 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:39 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:20 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.051 |  |
| 2026-03-28 11:01:13 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.023 |  |
| 2026-03-28 11:01:11 | Pitabeddara (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-28 11:01:10 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:07 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.109 |  |
| 2026-03-28 11:01:06 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:00:47 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | -0.024 |  |
| 2026-03-28 11:00:41 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:00:37 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-28 10:18:22 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-28 10:18:10 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-28 10:16:38 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 11:07:17 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-03-28 11:03:11 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-03-28 11:03:24 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-28 11:02:14 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-28 11:00:37 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-28 11:01:39 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:43 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:16 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 10:02:56 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:06 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:03:00 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 10:04:55 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:04:00 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:03:50 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:10 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:32 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:55 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:58 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:24 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:06:11 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-28 10:03:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:03:53 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:35 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:07:30 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:20 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:00:41 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 10:04:17 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:07:25 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-28 10:02:47 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:02:08 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 11:01:11 | Pitabeddara (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-28 11:01:13 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.023 |  |
| 2026-03-28 11:00:47 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | -0.024 |  |
| 2026-03-28 11:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-03-28 11:01:20 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.051 |  |
| 2026-03-28 11:04:40 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.058 |  |
| 2026-03-28 11:01:07 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)