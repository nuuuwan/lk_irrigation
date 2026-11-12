# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_15:09:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,903 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 15:09:14 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 15:09:03 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:08:22 | Magura (Kalu Ganga) | 5.11 | 🟡 Alert | -0.050 |  |
| 2026-11-12 15:07:39 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-12 15:06:46 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:06:37 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.041 |  |
| 2026-11-12 15:06:29 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.059 |  |
| 2026-11-12 15:06:15 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | -0.062 |  |
| 2026-11-12 15:05:54 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:05:47 | Katharagama (Menik Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 15:05:20 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.187 |  |
| 2026-11-12 15:05:08 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.031 |  |
| 2026-11-12 15:04:55 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-11-12 15:04:12 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 15:03:53 | Weraganthota (Mahaweli Ganga) | -2.13 | 🟢 Normal | -0.009 |  |
| 2026-11-12 15:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 15:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 15:03:26 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:03:18 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | -0.010 |  |
| 2026-11-12 15:03:17 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-12 15:03:15 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | -0.052 |  |
| 2026-11-12 15:02:58 | Dunamale (Aththanagalu Oya) | 4.16 | 🟡 Alert | -0.026 |  |
| 2026-11-12 15:02:56 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 15:02:55 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | -0.010 |  |
| 2026-11-12 15:02:55 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | -0.108 |  |
| 2026-11-12 15:02:52 | Hanwella (Kelani Ganga) | 5.15 | 🟢 Normal | -0.110 |  |
| 2026-11-12 15:02:12 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.060 |  |
| 2026-11-12 15:01:58 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-12 15:01:50 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-11-12 15:01:37 | Thanamalwila (Kirindi Oya) | 2.48 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-12 15:01:31 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.066 |  |
| 2026-11-12 15:01:29 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-12 15:01:25 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-11-12 15:01:22 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-11-12 15:01:21 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:01:19 | Thaldena (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.745 | 🔺 Rising |
| 2026-11-12 15:00:34 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 15:00:21 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-11-12 14:59:57 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 15:04:12 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 15:09:14 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 15:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 15:03:18 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | -0.010 |  |
| 2026-11-12 15:02:55 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | -0.010 |  |
| 2026-11-12 15:02:58 | Dunamale (Aththanagalu Oya) | 4.16 | 🟡 Alert | -0.026 |  |
| 2026-11-12 15:08:22 | Magura (Kalu Ganga) | 5.11 | 🟡 Alert | -0.050 |  |
| 2026-11-12 15:01:19 | Thaldena (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.745 | 🔺 Rising |
| 2026-11-12 15:01:22 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-11-12 15:00:21 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-11-12 15:03:17 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-12 15:01:37 | Thanamalwila (Kirindi Oya) | 2.48 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-12 15:01:29 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-12 15:07:39 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-12 15:02:56 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 15:00:34 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 14:59:57 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-12 15:05:47 | Katharagama (Menik Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 15:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 15:01:21 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:05:54 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:06:46 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:09:03 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:03:26 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:03:53 | Weraganthota (Mahaweli Ganga) | -2.13 | 🟢 Normal | -0.009 |  |
| 2026-11-12 15:01:58 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-12 15:04:55 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-11-12 15:01:25 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-11-12 15:01:50 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-11-12 15:05:08 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.031 |  |
| 2026-11-12 15:06:37 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.041 |  |
| 2026-11-12 15:03:15 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | -0.052 |  |
| 2026-11-12 15:06:29 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.059 |  |
| 2026-11-12 15:02:12 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.060 |  |
| 2026-11-12 15:06:15 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | -0.062 |  |
| 2026-11-12 15:01:31 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.066 |  |
| 2026-11-12 15:02:55 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | -0.108 |  |
| 2026-11-12 15:02:52 | Hanwella (Kelani Ganga) | 5.15 | 🟢 Normal | -0.110 |  |
| 2026-11-12 15:05:20 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.187 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)