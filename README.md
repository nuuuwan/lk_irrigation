# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_06:14:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,707 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 06:14:13 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.008 |  |
| 2026-10-01 06:10:28 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-01 06:09:26 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 06:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-10-01 06:10:28 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-01 06:00:50 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 06:07:36 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-01 06:00:30 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-01 06:02:00 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 06:03:22 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 06:02:49 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:01:27 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:06:36 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:05:13 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:05:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:05:52 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:02:48 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:03:42 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:00:38 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:09:04 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:09:26 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:03:56 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:02:43 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:02:46 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:14:13 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.008 |  |
| 2026-10-01 05:02:54 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-01 06:03:40 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-10-01 06:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-10-01 06:01:50 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-01 06:01:08 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-10-01 06:01:53 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-10-01 06:05:06 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.011 |  |
| 2026-10-01 06:04:44 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.017 |  |
| 2026-10-01 06:04:00 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.020 |  |
| 2026-10-01 06:01:33 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.023 |  |
| 2026-10-01 06:03:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.045 |  |
| 2026-10-01 06:01:26 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.059 |  |
| 2026-10-01 06:05:31 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.069 |  |
| 2026-10-01 06:05:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.118 |  |
| 2026-10-01 06:04:19 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)