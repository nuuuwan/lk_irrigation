# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19_10:20:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **210,364 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 10:20:42 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:16:53 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.103 |  |
| 2026-07-19 10:10:21 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -1.200 |  |
| 2026-07-19 10:09:51 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -1.200 |  |
| 2026-07-19 10:09:50 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -1.200 |  |
| 2026-07-19 10:08:46 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 10:08:43 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:08:01 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:07:18 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-07-19 10:07:01 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:07:01 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-19 10:06:48 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:05:27 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:05:11 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:04:57 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:04:56 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-19 10:04:45 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.120 |  |
| 2026-07-19 10:04:43 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:04:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-07-19 10:04:06 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.063 |  |
| 2026-07-19 10:03:50 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 10:03:45 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:03:28 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:03:15 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-19 10:03:11 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 10:03:06 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:03:03 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:02:51 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:02:34 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-07-19 10:02:12 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:02:03 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:47 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:45 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:30 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:23 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:21 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-19 10:01:18 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.023 |  |
| 2026-07-19 10:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 10:07:01 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-19 10:01:21 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-19 10:04:56 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-19 10:03:11 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 10:03:50 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 10:08:46 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 10:04:43 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:20:42 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:45 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:02:51 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:23 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:02:12 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:08:43 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-19 09:03:05 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:04:06 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:05:11 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:07:01 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:08:01 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:03:06 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:06:48 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:02:03 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:03:28 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:03:45 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:30 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:04:57 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:05:27 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:03:03 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 09:02:29 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:01:47 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-19 10:04:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-07-19 10:07:18 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-07-19 10:03:15 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-19 10:02:34 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-07-19 10:01:18 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.023 |  |
| 2026-07-19 10:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.063 |  |
| 2026-07-19 10:16:53 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.103 |  |
| 2026-07-19 10:04:45 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.120 |  |
| 2026-07-19 10:10:21 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -1.200 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)