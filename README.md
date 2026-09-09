# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_17:03:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,328 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 17:03:23 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 17:03:05 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:03 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:52 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 17:02:49 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.116 |  |
| 2026-09-09 17:02:27 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:25 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:12 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:11 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:11 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:10 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.060 |  |
| 2026-09-09 17:01:49 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 17:01:44 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:01:03 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.161 |  |
| 2026-09-09 17:00:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:26:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.116 |  |
| 2026-09-09 16:26:25 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 17:01:49 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 17:02:52 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 16:02:37 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 16:06:10 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-09 17:03:23 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 17:02:11 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:00:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:49 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:57:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:01:54 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:11 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:00:58 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:03 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:25 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:05 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:03:09 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:25 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:11 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:00:11 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:27 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:01:44 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:40 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:49 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:03:27 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:12 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:26:25 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:07:09 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:03:47 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:01:08 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-09-09 16:04:54 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-09-09 16:00:37 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-09 16:09:10 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.039 |  |
| 2026-09-09 16:06:17 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.047 |  |
| 2026-09-09 17:02:10 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.060 |  |
| 2026-09-09 16:04:28 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.080 |  |
| 2026-09-09 16:02:22 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.097 |  |
| 2026-09-09 17:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.116 |  |
| 2026-09-09 17:01:03 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)