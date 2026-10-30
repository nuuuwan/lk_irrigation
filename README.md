# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_13:29:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 13:29:24 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.007 |  |
| 2026-10-30 13:20:09 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:12:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.051 |  |
| 2026-10-30 13:10:12 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:09:39 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-10-30 13:09:14 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:08:38 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-30 13:08:27 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:08:26 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:08:24 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:07:24 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | -0.030 |  |
| 2026-10-30 13:06:47 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:06:31 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.037 |  |
| 2026-10-30 13:05:59 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 13:05:50 | Panadugama (Nilwala Ganga) | 5.33 | 🟡 Alert | -0.040 |  |
| 2026-10-30 13:05:31 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:05:30 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:05:15 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 20.571 | 🔺 Rising |
| 2026-10-30 13:04:27 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-10-30 13:04:19 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 20.571 | 🔺 Rising |
| 2026-10-30 13:04:13 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.072 |  |
| 2026-10-30 13:04:12 | Putupaula (Kalu Ganga) | 3.31 | 🟡 Alert | -0.029 |  |
| 2026-10-30 13:03:50 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 13:03:47 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-10-30 13:03:45 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:58 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-10-30 13:02:51 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-30 13:02:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:40 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:02:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:19 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:12 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:04 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:02:03 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.070 |  |
| 2026-10-30 13:01:34 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:01:18 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:01:08 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:00:37 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:00:26 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.231 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 13:05:59 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 13:12:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.051 |  |
| 2026-10-30 13:04:12 | Putupaula (Kalu Ganga) | 3.31 | 🟡 Alert | -0.029 |  |
| 2026-10-30 13:05:50 | Panadugama (Nilwala Ganga) | 5.33 | 🟡 Alert | -0.040 |  |
| 2026-10-30 13:05:15 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 20.571 | 🔺 Rising |
| 2026-10-30 13:08:38 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-30 13:02:51 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-30 13:03:50 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 13:01:08 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:12 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:19 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:20:09 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:08:26 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:06:47 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:09:14 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:02:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:08:27 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:03:45 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:10:12 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:01:34 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:29:24 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.007 |  |
| 2026-10-30 13:09:39 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-10-30 13:05:30 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:02:04 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:00:37 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:02:40 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:01:18 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:05:31 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:03:47 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-10-30 13:02:58 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-10-30 13:04:27 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-10-30 13:07:24 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | -0.030 |  |
| 2026-10-30 12:02:23 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.033 |  |
| 2026-10-30 13:06:31 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.037 |  |
| 2026-10-30 13:02:03 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.070 |  |
| 2026-10-30 13:04:13 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.072 |  |
| 2026-10-30 13:00:26 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.231 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)