# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_08:14:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 08:14:31 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-11-11 08:12:50 | Magura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.200 |  |
| 2026-11-11 08:12:34 | Moragaswewa (Deduru Oya) | 2.60 | 🟢 Normal | -0.022 |  |
| 2026-11-11 08:11:14 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-11-11 08:10:55 | Badalgama (Maha Oya) | 4.41 | 🟢 Normal | -0.085 |  |
| 2026-11-11 08:10:45 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.215 |  |
| 2026-11-11 08:08:14 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-11 08:07:35 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.049 |  |
| 2026-11-11 08:07:07 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 08:06:49 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | -0.030 |  |
| 2026-11-11 08:06:22 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.154 |  |
| 2026-11-11 08:06:13 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.070 |  |
| 2026-11-11 08:05:51 | Baddegama (Gin Ganga) | 4.25 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 08:05:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:05:07 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | -0.029 |  |
| 2026-11-11 08:04:37 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:04:28 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:04:02 | Panadugama (Nilwala Ganga) | 5.81 | 🟡 Alert | -0.061 |  |
| 2026-11-11 08:03:59 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | -0.072 |  |
| 2026-11-11 08:03:59 | Dunamale (Aththanagalu Oya) | 4.20 | 🟡 Alert | -0.030 |  |
| 2026-11-11 08:03:33 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.153 |  |
| 2026-11-11 08:03:31 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | -0.112 |  |
| 2026-11-11 08:03:22 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-11 08:03:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:03:11 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.232 |  |
| 2026-11-11 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.045 |  |
| 2026-11-11 08:02:30 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.041 |  |
| 2026-11-11 08:02:26 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 08:02:09 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.114 |  |
| 2026-11-11 08:02:02 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:43 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:01:39 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-11-11 08:01:21 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-11 08:01:09 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:01:04 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-11-11 08:00:58 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.061 |  |
| 2026-11-11 08:00:56 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 08:00:28 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 08:07:07 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 08:05:51 | Baddegama (Gin Ganga) | 4.25 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 08:03:59 | Dunamale (Aththanagalu Oya) | 4.20 | 🟡 Alert | -0.030 |  |
| 2026-11-11 08:04:02 | Panadugama (Nilwala Ganga) | 5.81 | 🟡 Alert | -0.061 |  |
| 2026-11-11 08:03:22 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-11 08:08:14 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-11 08:00:56 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 08:05:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:01:09 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:01:43 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:04:28 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:04:37 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:14:31 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-11-11 08:11:14 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-11-11 08:02:02 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:39 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:02:26 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:03:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:04 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-11-11 08:01:21 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-11 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-11-11 08:12:34 | Moragaswewa (Deduru Oya) | 2.60 | 🟢 Normal | -0.022 |  |
| 2026-11-11 08:05:07 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | -0.029 |  |
| 2026-11-11 08:06:49 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | -0.030 |  |
| 2026-11-11 08:02:30 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.041 |  |
| 2026-11-11 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.045 |  |
| 2026-11-11 08:07:35 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.049 |  |
| 2026-11-11 08:00:58 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.061 |  |
| 2026-11-11 08:06:13 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.070 |  |
| 2026-11-11 08:03:59 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | -0.072 |  |
| 2026-11-11 08:10:55 | Badalgama (Maha Oya) | 4.41 | 🟢 Normal | -0.085 |  |
| 2026-11-11 08:03:31 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | -0.112 |  |
| 2026-11-11 08:02:09 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.114 |  |
| 2026-11-11 08:03:33 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.153 |  |
| 2026-11-11 08:06:22 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.154 |  |
| 2026-11-11 08:12:50 | Magura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.200 |  |
| 2026-11-11 08:10:45 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.215 |  |
| 2026-11-11 08:03:11 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)