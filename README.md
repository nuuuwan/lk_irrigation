# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_07:09:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,639 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 07:09:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.056 |  |
| 2026-03-26 07:07:53 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:07:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:07:34 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:06:48 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-26 07:06:39 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:06:06 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-03-26 07:05:39 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2026-03-26 07:05:27 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:04:10 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-26 07:04:10 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:56 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 07:03:37 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:22 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:21 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:19 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:16 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 07:03:11 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-26 07:03:10 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2026-03-26 07:03:01 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:02:59 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-26 07:02:34 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-03-26 07:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.111 |  |
| 2026-03-26 07:02:12 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | -39.360 |  |
| 2026-03-26 07:01:48 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:01:23 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-03-26 07:01:22 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:01:10 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-03-26 07:00:57 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -39.360 |  |
| 2026-03-26 07:00:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-26 06:52:31 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.014 |  |
| 2026-03-26 06:32:53 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 06:25:57 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 06:16:24 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 07:01:23 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-03-26 07:06:06 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-03-26 06:05:50 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-26 07:06:48 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-26 07:02:59 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-26 07:00:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-26 07:03:56 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 07:03:16 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 07:03:37 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:01:22 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:06:39 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:02:34 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 06:25:57 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 06:05:56 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 06:01:36 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:01 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:19 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:21 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:04:10 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:07:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:03:22 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:05:27 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:01:48 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 06:02:03 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:02:01 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:07:53 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-26 06:16:24 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:07:34 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 07:04:10 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-26 07:03:11 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-26 06:52:31 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.014 |  |
| 2026-03-26 07:01:10 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-03-26 07:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-03-26 07:05:39 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2026-03-26 07:09:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.056 |  |
| 2026-03-26 07:03:10 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2026-03-26 07:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.111 |  |
| 2026-03-26 07:02:12 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | -39.360 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)