# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_02:38:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,667 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 02:38:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:28:11 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:25:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:13:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 9.144 | 🔺 Rising |
| 2026-03-24 02:12:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 9.144 | 🔺 Rising |
| 2026-03-24 02:08:32 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:08:24 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-24 02:08:02 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-03-24 02:07:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:07:06 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:05:22 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:05:21 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:04:54 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-24 02:04:48 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:04:45 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:03:51 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-03-24 02:03:04 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:03:00 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:02:44 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:02:37 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:02:36 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:02:35 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-03-24 02:02:25 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:02:07 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:01:38 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:01:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-24 02:01:14 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:01:06 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.014 |  |
| 2026-03-24 02:01:02 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.160 |  |
| 2026-03-24 02:00:44 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 02:13:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 9.144 | 🔺 Rising |
| 2026-03-24 02:08:24 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-24 02:04:54 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-24 02:01:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-24 02:38:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:00:44 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:02:07 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-23 21:01:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:02:25 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:01:38 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:03:00 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:05:21 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:05:22 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:08:32 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:03:04 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:02:36 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-24 01:03:25 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:02:37 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:04:45 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:28:11 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:25:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:07:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 01:06:43 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.005 |  |
| 2026-03-24 02:07:06 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:02:44 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:04:48 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-24 01:00:54 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:17 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:01:14 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-03-24 01:02:11 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:01:06 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.014 |  |
| 2026-03-24 02:08:02 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-03-24 02:02:35 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-03-23 21:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-03-24 02:03:51 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-03-23 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.101 |  |
| 2026-03-24 02:01:02 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)