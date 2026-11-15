# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_16:02:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 16:02:59 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-11-15 16:02:58 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:02:50 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:02:48 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.021 |  |
| 2026-11-15 16:02:16 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-15 16:02:06 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-15 16:02:05 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:01:38 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 16:01:33 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:01:33 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 16:01:29 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:14 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:09 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 16:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:04 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-11-15 16:01:03 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:00:32 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:17:10 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 15:04:02 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 16:02:06 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-15 15:05:29 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-15 15:03:35 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-15 16:01:09 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 15:00:12 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 16:01:33 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 16:01:38 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 16:00:32 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:05:13 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:01:20 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:02:50 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:02:58 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:03:41 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:05:05 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:03:43 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:04:33 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:14 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:07:31 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:29 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:05:36 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:02:05 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:01:33 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-15 15:11:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:01:03 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-15 15:02:41 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | -0.010 |  |
| 2026-11-15 15:08:40 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.011 |  |
| 2026-11-15 15:10:04 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-11-15 15:02:03 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.013 |  |
| 2026-11-15 16:02:16 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-15 16:02:59 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-11-15 15:03:10 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.021 |  |
| 2026-11-15 16:02:48 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.021 |  |
| 2026-11-15 15:02:23 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.022 |  |
| 2026-11-15 16:01:04 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-11-15 15:00:38 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.032 |  |
| 2026-11-15 15:17:10 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.033 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)