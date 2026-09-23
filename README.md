# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_06:15:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,505 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 06:15:56 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-09-23 06:14:02 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.053 |  |
| 2026-09-23 06:10:40 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.085 |  |
| 2026-09-23 06:09:23 | Baddegama (Gin Ganga) | 3.92 | 🟡 Alert | 0.000 |  |
| 2026-09-23 06:07:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-09-23 06:07:09 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.021 |  |
| 2026-09-23 06:07:01 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:06:53 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-23 06:06:52 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.058 |  |
| 2026-09-23 06:06:33 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -7.579 |  |
| 2026-09-23 06:06:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:05:55 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -7.579 |  |
| 2026-09-23 06:05:22 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.044 |  |
| 2026-09-23 06:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.032 |  |
| 2026-09-23 06:04:29 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-23 06:04:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:03:56 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:03:06 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.034 |  |
| 2026-09-23 06:03:05 | Deraniyagala (Kelani Ganga) | 2.31 | 🟢 Normal | 14.625 | 🔺 Rising |
| 2026-09-23 06:02:41 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.055 |  |
| 2026-09-23 06:02:41 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-09-23 06:02:38 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-23 06:02:33 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | 14.625 | 🔺 Rising |
| 2026-09-23 06:02:17 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:02:15 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:02:05 | Magura (Kalu Ganga) | 4.11 | 🟡 Alert | -0.039 |  |
| 2026-09-23 06:02:02 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | -0.059 |  |
| 2026-09-23 06:01:52 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-23 06:01:41 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.055 |  |
| 2026-09-23 06:01:36 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-09-23 06:01:33 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -36.000 |  |
| 2026-09-23 06:01:32 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -36.000 |  |
| 2026-09-23 06:01:31 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -36.000 |  |
| 2026-09-23 06:01:20 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 06:01:18 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:01:17 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-09-23 06:01:12 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-09-23 06:00:39 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:00:37 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-23 06:00:31 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-09-23 06:00:13 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.007 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 06:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.032 |  |
| 2026-09-23 06:09:23 | Baddegama (Gin Ganga) | 3.92 | 🟡 Alert | 0.000 |  |
| 2026-09-23 06:00:37 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-23 06:02:05 | Magura (Kalu Ganga) | 4.11 | 🟡 Alert | -0.039 |  |
| 2026-09-23 06:03:05 | Deraniyagala (Kelani Ganga) | 2.31 | 🟢 Normal | 14.625 | 🔺 Rising |
| 2026-09-23 06:15:56 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-09-23 06:06:53 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-23 06:02:38 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-23 06:01:20 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 06:00:13 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-09-23 06:04:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:00:39 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:02:15 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:06:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:07:01 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:03:56 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:01:18 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:02:17 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 06:07:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-09-23 06:01:52 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-23 06:04:29 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-23 06:01:17 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-09-23 06:00:31 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-09-23 06:01:36 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-09-23 06:02:41 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-09-23 06:01:12 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-09-23 06:07:09 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.021 |  |
| 2026-09-23 06:03:06 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.034 |  |
| 2026-09-23 06:05:22 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.044 |  |
| 2026-09-23 06:14:02 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.053 |  |
| 2026-09-23 06:02:41 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.055 |  |
| 2026-09-23 06:01:41 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.055 |  |
| 2026-09-23 06:06:52 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.058 |  |
| 2026-09-23 06:02:02 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | -0.059 |  |
| 2026-09-23 06:10:40 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.085 |  |
| 2026-09-23 06:06:33 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -7.579 |  |
| 2026-09-23 06:01:33 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)