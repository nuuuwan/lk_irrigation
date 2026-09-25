# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_01:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,031 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 01:03:25 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:03:05 | Kithulgala (Kelani Ganga) | 2.87 | 🟢 Normal | -0.033 |  |
| 2026-09-26 01:03:01 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-09-26 01:02:57 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:02:47 | Rathnapura (Kalu Ganga) | 5.65 | 🟡 Alert | -0.083 |  |
| 2026-09-26 01:02:43 | Hanwella (Kelani Ganga) | 5.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-26 01:02:33 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:02:18 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:01:43 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-26 01:01:34 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | -0.042 |  |
| 2026-09-26 01:01:29 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:01:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:00:21 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:58:56 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 00:09:29 | Baddegama (Gin Ganga) | 4.77 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-26 00:17:35 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 00:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 00:03:04 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-26 00:03:21 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.034 |  |
| 2026-09-26 01:02:47 | Rathnapura (Kalu Ganga) | 5.65 | 🟡 Alert | -0.083 |  |
| 2026-09-26 01:01:43 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-26 00:01:51 | Glencourse (Kelani Ganga) | 13.90 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-26 00:02:28 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-26 01:02:43 | Hanwella (Kelani Ganga) | 5.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-26 00:07:52 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 00:05:05 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 01:00:21 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:01:23 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:01:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:02:57 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:58:56 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:02:18 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:05:27 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:03:25 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:05:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:02:49 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:02:37 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:01:29 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:02:33 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:06:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-26 00:05:33 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-26 00:03:30 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-26 01:03:01 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-09-26 00:05:57 | Nawalapitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-09-26 01:03:05 | Kithulgala (Kelani Ganga) | 2.87 | 🟢 Normal | -0.033 |  |
| 2026-09-26 00:10:06 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.037 |  |
| 2026-09-26 01:01:34 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | -0.042 |  |
| 2026-09-26 00:08:11 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.049 |  |
| 2026-09-26 00:04:26 | Deraniyagala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)