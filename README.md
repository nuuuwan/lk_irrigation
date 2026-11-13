# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_19:28:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 19:28:01 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | -0.030 |  |
| 2026-11-13 19:25:50 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.008 |  |
| 2026-11-13 19:14:36 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.061 |  |
| 2026-11-13 19:14:18 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 19:13:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | -0.034 |  |
| 2026-11-13 19:13:19 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:09:27 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-11-13 19:08:22 | Moraketiya (Walawe Ganga) | 3.70 | 🟡 Alert | -0.027 |  |
| 2026-11-13 19:08:10 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.039 |  |
| 2026-11-13 19:06:35 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.029 |  |
| 2026-11-13 19:05:52 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.087 |  |
| 2026-11-13 19:05:40 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-11-13 19:05:33 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.057 |  |
| 2026-11-13 19:05:11 | Baddegama (Gin Ganga) | 4.03 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-13 19:05:02 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.066 |  |
| 2026-11-13 19:05:01 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-11-13 19:04:00 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:03:52 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.040 |  |
| 2026-11-13 19:03:28 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:03:02 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-11-13 19:02:52 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:02:25 | Kuda Oya (Kirindi Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:02:16 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-13 19:02:10 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:02:08 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-11-13 19:02:04 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.060 |  |
| 2026-11-13 19:02:03 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:02:02 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:02:01 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:01:53 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.050 |  |
| 2026-11-13 19:01:42 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.042 |  |
| 2026-11-13 19:01:41 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:00:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.090 |  |
| 2026-11-13 19:00:33 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:00:16 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:00:08 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 19:14:18 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 19:05:11 | Baddegama (Gin Ganga) | 4.03 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-13 19:28:01 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | -0.030 |  |
| 2026-11-13 19:08:22 | Moraketiya (Walawe Ganga) | 3.70 | 🟡 Alert | -0.027 |  |
| 2026-11-13 19:13:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | -0.034 |  |
| 2026-11-13 19:02:16 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 19:00:33 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:02:01 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:02:03 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:13:19 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:04:00 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:02:10 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-11-13 19:25:50 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.008 |  |
| 2026-11-13 19:09:27 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-11-13 19:03:28 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:00:16 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:01:41 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:00:08 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:02:25 | Kuda Oya (Kirindi Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 19:03:02 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-11-13 19:05:01 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-11-13 19:05:40 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-11-13 19:02:08 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-13 19:06:35 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.029 |  |
| 2026-11-13 19:08:10 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.039 |  |
| 2026-11-13 19:03:52 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.040 |  |
| 2026-11-13 19:01:42 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.042 |  |
| 2026-11-13 19:01:53 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.050 |  |
| 2026-11-13 19:05:33 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.057 |  |
| 2026-11-13 19:02:04 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.060 |  |
| 2026-11-13 19:14:36 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.061 |  |
| 2026-11-13 19:05:02 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.066 |  |
| 2026-11-13 19:05:52 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.087 |  |
| 2026-11-13 19:00:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)