# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_06:08:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,914 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 06:01:07 | Moragaswewa (Deduru Oya) | 2.05 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-09 06:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.82 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-09 06:02:34 | Badalgama (Maha Oya) | 4.95 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-09 06:03:37 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-09 06:01:12 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-09 06:03:29 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-09 06:01:26 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 06:02:49 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 06:02:21 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 06:03:05 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 06:05:57 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 06:00:19 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 06:06:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 06:06:25 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-09 06:07:33 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 06:01:54 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-09 06:03:13 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 06:01:43 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-09 06:00:53 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-10-09 06:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2026-10-09 06:04:00 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-09 06:02:22 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-10-09 06:03:49 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-10-09 06:05:39 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.037 |  |
| 2026-10-09 06:01:30 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | -0.043 |  |
| 2026-10-09 06:04:50 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | -0.051 |  |
| 2026-10-09 06:02:10 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.072 |  |
| 2026-10-09 06:04:31 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.073 |  |
| 2026-10-09 06:08:53 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.081 |  |
| 2026-10-09 06:06:52 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | -0.088 |  |
| 2026-10-09 06:01:20 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.090 |  |
| 2026-10-09 06:01:07 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | -0.103 |  |
| 2026-10-09 06:05:50 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.138 |  |
| 2026-10-09 06:03:11 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.159 |  |
| 2026-10-09 06:02:26 | Giriulla (Maha Oya) | 3.92 | 🟢 Normal | -0.211 |  |
| 2026-10-09 06:06:43 | Rathnapura (Kalu Ganga) | 3.34 | 🟢 Normal | -0.223 |  |
| 2026-10-09 06:02:08 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | -0.271 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)