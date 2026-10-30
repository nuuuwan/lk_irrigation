# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_05:36:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 05:36:06 | Panadugama (Nilwala Ganga) | 5.66 | 🟡 Alert | -0.020 |  |
| 2026-10-30 05:35:54 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:28:11 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-10-30 05:27:50 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-10-30 05:20:54 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.024 |  |
| 2026-10-30 05:17:37 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.016 |  |
| 2026-10-30 05:15:41 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | -0.016 |  |
| 2026-10-30 05:15:18 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-10-30 05:11:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | -0.226 |  |
| 2026-10-30 05:10:19 | Ellagawa (Kalu Ganga) | 9.20 | 🟢 Normal | -0.047 |  |
| 2026-10-30 05:08:07 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:07:28 | Baddegama (Gin Ganga) | 3.63 | 🟡 Alert | -7.579 |  |
| 2026-10-30 05:07:09 | Baddegama (Gin Ganga) | 3.67 | 🟡 Alert | -7.579 |  |
| 2026-10-30 05:06:51 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-10-30 05:06:30 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:06:00 | Putupaula (Kalu Ganga) | 3.56 | 🟡 Alert | -0.053 |  |
| 2026-10-30 05:05:40 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.101 |  |
| 2026-10-30 05:05:34 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-30 05:05:26 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.020 |  |
| 2026-10-30 05:04:52 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.074 |  |
| 2026-10-30 05:04:13 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:03:48 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.040 |  |
| 2026-10-30 05:03:47 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:03:21 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 05:15:41 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | -0.016 |  |
| 2026-10-30 05:11:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | -0.226 |  |
| 2026-10-30 05:36:06 | Panadugama (Nilwala Ganga) | 5.66 | 🟡 Alert | -0.020 |  |
| 2026-10-30 05:06:00 | Putupaula (Kalu Ganga) | 3.56 | 🟡 Alert | -0.053 |  |
| 2026-10-30 05:07:28 | Baddegama (Gin Ganga) | 3.63 | 🟡 Alert | -7.579 |  |
| 2026-10-30 05:28:11 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-30 04:01:46 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-30 05:02:53 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-30 05:02:20 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:01:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:35:54 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:03:47 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:02:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:08:07 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:06:30 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:04:13 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:02:03 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-30 05:05:34 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 05:17:37 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.016 |  |
| 2026-10-30 05:06:51 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-10-30 05:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-10-30 05:02:56 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.019 |  |
| 2026-10-30 05:02:47 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-10-30 05:05:26 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.020 |  |
| 2026-10-30 05:02:11 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.020 |  |
| 2026-10-30 05:15:18 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-10-30 05:20:54 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.024 |  |
| 2026-10-30 05:00:38 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.025 |  |
| 2026-10-30 04:08:42 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-10-30 05:03:21 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2026-10-30 05:02:46 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-10-30 05:03:48 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.040 |  |
| 2026-10-30 05:10:19 | Ellagawa (Kalu Ganga) | 9.20 | 🟢 Normal | -0.047 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-30 05:04:52 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.074 |  |
| 2026-10-30 05:05:40 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.101 |  |
| 2026-10-30 05:02:11 | Pitabeddara (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)