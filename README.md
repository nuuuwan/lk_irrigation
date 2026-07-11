# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_11:23:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 11:23:45 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:12:10 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:11:03 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-11 11:10:25 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.009 |  |
| 2026-07-11 11:09:18 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:09:04 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:08:29 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:08:28 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-07-11 11:08:27 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:08:27 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-07-11 11:08:08 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 11:07:41 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:07:39 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:05:27 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:04:44 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:04:14 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:04:12 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:03:53 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:03:47 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-07-11 11:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:03:23 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:03:19 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.019 |  |
| 2026-07-11 11:03:19 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:03:08 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:03:08 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.051 |  |
| 2026-07-11 11:02:47 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.372 |  |
| 2026-07-11 11:02:46 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-11 11:02:39 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-07-11 11:02:35 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:02:29 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.020 |  |
| 2026-07-11 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 11:02:08 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:02:02 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:02:01 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:01:55 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-07-11 11:01:33 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:27 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:21 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:20 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:09 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:08 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:00:21 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 11:01:55 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-07-11 11:11:03 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-11 11:02:46 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-11 11:08:08 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 11:02:35 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:20 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:23:45 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:02:02 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:07:41 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:03:08 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:04:14 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:03:23 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:12:10 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:08 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:08:27 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:21 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:09 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:04:44 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:09:04 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:02:08 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:01:27 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:07:39 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:09:18 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:00:21 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:03:19 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 11:10:25 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.009 |  |
| 2026-07-11 11:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:02:01 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:03:53 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:05:27 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-07-11 11:03:47 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-07-11 11:03:19 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.019 |  |
| 2026-07-11 11:08:28 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-07-11 11:08:27 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-07-11 11:02:39 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-07-11 11:02:29 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.020 |  |
| 2026-07-11 11:03:08 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.051 |  |
| 2026-07-11 11:02:47 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.372 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)