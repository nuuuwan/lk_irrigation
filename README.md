# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_14:08:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,328 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 14:08:19 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-10-18 14:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | -0.161 |  |
| 2026-10-18 14:06:55 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.046 |  |
| 2026-10-18 14:05:33 | Putupaula (Kalu Ganga) | 1.89 | 🟢 Normal | -0.011 |  |
| 2026-10-18 14:05:10 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.013 |  |
| 2026-10-18 14:04:43 | Ellagawa (Kalu Ganga) | 7.73 | 🟢 Normal | -0.020 |  |
| 2026-10-18 14:04:36 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:04:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.092 |  |
| 2026-10-18 14:04:24 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:04:14 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-18 14:04:02 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.059 |  |
| 2026-10-18 14:04:00 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.099 |  |
| 2026-10-18 14:03:42 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:03:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-18 14:03:25 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.049 |  |
| 2026-10-18 14:03:22 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.060 |  |
| 2026-10-18 14:03:22 | Moragaswewa (Deduru Oya) | 1.88 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-10-18 14:03:14 | Hanwella (Kelani Ganga) | 3.68 | 🟢 Normal | -0.090 |  |
| 2026-10-18 14:03:14 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.141 |  |
| 2026-10-18 14:03:07 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:02:34 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-18 14:02:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 14:02:12 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-18 14:02:10 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-10-18 14:02:10 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:02:04 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 14:01:53 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.044 |  |
| 2026-10-18 14:01:32 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 14:01:31 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:00:45 | Horowpothana (Yan Oya) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-10-18 14:00:32 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.022 |  |
| 2026-10-18 14:00:31 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-10-18 14:00:16 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.136 |  |
| 2026-10-18 13:59:26 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:23:16 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:22:09 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 13:13:51 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 13:03:23 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.045 |  |
| 2026-10-18 14:03:22 | Moragaswewa (Deduru Oya) | 1.88 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-10-18 14:01:32 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 14:02:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 14:02:04 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 13:02:31 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-18 14:01:31 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:04:24 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:02:10 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:03:42 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:04:36 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:03:07 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:08:19 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-10-18 13:11:38 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-10-18 14:04:14 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-18 14:02:12 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-18 14:02:34 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-18 14:00:31 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-10-18 14:05:33 | Putupaula (Kalu Ganga) | 1.89 | 🟢 Normal | -0.011 |  |
| 2026-10-18 14:05:10 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.013 |  |
| 2026-10-18 14:04:43 | Ellagawa (Kalu Ganga) | 7.73 | 🟢 Normal | -0.020 |  |
| 2026-10-18 14:03:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-18 14:00:45 | Horowpothana (Yan Oya) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-10-18 13:05:22 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-10-18 14:00:32 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.022 |  |
| 2026-10-18 14:02:10 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-10-18 13:00:44 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.041 |  |
| 2026-10-18 14:01:53 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.044 |  |
| 2026-10-18 14:06:55 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.046 |  |
| 2026-10-18 14:03:25 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.049 |  |
| 2026-10-18 14:04:02 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.059 |  |
| 2026-10-18 14:03:22 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.060 |  |
| 2026-10-18 14:03:14 | Hanwella (Kelani Ganga) | 3.68 | 🟢 Normal | -0.090 |  |
| 2026-10-18 14:04:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.092 |  |
| 2026-10-18 14:04:00 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.099 |  |
| 2026-10-18 14:00:16 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.136 |  |
| 2026-10-18 14:03:14 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.141 |  |
| 2026-10-18 14:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)