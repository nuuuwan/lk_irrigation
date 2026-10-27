# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_19:10:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,630 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 19:10:49 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.044 |  |
| 2026-10-27 19:07:09 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.009 |  |
| 2026-10-27 19:07:09 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -12.150 |  |
| 2026-10-27 19:07:03 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:06:27 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | 0.000 |  |
| 2026-10-27 19:06:14 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | -0.029 |  |
| 2026-10-27 19:06:09 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-27 19:05:56 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-27 19:05:50 | Rathnapura (Kalu Ganga) | 7.70 | 🟠 Minor Flood | -0.113 |  |
| 2026-10-27 19:05:28 | Ellagawa (Kalu Ganga) | 10.13 | 🟡 Alert | -0.009 |  |
| 2026-10-27 19:04:52 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 19:04:39 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-10-27 19:04:21 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:04:08 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-10-27 19:03:58 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-27 19:03:54 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:03:41 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.068 |  |
| 2026-10-27 19:03:30 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-10-27 19:03:22 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.064 |  |
| 2026-10-27 19:03:19 | Glencourse (Kelani Ganga) | 12.17 | 🟢 Normal | -0.087 |  |
| 2026-10-27 19:03:02 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:03:02 | Moragaswewa (Deduru Oya) | 4.61 | 🟢 Normal | -0.196 |  |
| 2026-10-27 19:02:47 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 19:02:42 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:02:35 | Magura (Kalu Ganga) | 4.76 | 🟡 Alert | -0.048 |  |
| 2026-10-27 19:02:29 | Dunamale (Aththanagalu Oya) | 4.75 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-27 19:02:25 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-10-27 19:02:09 | Hanwella (Kelani Ganga) | 5.29 | 🟢 Normal | -0.101 |  |
| 2026-10-27 19:01:57 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.151 |  |
| 2026-10-27 19:01:49 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | -12.150 |  |
| 2026-10-27 19:01:36 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-27 19:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-27 19:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.66 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-27 19:00:08 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-10-27 19:00:08 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:29:26 | Moragaswewa (Deduru Oya) | 4.72 | 🟢 Normal | -0.196 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 19:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.66 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-27 19:03:58 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-27 19:02:29 | Dunamale (Aththanagalu Oya) | 4.75 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-27 19:06:14 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | -0.029 |  |
| 2026-10-27 19:05:50 | Rathnapura (Kalu Ganga) | 7.70 | 🟠 Minor Flood | -0.113 |  |
| 2026-10-27 19:04:52 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 19:06:27 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | 0.000 |  |
| 2026-10-27 19:05:28 | Ellagawa (Kalu Ganga) | 10.13 | 🟡 Alert | -0.009 |  |
| 2026-10-27 19:02:35 | Magura (Kalu Ganga) | 4.76 | 🟡 Alert | -0.048 |  |
| 2026-10-27 19:02:47 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 18:01:41 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:03:02 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:02:42 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:00:08 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:04:21 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:07:03 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-27 19:03:54 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-27 19:07:09 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.009 |  |
| 2026-10-27 19:04:39 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-10-27 19:01:36 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-27 19:05:56 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-27 18:01:28 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-27 19:06:09 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-27 19:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-27 19:03:30 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-10-27 19:04:08 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-10-27 19:02:25 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-10-27 19:00:08 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-10-27 19:10:49 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.044 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-27 19:03:22 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.064 |  |
| 2026-10-27 19:03:41 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.068 |  |
| 2026-10-27 19:03:19 | Glencourse (Kelani Ganga) | 12.17 | 🟢 Normal | -0.087 |  |
| 2026-10-27 19:02:09 | Hanwella (Kelani Ganga) | 5.29 | 🟢 Normal | -0.101 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-27 19:01:57 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.151 |  |
| 2026-10-27 19:03:02 | Moragaswewa (Deduru Oya) | 4.61 | 🟢 Normal | -0.196 |  |
| 2026-10-27 19:07:09 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -12.150 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)