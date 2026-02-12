# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_15:03:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 15:03:42 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:03:25 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:03:22 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:02:49 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:02:43 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-02-12 15:02:29 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:02:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-12 15:02:04 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.040 |  |
| 2026-02-12 15:02:01 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:01:40 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:01:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.126 |  |
| 2026-02-12 15:01:33 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:01:31 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 15:01:09 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:00:55 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 15:00:45 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-02-12 15:00:32 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:00:06 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:54:01 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-02-12 14:23:46 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:22:17 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:15:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:12:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-12 14:11:44 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:11:28 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:11:11 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:10:00 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:09:58 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:09:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-02-12 14:09:00 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 14:04:45 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-12 14:06:02 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-12 15:00:55 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-12 15:01:31 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 14:01:30 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 15:02:01 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:00:06 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:03:25 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:01:40 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:03:42 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:01:01 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:11:11 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:10:00 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:02:58 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:02:49 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:03:08 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:04:19 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:01:09 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:11:44 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:01:33 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:02:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:06:53 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:23:46 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:04:42 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:00:32 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:03:22 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:15:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 15:02:29 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:22:17 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-12 14:09:00 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-02-12 14:03:59 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-12 15:02:43 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-02-12 14:02:02 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-02-12 14:54:01 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-02-12 15:00:45 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-02-12 15:02:04 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.040 |  |
| 2026-02-12 15:01:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)