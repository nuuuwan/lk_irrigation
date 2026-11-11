# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_09:03:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,741 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 09:03:21 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.022 |  |
| 2026-11-11 09:03:21 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.199 |  |
| 2026-11-11 09:03:08 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | -0.021 |  |
| 2026-11-11 09:03:03 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.021 |  |
| 2026-11-11 09:02:56 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-11-11 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 09:02:42 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.081 |  |
| 2026-11-11 09:02:40 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-11-11 09:02:35 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:02:21 | Dunamale (Aththanagalu Oya) | 4.17 | 🟡 Alert | -0.031 |  |
| 2026-11-11 09:02:17 | Horowpothana (Yan Oya) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-11-11 09:02:14 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | -0.024 |  |
| 2026-11-11 09:02:09 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.118 |  |
| 2026-11-11 09:01:50 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-11 09:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:01:30 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:01:08 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-11 09:01:07 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:01:07 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:01:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.046 |  |
| 2026-11-11 09:00:11 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 08:07:07 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 08:05:51 | Baddegama (Gin Ganga) | 4.25 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 09:02:21 | Dunamale (Aththanagalu Oya) | 4.17 | 🟡 Alert | -0.031 |  |
| 2026-11-11 08:04:02 | Panadugama (Nilwala Ganga) | 5.81 | 🟡 Alert | -0.061 |  |
| 2026-11-11 08:03:22 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-11 09:01:50 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-11 08:08:14 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-11 09:00:11 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 08:05:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:01:07 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:01:30 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:02:35 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-11 09:01:07 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:14:31 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-11-11 08:11:14 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-11-11 09:01:08 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-11 09:02:40 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-11-11 09:03:03 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.021 |  |
| 2026-11-11 09:03:08 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | -0.021 |  |
| 2026-11-11 09:03:21 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.022 |  |
| 2026-11-11 09:02:14 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | -0.024 |  |
| 2026-11-11 08:05:07 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | -0.029 |  |
| 2026-11-11 09:02:56 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-11-11 09:02:17 | Horowpothana (Yan Oya) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-11-11 08:02:30 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.041 |  |
| 2026-11-11 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.045 |  |
| 2026-11-11 09:01:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.046 |  |
| 2026-11-11 08:03:59 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | -0.072 |  |
| 2026-11-11 09:02:42 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.081 |  |
| 2026-11-11 08:10:55 | Badalgama (Maha Oya) | 4.41 | 🟢 Normal | -0.085 |  |
| 2026-11-11 08:03:31 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | -0.112 |  |
| 2026-11-11 09:02:09 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.118 |  |
| 2026-11-11 08:06:22 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.154 |  |
| 2026-11-11 09:03:21 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.199 |  |
| 2026-11-11 08:12:50 | Magura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.200 |  |
| 2026-11-11 08:10:45 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.215 |  |

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

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)