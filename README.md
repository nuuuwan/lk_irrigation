# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_01:03:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,207 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 01:03:18 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:03:04 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 01:03:00 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-14 01:02:48 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:02:36 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 01:02:16 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-14 01:02:12 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:02:09 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | -0.085 |  |
| 2026-09-14 01:02:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-09-14 01:01:35 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.050 |  |
| 2026-09-14 01:01:15 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:01:11 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 01:02:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-09-14 00:03:51 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-14 00:02:19 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-14 00:00:39 | Magura (Kalu Ganga) | 2.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-14 01:02:16 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-14 00:02:34 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 01:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 01:03:04 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 00:09:36 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:03:07 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:01:15 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:04:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:02:12 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:06:30 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:01:11 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:03:26 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:10:23 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:02:53 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:01:30 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:02:48 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:05:19 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:03:18 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:02:36 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:02:31 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:01:48 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:03:00 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-14 00:06:45 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-09-14 00:08:45 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.020 |  |
| 2026-09-14 00:02:16 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-09-14 00:08:06 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-09-14 00:06:21 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.047 |  |
| 2026-09-14 01:01:35 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.050 |  |
| 2026-09-14 00:04:02 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.057 |  |
| 2026-09-14 00:03:21 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.062 |  |
| 2026-09-14 01:02:09 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)