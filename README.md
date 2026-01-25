# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_12:36:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,238 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 12:36:47 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:13:17 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-25 12:12:53 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:12:13 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.015 |  |
| 2026-01-25 12:09:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:08:25 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:07:21 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:07:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:06:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-01-25 12:06:16 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.058 |  |
| 2026-01-25 12:06:12 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:05:47 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:05:29 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:05:02 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:04:32 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:04:30 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.073 |  |
| 2026-01-25 12:04:12 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:04:01 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:03:55 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.062 |  |
| 2026-01-25 12:03:53 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-25 12:03:34 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 12:03:32 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:03:30 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:03:18 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.038 |  |
| 2026-01-25 12:02:52 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:02:45 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-01-25 12:02:39 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:02:20 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:02:20 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-25 12:02:08 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 12:01:54 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-01-25 12:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:01:37 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:00:58 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:00:51 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:00:35 | Yaka Wewa (Ma Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-01-25 12:00:29 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.111 |  |
| 2026-01-25 12:00:20 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 12:03:34 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 12:02:08 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 12:13:17 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-25 12:00:51 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:01:37 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:06:12 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:03:30 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:04:01 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:09:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:08:25 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:05:47 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:02:39 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:05:29 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:07:21 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:04:32 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:00:58 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:03:32 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:12:53 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:00:20 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:02:52 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:02:20 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:02:20 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:36:47 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:05:02 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:04:12 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:03:53 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:02:00 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.010 |  |
| 2026-01-25 12:12:13 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.015 |  |
| 2026-01-25 12:00:35 | Yaka Wewa (Ma Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-01-25 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-25 12:01:54 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-01-25 12:02:45 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-01-25 12:06:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-01-25 12:03:18 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.038 |  |
| 2026-01-25 12:06:16 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.058 |  |
| 2026-01-25 12:03:55 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.062 |  |
| 2026-01-25 12:04:30 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.073 |  |
| 2026-01-25 12:00:29 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)