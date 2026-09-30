# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_06:14:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,806 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 06:14:23 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-09-30 06:10:27 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:07:51 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.028 |  |
| 2026-09-30 06:06:33 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:05:56 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-09-30 06:05:52 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-09-30 06:05:26 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-09-30 06:05:03 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-30 06:04:50 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:04:29 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.126 |  |
| 2026-09-30 06:04:27 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.039 |  |
| 2026-09-30 06:04:19 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:04:13 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-30 06:04:09 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 06:05:03 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-30 06:00:16 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-30 06:04:13 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-30 06:04:09 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-30 06:00:24 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 06:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-30 06:03:59 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 06:00:37 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:02:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:03:06 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:10:27 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:04:19 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:04:50 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:00:31 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:04:01 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:02:25 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:06:33 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:00:33 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:01:09 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:14:23 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-09-30 06:05:26 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-09-30 06:04:00 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-09-30 06:05:52 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-09-30 06:05:56 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-09-30 06:02:17 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-09-30 06:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-09-30 06:01:07 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-09-30 06:00:53 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.022 |  |
| 2026-09-30 06:07:51 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.028 |  |
| 2026-09-30 06:01:46 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.030 |  |
| 2026-09-30 06:03:05 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.039 |  |
| 2026-09-30 06:04:27 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.039 |  |
| 2026-09-30 06:01:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.040 |  |
| 2026-09-30 06:02:12 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.043 |  |
| 2026-09-30 06:04:29 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.126 |  |
| 2026-09-30 06:02:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.183 |  |
| 2026-09-30 06:03:25 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.231 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)