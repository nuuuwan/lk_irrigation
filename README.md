# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_11:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 11:03:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-01 11:03:18 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:02:51 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.052 |  |
| 2026-11-01 11:02:35 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-01 11:02:30 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:25 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:17 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:10 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.061 |  |
| 2026-11-01 11:02:08 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.031 |  |
| 2026-11-01 11:02:08 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.221 |  |
| 2026-11-01 11:02:07 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:01:56 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.052 |  |
| 2026-11-01 11:01:54 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-11-01 11:01:31 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:01:25 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 11:01:20 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:01:05 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:00:10 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 10:39:52 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-11-01 10:37:42 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.025 |  |
| 2026-11-01 10:32:24 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 11:01:25 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 11:03:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-01 10:05:24 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-01 11:02:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-01 10:06:26 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 10:04:48 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 10:02:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:00:10 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:25 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:30 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:01:05 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 10:32:24 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:07 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:17 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:01:31 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 10:12:26 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:35 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:38 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-01 10:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:03:18 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:01:20 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 10:00:42 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-01 10:05:39 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-11-01 10:02:06 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-11-01 10:02:07 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-11-01 11:01:54 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-11-01 10:03:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-11-01 11:02:08 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.031 |  |
| 2026-11-01 10:01:21 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.031 |  |
| 2026-11-01 10:02:28 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.047 |  |
| 2026-11-01 10:04:23 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-11-01 11:01:56 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.052 |  |
| 2026-11-01 11:02:51 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.052 |  |
| 2026-11-01 11:02:10 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.061 |  |
| 2026-11-01 10:04:51 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.071 |  |
| 2026-11-01 10:01:29 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.072 |  |
| 2026-11-01 10:05:43 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.095 |  |
| 2026-11-01 11:02:08 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)