# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_02:02:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,465 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 02:02:50 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-11 02:02:47 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.039 |  |
| 2026-11-11 02:02:45 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -108.000 |  |
| 2026-11-11 02:02:44 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -108.000 |  |
| 2026-11-11 02:02:42 | Glencourse (Kelani Ganga) | 13.18 | 🟢 Normal | -0.010 |  |
| 2026-11-11 02:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | -0.006 |  |
| 2026-11-11 02:02:29 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -126.000 |  |
| 2026-11-11 02:02:27 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -126.000 |  |
| 2026-11-11 02:02:11 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.041 |  |
| 2026-11-11 02:01:48 | Thawalama (Gin Ganga) | 4.21 | 🟡 Alert | -0.246 |  |
| 2026-11-11 02:01:37 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-11 02:01:21 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-11-11 02:01:19 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.070 |  |
| 2026-11-11 02:01:10 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 00:02:18 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-11 00:08:50 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 01:07:33 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 02:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | -0.006 |  |
| 2026-11-11 01:03:02 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | -0.029 |  |
| 2026-11-11 00:05:16 | Magura (Kalu Ganga) | 4.13 | 🟡 Alert | -0.048 |  |
| 2026-11-11 01:02:53 | Rathnapura (Kalu Ganga) | 5.45 | 🟡 Alert | -0.118 |  |
| 2026-11-11 00:01:12 | Peradeniya (Mahaweli Ganga) | 5.31 | 🟡 Alert | -0.196 |  |
| 2026-11-11 02:01:48 | Thawalama (Gin Ganga) | 4.21 | 🟡 Alert | -0.246 |  |
| 2026-11-11 01:03:01 | Giriulla (Maha Oya) | 3.53 | 🟢 Normal | 1.035 | 🔺 Rising |
| 2026-11-11 01:04:26 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-11-11 01:03:13 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-11 01:04:09 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-10 22:02:07 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-11 01:02:45 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 02:01:37 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:22:08 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:12:57 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-11 01:01:09 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-11 02:02:42 | Glencourse (Kelani Ganga) | 13.18 | 🟢 Normal | -0.010 |  |
| 2026-11-11 02:01:21 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-11-11 01:02:39 | Moraketiya (Walawe Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:03:24 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-11 02:02:50 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-11 01:04:53 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-11 01:04:48 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.022 |  |
| 2026-11-11 02:02:47 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.039 |  |
| 2026-11-11 02:02:11 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.041 |  |
| 2026-11-11 01:02:42 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.062 |  |
| 2026-11-11 01:11:18 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.066 |  |
| 2026-11-11 02:01:19 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.070 |  |
| 2026-11-11 01:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.089 |  |
| 2026-11-11 01:01:07 | Pitabeddara (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.114 |  |
| 2026-11-11 01:08:11 | Holombuwa (Kelani Ganga) | 1.80 | 🟢 Normal | -0.277 |  |
| 2026-11-11 02:02:45 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -108.000 |  |
| 2026-11-11 02:02:29 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -126.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)