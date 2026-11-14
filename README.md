# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_17:30:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,775 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 17:30:40 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.007 |  |
| 2026-11-14 17:28:01 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.013 |  |
| 2026-11-14 17:19:46 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-11-14 17:11:00 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:10:42 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.029 |  |
| 2026-11-14 17:08:54 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:08:44 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 17:07:59 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:07:24 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:07:05 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.019 |  |
| 2026-11-14 17:06:35 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | -0.045 |  |
| 2026-11-14 17:06:11 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-11-14 17:05:58 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-11-14 17:05:13 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.073 |  |
| 2026-11-14 17:05:11 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:05:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-11-14 17:05:06 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:04:20 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:04:18 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.048 |  |
| 2026-11-14 17:04:10 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | -0.029 |  |
| 2026-11-14 17:03:41 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | -0.044 |  |
| 2026-11-14 17:03:29 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:03:27 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:03:23 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:03:15 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:03:01 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 17:02:50 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:50 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-11-14 17:02:33 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.100 |  |
| 2026-11-14 17:02:26 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 17:02:25 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 17:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:11 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:02:04 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:01:38 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:01:33 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:00:52 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-14 17:00:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 17:08:44 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 17:04:10 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | -0.029 |  |
| 2026-11-14 17:00:52 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-14 17:02:25 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 17:03:01 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 17:05:06 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:04 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:11:00 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:03:29 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:01:38 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:07:24 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:08:54 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:01:33 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:03:15 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:50 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:05:11 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:07:59 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:30:40 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.007 |  |
| 2026-11-14 17:02:33 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:00:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:02:11 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:03:27 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:04:20 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:03:23 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:28:01 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.013 |  |
| 2026-11-14 17:07:05 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.019 |  |
| 2026-11-14 17:05:58 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-11-14 17:06:11 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-11-14 17:02:26 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 17:02:50 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-11-14 17:10:42 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.029 |  |
| 2026-11-14 17:05:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-11-14 17:19:46 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-11-14 17:03:41 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | -0.044 |  |
| 2026-11-14 17:06:35 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | -0.045 |  |
| 2026-11-14 17:04:18 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.048 |  |
| 2026-11-14 17:05:13 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.073 |  |
| 2026-11-14 17:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)