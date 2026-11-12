# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_16:30:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,943 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 16:30:00 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 16:16:09 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:15:39 | Ellagawa (Kalu Ganga) | 8.31 | 🟢 Normal | -0.009 |  |
| 2026-11-12 16:14:56 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.016 |  |
| 2026-11-12 16:13:11 | Panadugama (Nilwala Ganga) | 5.92 | 🟡 Alert | 0.052 | 🔺 Rising |
| 2026-11-12 16:13:00 | Giriulla (Maha Oya) | 2.56 | 🟢 Normal | -0.059 |  |
| 2026-11-12 16:12:43 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-11-12 16:11:38 | Kuda Oya (Kirindi Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:09:48 | Thanamalwila (Kirindi Oya) | 2.52 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-12 16:09:14 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.094 |  |
| 2026-11-12 16:07:56 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-11-12 16:07:26 | Magura (Kalu Ganga) | 5.07 | 🟡 Alert | -0.041 |  |
| 2026-11-12 16:07:10 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.075 |  |
| 2026-11-12 16:06:50 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-12 16:06:25 | Badalgama (Maha Oya) | 4.04 | 🟢 Normal | -0.080 |  |
| 2026-11-12 16:04:51 | Katharagama (Menik Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:04:28 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:04:27 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-11-12 16:04:26 | Thaldena (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.494 | 🔺 Rising |
| 2026-11-12 16:04:18 | Wellawaya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.153 |  |
| 2026-11-12 16:03:55 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-12 16:03:47 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-12 16:03:45 | Dunamale (Aththanagalu Oya) | 4.14 | 🟡 Alert | -0.020 |  |
| 2026-11-12 16:03:42 | Kuda Oya (Kirindi Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:03:30 | Peradeniya (Mahaweli Ganga) | 4.53 | 🟢 Normal | -0.070 |  |
| 2026-11-12 16:03:30 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.063 |  |
| 2026-11-12 16:03:26 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-11-12 16:03:22 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-11-12 16:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 16:03:02 | Hanwella (Kelani Ganga) | 5.03 | 🟢 Normal | -0.120 |  |
| 2026-11-12 16:02:48 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | -0.020 |  |
| 2026-11-12 16:02:39 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-11-12 16:02:38 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-12 16:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 16:02:01 | Nagalagam Street (Kelani Ganga) | 0.96 | 🟢 Normal | -0.015 |  |
| 2026-11-12 16:01:38 | Manampitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 16:01:19 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-11-12 16:01:11 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 16:00:32 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-12 16:00:24 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 16:12:43 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-11-12 16:30:00 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 16:13:11 | Panadugama (Nilwala Ganga) | 5.92 | 🟡 Alert | 0.052 | 🔺 Rising |
| 2026-11-12 16:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 16:03:45 | Dunamale (Aththanagalu Oya) | 4.14 | 🟡 Alert | -0.020 |  |
| 2026-11-12 16:02:48 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | -0.020 |  |
| 2026-11-12 16:07:26 | Magura (Kalu Ganga) | 5.07 | 🟡 Alert | -0.041 |  |
| 2026-11-12 16:04:26 | Thaldena (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.494 | 🔺 Rising |
| 2026-11-12 16:03:47 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-12 16:03:26 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-11-12 16:00:32 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-12 16:03:55 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-12 16:02:38 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-12 16:06:50 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-12 16:09:48 | Thanamalwila (Kirindi Oya) | 2.52 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-12 16:01:38 | Manampitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 16:01:11 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 16:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 16:16:09 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:04:28 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:04:51 | Katharagama (Menik Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:11:38 | Kuda Oya (Kirindi Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:15:39 | Ellagawa (Kalu Ganga) | 8.31 | 🟢 Normal | -0.009 |  |
| 2026-11-12 16:04:27 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-11-12 16:01:19 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-11-12 16:02:01 | Nagalagam Street (Kelani Ganga) | 0.96 | 🟢 Normal | -0.015 |  |
| 2026-11-12 16:14:56 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.016 |  |
| 2026-11-12 16:07:56 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-11-12 16:02:39 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-11-12 16:00:24 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-12 16:03:22 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-11-12 16:13:00 | Giriulla (Maha Oya) | 2.56 | 🟢 Normal | -0.059 |  |
| 2026-11-12 16:03:30 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.063 |  |
| 2026-11-12 16:03:30 | Peradeniya (Mahaweli Ganga) | 4.53 | 🟢 Normal | -0.070 |  |
| 2026-11-12 16:07:10 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.075 |  |
| 2026-11-12 16:06:25 | Badalgama (Maha Oya) | 4.04 | 🟢 Normal | -0.080 |  |
| 2026-11-12 16:09:14 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.094 |  |
| 2026-11-12 16:03:02 | Hanwella (Kelani Ganga) | 5.03 | 🟢 Normal | -0.120 |  |
| 2026-11-12 16:04:18 | Wellawaya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)