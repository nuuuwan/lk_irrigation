# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_23:07:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,653 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 23:07:40 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 23:07:35 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-08 23:07:12 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-08 23:06:06 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-08 23:05:47 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:04:44 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-10-08 23:04:31 | Holombuwa (Kelani Ganga) | 3.26 | 🟡 Alert | -0.475 |  |
| 2026-10-08 23:04:29 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-08 23:04:22 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:03:43 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-10-08 23:03:21 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-08 23:03:16 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-08 23:03:00 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:02:59 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-10-08 23:02:38 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-10-08 23:02:22 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-08 23:02:18 | Peradeniya (Mahaweli Ganga) | 3.37 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-08 23:02:04 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:02:03 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-08 23:01:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:01:49 | Giriulla (Maha Oya) | 4.20 | 🟢 Normal | 0.519 | 🔺 Rising |
| 2026-10-08 23:01:48 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-08 23:01:31 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-08 23:00:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:40:42 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-08 22:34:35 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 23:04:31 | Holombuwa (Kelani Ganga) | 3.26 | 🟡 Alert | -0.475 |  |
| 2026-10-08 23:01:49 | Giriulla (Maha Oya) | 4.20 | 🟢 Normal | 0.519 | 🔺 Rising |
| 2026-10-08 23:04:44 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-10-08 23:02:38 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-10-08 23:02:03 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-08 23:04:29 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-08 23:03:21 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-08 23:06:06 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-08 23:01:48 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-08 23:03:43 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-10-08 22:03:59 | Thawalama (Gin Ganga) | 3.59 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-08 23:07:12 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-08 23:07:35 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-08 22:18:02 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-08 22:05:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-08 23:02:18 | Peradeniya (Mahaweli Ganga) | 3.37 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-08 23:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-08 23:02:22 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-08 22:40:42 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-08 22:05:58 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-08 21:00:42 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 22:02:26 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 23:07:40 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:02:04 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:01:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:00:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:04:22 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:03:00 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:03:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:05:47 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:01:31 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:04:04 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-08 22:34:35 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.013 |  |
| 2026-10-08 23:02:59 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-10-08 23:03:16 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-08 22:05:50 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)