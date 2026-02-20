# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_12:02:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,127 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 12:02:48 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:02:47 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-02-20 12:02:24 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-02-20 12:02:08 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:07 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
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
| 2026-02-20 11:28:42 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.079 |  |
| 2026-02-20 11:22:40 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.015 |  |
| 2026-02-20 11:17:03 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-02-20 11:12:19 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:10:48 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:08:18 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:08:18 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:07:32 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.033 |  |
| 2026-02-20 11:06:50 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:06:45 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.071 |  |
| 2026-02-20 11:06:26 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 12:00:30 | Padiyathalawa (Maduru Oya) | 2.63 | 🟢 Normal | 0.669 | 🔺 Rising |
| 2026-02-20 11:17:03 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-02-20 11:02:10 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-20 12:02:48 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 12:01:40 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:04:06 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:54 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:18 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:54 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:29 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:08 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:45 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:01:11 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:07 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:01 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:08 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:06:50 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:57 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:02:02 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:06:26 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 12:00:44 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:54 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:04:05 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.005 |  |
| 2026-02-20 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:01:39 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-20 12:01:46 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-02-20 11:22:40 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.015 |  |
| 2026-02-20 11:03:22 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-02-20 12:02:47 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-02-20 11:05:50 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.029 |  |
| 2026-02-20 12:02:24 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-02-20 12:01:48 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-02-20 11:57:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.071 |  |
| 2026-02-20 11:28:42 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.079 |  |
| 2026-02-20 11:02:50 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.088 |  |
| 2026-02-20 11:02:06 | Weraganthota (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)