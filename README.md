# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_07:04:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 07:04:35 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:04:25 | Putupaula (Kalu Ganga) | 3.46 | 🟡 Alert | -0.029 |  |
| 2026-10-30 07:04:22 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:04:18 | Panadugama (Nilwala Ganga) | 5.60 | 🟡 Alert | -0.032 |  |
| 2026-10-30 07:04:15 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.029 |  |
| 2026-10-30 07:04:13 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.047 |  |
| 2026-10-30 07:03:55 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-30 07:03:43 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-30 07:03:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:03:14 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:03:02 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-30 07:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 07:02:39 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.029 |  |
| 2026-10-30 07:02:23 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.084 |  |
| 2026-10-30 07:01:33 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.001 |  |
| 2026-10-30 07:01:19 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:01:13 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:01:05 | Baddegama (Gin Ganga) | 3.57 | 🟡 Alert | -0.033 |  |
| 2026-10-30 07:00:21 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.127 |  |
| 2026-10-30 06:39:10 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-10-30 06:36:32 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 07:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 06:36:32 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-30 07:04:25 | Putupaula (Kalu Ganga) | 3.46 | 🟡 Alert | -0.029 |  |
| 2026-10-30 07:04:18 | Panadugama (Nilwala Ganga) | 5.60 | 🟡 Alert | -0.032 |  |
| 2026-10-30 07:01:05 | Baddegama (Gin Ganga) | 3.57 | 🟡 Alert | -0.033 |  |
| 2026-10-30 06:04:54 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 06:03:41 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 07:01:33 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.001 |  |
| 2026-10-30 07:01:19 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:03:14 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:06:13 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:04:35 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:03:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:02:04 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:04:22 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 07:01:13 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:05:45 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-30 07:03:55 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 07:03:43 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-30 07:03:02 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-30 06:02:48 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-10-30 06:39:10 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-10-30 06:07:48 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.019 |  |
| 2026-10-30 06:03:02 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-10-30 06:02:57 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.025 |  |
| 2026-10-30 06:04:40 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.026 |  |
| 2026-10-30 07:04:15 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.029 |  |
| 2026-10-30 07:02:39 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.029 |  |
| 2026-10-30 06:07:11 | Ellagawa (Kalu Ganga) | 9.17 | 🟢 Normal | -0.032 |  |
| 2026-10-30 07:04:13 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.047 |  |
| 2026-10-30 06:00:57 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.052 |  |
| 2026-10-30 06:01:19 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.052 |  |
| 2026-10-30 06:02:24 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.074 |  |
| 2026-10-30 07:02:23 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.084 |  |
| 2026-10-30 06:06:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.115 |  |
| 2026-10-30 06:01:36 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.127 |  |
| 2026-10-30 07:00:21 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)