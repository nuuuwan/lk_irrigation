# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_15:03:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 15:03:32 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:25 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:24 | Dunamale (Aththanagalu Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:21 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-25 15:03:09 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:29 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-02-25 15:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-25 15:02:16 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:13 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:06 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:06 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-02-25 15:02:05 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:50 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:40 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:35 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:31 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | -0.020 |  |
| 2026-02-25 15:01:19 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:16 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:03 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:01 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-25 15:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:00:30 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-25 14:43:29 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.012 |  |
| 2026-02-25 14:14:03 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:13:20 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:11:07 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-25 14:09:00 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:08:58 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 14:06:09 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-25 14:01:51 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-25 15:00:30 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-25 14:03:09 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-25 15:01:16 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:16 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:19 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:06 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:50 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:35 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:07:01 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:09 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:13 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:32 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:25 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:04:31 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:24 | Dunamale (Aththanagalu Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:03 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:40 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:05:38 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:03:26 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:05 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:05:45 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:05:49 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:00:59 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:08:58 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-02-25 15:02:29 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-02-25 15:03:21 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-25 14:03:42 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-25 14:43:29 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.012 |  |
| 2026-02-25 14:11:07 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-25 15:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-25 15:01:31 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | -0.020 |  |
| 2026-02-25 15:01:01 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-25 14:05:06 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.021 |  |
| 2026-02-25 15:02:06 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-02-25 14:02:24 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)