# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_12:14:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 12:14:09 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.050 |  |
| 2026-02-20 12:12:51 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-02-20 12:09:31 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-20 12:07:57 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.092 |  |
| 2026-02-20 12:05:48 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:05:47 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:05:27 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-20 12:05:20 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:05:16 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.386 |  |
| 2026-02-20 12:05:16 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:05:10 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:51 | Weraganthota (Mahaweli Ganga) | -0.46 | 🟢 Normal | -0.086 |  |
| 2026-02-20 12:04:43 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:41 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-20 12:04:18 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:17 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:16 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.049 |  |
| 2026-02-20 12:03:24 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:03:21 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.031 |  |
| 2026-02-20 12:03:05 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:48 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:02:47 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-02-20 12:02:24 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-02-20 12:02:08 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:07 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.050 |  |
| 2026-02-20 12:02:02 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:54 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:54 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:48 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-02-20 12:01:46 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-02-20 12:01:40 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:39 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:01:18 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:11 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:00:44 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:00:30 | Padiyathalawa (Maduru Oya) | 2.63 | 🟢 Normal | 0.669 | 🔺 Rising |
| 2026-02-20 11:57:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 12:00:30 | Padiyathalawa (Maduru Oya) | 2.63 | 🟢 Normal | 0.669 | 🔺 Rising |
| 2026-02-20 12:05:27 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-20 12:04:41 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-20 12:02:48 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 12:01:40 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:54 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:18 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:05:20 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:18 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:54 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:03:24 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:03:05 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:11 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:43 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:05:16 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:08 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:05:10 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:02 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:04:17 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:00:44 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:05:47 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:09:31 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-20 12:05:48 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:01:39 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:01:46 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-02-20 12:12:51 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-02-20 12:02:47 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-02-20 12:03:21 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.031 |  |
| 2026-02-20 12:02:24 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-02-20 12:01:48 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-02-20 12:04:16 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.049 |  |
| 2026-02-20 12:14:09 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.050 |  |
| 2026-02-20 11:57:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.071 |  |
| 2026-02-20 12:04:51 | Weraganthota (Mahaweli Ganga) | -0.46 | 🟢 Normal | -0.086 |  |
| 2026-02-20 12:07:57 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.092 |  |
| 2026-02-20 12:05:16 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.386 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)