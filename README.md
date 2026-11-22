# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_19:02:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,942 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 19:02:58 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:02:46 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-11-22 19:02:43 | Moragaswewa (Deduru Oya) | 3.31 | 🟢 Normal | -0.241 |  |
| 2026-11-22 19:02:21 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:02:19 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.051 |  |
| 2026-11-22 19:02:03 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.040 |  |
| 2026-11-22 19:01:57 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:01:57 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:01:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:01:10 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:00:49 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:00:11 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 19:00:07 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-11-22 19:00:07 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -3.303 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 18:06:35 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-11-22 18:06:59 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-11-22 18:04:21 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-22 18:01:41 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 19:00:11 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 18:03:19 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 18:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:01:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:01:57 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:02:21 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:11:06 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:01:07 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:50 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:53 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:05:47 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:03:22 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:01:10 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:13:10 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-11-22 18:03:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:01:57 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:00:49 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:02:58 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:00:07 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-22 19:02:46 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-11-22 18:02:44 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.031 |  |
| 2026-11-22 18:04:07 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-11-22 19:02:03 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.040 |  |
| 2026-11-22 18:05:20 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.041 |  |
| 2026-11-22 18:02:10 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.043 |  |
| 2026-11-22 18:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-11-22 18:01:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-11-22 19:02:19 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.051 |  |
| 2026-11-22 18:01:57 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.148 |  |
| 2026-11-22 19:02:43 | Moragaswewa (Deduru Oya) | 3.31 | 🟢 Normal | -0.241 |  |
| 2026-11-22 19:00:07 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -3.303 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)