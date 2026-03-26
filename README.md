# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_08:06:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 08:06:03 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.045 |  |
| 2026-03-26 08:05:57 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.030 |  |
| 2026-03-26 08:04:57 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:04:56 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-03-26 08:04:44 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:04:40 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-26 08:04:23 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-26 08:04:11 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:04:04 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.259 |  |
| 2026-03-26 08:03:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-26 08:03:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:39 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:38 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:34 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-26 08:03:31 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:16 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:03 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:02:42 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-03-26 08:02:30 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 08:01:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:44 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:39 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:38 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2026-03-26 08:01:32 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:14 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:03 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-26 07:39:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.045 |  |
| 2026-03-26 07:31:57 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-26 07:23:53 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.007 |  |
| 2026-03-26 07:23:27 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:15:39 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:12:52 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 08:01:03 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-26 08:03:34 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-26 08:04:23 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-26 08:02:30 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 08:04:40 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-26 08:02:42 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:32 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:31 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:39 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:04:44 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:03 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:15:39 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:16 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:38 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:19 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:04:10 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:14 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:03:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:04:11 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:01:48 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:44 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:04:04 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:04:57 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 08:01:39 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:23:53 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.007 |  |
| 2026-03-26 08:03:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-26 08:04:56 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-03-26 07:12:52 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.029 |  |
| 2026-03-26 08:05:57 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.030 |  |
| 2026-03-26 08:01:38 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2026-03-26 08:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-03-26 08:06:03 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.045 |  |
| 2026-03-26 07:05:39 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2026-03-26 07:09:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.056 |  |
| 2026-03-26 08:03:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.259 |  |
| 2026-03-26 07:02:12 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | -39.360 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)