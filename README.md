# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_09:17:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 09:17:13 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | 0.017 | 🔺 Rising |
| 2026-10-17 09:16:36 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.074 |  |
| 2026-10-17 09:13:25 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.051 |  |
| 2026-10-17 09:10:51 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | -0.009 |  |
| 2026-10-17 09:09:43 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | -0.009 |  |
| 2026-10-17 09:09:00 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-17 09:06:42 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.040 |  |
| 2026-10-17 09:06:37 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-10-17 09:05:53 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.075 |  |
| 2026-10-17 09:05:40 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:05:09 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.039 |  |
| 2026-10-17 09:05:01 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-17 09:04:55 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.118 |  |
| 2026-10-17 09:04:46 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | -0.044 |  |
| 2026-10-17 09:04:10 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.022 |  |
| 2026-10-17 09:04:06 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.79 | 🟡 Alert | -0.010 |  |
| 2026-10-17 09:03:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:02:59 | Hanwella (Kelani Ganga) | 3.75 | 🟢 Normal | -0.041 |  |
| 2026-10-17 09:02:58 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-10-17 09:02:54 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 09:02:50 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.094 |  |
| 2026-10-17 09:02:33 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.050 |  |
| 2026-10-17 09:02:22 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 09:02:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:02:11 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:02:11 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.081 |  |
| 2026-10-17 09:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:02:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:01:45 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-17 09:01:41 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-17 09:01:41 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:01:32 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.070 |  |
| 2026-10-17 09:01:12 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-17 09:01:11 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.071 |  |
| 2026-10-17 09:01:07 | Moraketiya (Walawe Ganga) | 1.46 | 🟢 Normal | -0.034 |  |
| 2026-10-17 09:00:52 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:00:51 | Thanthirimale (Malwathu Oya) | 2.47 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-17 09:00:22 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 09:17:13 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | 0.017 | 🔺 Rising |
| 2026-10-17 09:00:22 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 09:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.79 | 🟡 Alert | -0.010 |  |
| 2026-10-17 09:01:41 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-17 09:01:12 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-17 09:00:51 | Thanthirimale (Malwathu Oya) | 2.47 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-17 09:09:00 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-17 09:02:22 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 09:02:54 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 09:02:11 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:02:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:02:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:01:41 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:00:52 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 09:09:43 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | -0.009 |  |
| 2026-10-17 09:10:51 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | -0.009 |  |
| 2026-10-17 09:05:01 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-17 09:01:45 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-17 09:02:58 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-10-17 09:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:04:06 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:03:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:05:40 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:04:10 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.022 |  |
| 2026-10-17 09:01:07 | Moraketiya (Walawe Ganga) | 1.46 | 🟢 Normal | -0.034 |  |
| 2026-10-17 09:05:09 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.039 |  |
| 2026-10-17 09:06:42 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.040 |  |
| 2026-10-17 09:02:59 | Hanwella (Kelani Ganga) | 3.75 | 🟢 Normal | -0.041 |  |
| 2026-10-17 09:04:46 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | -0.044 |  |
| 2026-10-17 09:02:33 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.050 |  |
| 2026-10-17 09:13:25 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.051 |  |
| 2026-10-17 09:06:37 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-10-17 09:01:32 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.070 |  |
| 2026-10-17 09:01:11 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.071 |  |
| 2026-10-17 09:16:36 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.074 |  |
| 2026-10-17 09:05:53 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.075 |  |
| 2026-10-17 09:02:11 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.081 |  |
| 2026-10-17 09:02:50 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.094 |  |
| 2026-10-17 09:04:55 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)