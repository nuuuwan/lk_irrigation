# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_22:25:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 22:25:20 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:24:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-29 22:11:01 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:09:48 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-29 22:09:24 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.021 |  |
| 2026-06-29 22:08:35 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.128 |  |
| 2026-06-29 22:07:56 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:07:53 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.193 |  |
| 2026-06-29 22:07:38 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-06-29 22:04:50 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:04:49 | Glencourse (Kelani Ganga) | 12.07 | 🟢 Normal | -0.137 |  |
| 2026-06-29 22:04:16 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-29 22:04:15 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-06-29 22:03:28 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-29 22:03:27 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 22:08:35 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.128 |  |
| 2026-06-29 22:03:28 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-29 22:01:12 | Ellagawa (Kalu Ganga) | 7.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-29 22:04:16 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-29 22:03:27 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 22:03:17 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 22:24:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-29 22:00:58 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 22:02:59 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 22:03:20 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 18:03:53 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:03:18 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:03:20 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:01:56 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:04:05 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:07:56 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:00:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:01:21 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:02:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:11:01 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:25:20 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:04:50 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:01:57 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 22:04:15 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-06-29 22:02:22 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-06-29 22:00:37 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.011 |  |
| 2026-06-29 22:09:48 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-29 22:09:24 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.021 |  |
| 2026-06-29 22:01:14 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.021 |  |
| 2026-06-29 22:07:38 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-06-29 22:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-06-29 21:03:54 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-06-29 22:02:34 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.042 |  |
| 2026-06-29 22:01:05 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.066 |  |
| 2026-06-29 22:02:43 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.070 |  |
| 2026-06-29 22:04:49 | Glencourse (Kelani Ganga) | 12.07 | 🟢 Normal | -0.137 |  |
| 2026-06-29 22:07:53 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)