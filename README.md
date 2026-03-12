# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_23:47:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,739 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 23:47:34 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:32:27 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:29:22 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:17:49 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-12 23:17:42 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-03-12 23:10:31 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:05:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.072 |  |
| 2026-03-12 23:04:56 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-03-12 23:04:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:04:12 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-12 23:04:07 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:03:38 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-03-12 23:03:20 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:03:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-03-12 23:02:44 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.434 | 🔺 Rising |
| 2026-03-12 23:02:32 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:27 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:13 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:12 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-03-12 23:02:10 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:10 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 23:02:44 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.434 | 🔺 Rising |
| 2026-03-12 22:16:26 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-12 23:17:49 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-12 23:04:12 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-12 23:01:24 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-12 22:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 22:05:28 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 23:01:56 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 23:00:13 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:01:28 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:47:34 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:01:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:03:20 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:01:36 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:04:07 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:03:22 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:01:54 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:12:15 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:32:27 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:04:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:05:24 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:04 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:29:22 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:27 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:10 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:32 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:10:31 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:13 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:02:10 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-12 23:03:38 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-03-12 23:00:23 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.023 |  |
| 2026-03-12 23:04:56 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-03-12 23:03:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-03-12 23:17:42 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-03-12 23:02:12 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-03-12 23:05:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.072 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)