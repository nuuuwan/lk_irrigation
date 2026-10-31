# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_01:03:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,432 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 01:03:02 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.061 |  |
| 2026-11-01 01:03:00 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.041 |  |
| 2026-11-01 01:02:58 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:48 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:39 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-11-01 01:02:37 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:27 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:01:44 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-11-01 01:01:15 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-01 01:00:50 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:00:23 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 01:01:15 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-01 00:05:14 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-01 00:06:35 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 00:13:13 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-01 01:00:23 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:37 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:48 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:03:45 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:05:33 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:02:09 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:10:44 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:00:07 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:00:50 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:04:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:58 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:04:01 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:11:07 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-11-01 01:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:27 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:03:06 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:02:41 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:02:39 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-01 00:03:09 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.021 |  |
| 2026-11-01 01:01:44 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-11-01 00:04:47 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.022 |  |
| 2026-11-01 00:03:48 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-11-01 00:12:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.034 |  |
| 2026-11-01 00:15:07 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | -0.035 |  |
| 2026-11-01 01:03:00 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.041 |  |
| 2026-11-01 00:04:09 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | -0.041 |  |
| 2026-11-01 01:02:39 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-11-01 01:03:02 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.061 |  |
| 2026-11-01 00:08:20 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.066 |  |
| 2026-11-01 00:11:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)