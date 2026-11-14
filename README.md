# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_00:19:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,038 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 00:19:08 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.066 |  |
| 2026-11-15 00:17:25 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:15:21 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-15 00:11:29 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.009 |  |
| 2026-11-15 00:11:05 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -36.000 |  |
| 2026-11-15 00:11:04 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -36.000 |  |
| 2026-11-15 00:10:51 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-15 00:09:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -1.236 |  |
| 2026-11-15 00:09:02 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-15 00:08:46 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 00:08:23 | Nagalagam Street (Kelani Ganga) | 0.48 | 🟢 Normal | -1.236 |  |
| 2026-11-15 00:08:09 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:06:59 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:06:14 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.040 |  |
| 2026-11-15 00:06:01 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:06:00 | Panadugama (Nilwala Ganga) | 5.07 | 🟡 Alert | -0.030 |  |
| 2026-11-15 00:05:38 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:05:37 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:05:19 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:04:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.109 |  |
| 2026-11-15 00:04:20 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:04:11 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-11-15 00:03:46 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:03:45 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:03:24 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 00:03:24 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.011 |  |
| 2026-11-15 00:03:06 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:02:54 | Wellawaya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.216 |  |
| 2026-11-15 00:02:48 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:02:47 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.031 |  |
| 2026-11-15 00:02:46 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-15 00:02:45 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-15 00:02:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:02:25 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-11-15 00:01:58 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:01:35 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:00:47 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:00:07 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:57:17 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.044 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 00:08:46 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 00:06:00 | Panadugama (Nilwala Ganga) | 5.07 | 🟡 Alert | -0.030 |  |
| 2026-11-15 00:10:51 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 00:09:02 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-15 00:15:21 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-15 00:01:58 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:01:35 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:06:01 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:02:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:00:07 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:08:09 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:00:47 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:03:46 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:03:06 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:06:59 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:05:19 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:05:38 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-15 00:11:29 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.009 |  |
| 2026-11-15 00:04:20 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:05:37 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:02:48 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:03:45 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:17:25 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-11-15 00:02:25 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-15 00:03:24 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.011 |  |
| 2026-11-15 00:02:45 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-15 00:02:46 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-15 00:04:11 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-11-15 00:02:47 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.031 |  |
| 2026-11-15 00:06:14 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.040 |  |
| 2026-11-15 00:19:08 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.066 |  |
| 2026-11-15 00:04:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.109 |  |
| 2026-11-15 00:02:54 | Wellawaya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.216 |  |
| 2026-11-15 00:09:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -1.236 |  |
| 2026-11-15 00:11:05 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)