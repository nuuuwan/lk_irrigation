# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_17:03:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,957 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 17:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 17:03:18 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-12 17:03:17 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-12 17:02:46 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-12 17:02:23 | Hanwella (Kelani Ganga) | 4.96 | 🟢 Normal | -0.071 |  |
| 2026-11-12 17:02:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.076 |  |
| 2026-11-12 17:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | -0.010 |  |
| 2026-11-12 17:02:16 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-12 17:01:49 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-11-12 17:01:33 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.074 |  |
| 2026-11-12 17:01:09 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-12 17:01:08 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 17:00:30 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.120 |  |
| 2026-11-12 17:00:22 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:30:00 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 16:12:43 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-11-12 16:30:00 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 16:13:11 | Panadugama (Nilwala Ganga) | 5.92 | 🟡 Alert | 0.052 | 🔺 Rising |
| 2026-11-12 17:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | -0.010 |  |
| 2026-11-12 16:03:45 | Dunamale (Aththanagalu Oya) | 4.14 | 🟡 Alert | -0.020 |  |
| 2026-11-12 16:02:48 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | -0.020 |  |
| 2026-11-12 16:07:26 | Magura (Kalu Ganga) | 5.07 | 🟡 Alert | -0.041 |  |
| 2026-11-12 16:04:26 | Thaldena (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.494 | 🔺 Rising |
| 2026-11-12 16:03:47 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-12 16:03:26 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-11-12 17:02:16 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-12 17:02:46 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-12 17:03:17 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-12 16:03:55 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-12 16:02:38 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-12 17:01:09 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-12 16:09:48 | Thanamalwila (Kirindi Oya) | 2.52 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-12 17:01:08 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 17:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 17:00:22 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:16:09 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:04:28 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:04:51 | Katharagama (Menik Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-12 16:15:39 | Ellagawa (Kalu Ganga) | 8.31 | 🟢 Normal | -0.009 |  |
| 2026-11-12 17:03:18 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-12 16:04:27 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-11-12 17:01:49 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-11-12 16:07:56 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-11-12 16:02:39 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-11-12 16:03:30 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.063 |  |
| 2026-11-12 16:03:30 | Peradeniya (Mahaweli Ganga) | 4.53 | 🟢 Normal | -0.070 |  |
| 2026-11-12 17:02:23 | Hanwella (Kelani Ganga) | 4.96 | 🟢 Normal | -0.071 |  |
| 2026-11-12 17:01:33 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.074 |  |
| 2026-11-12 16:07:10 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.075 |  |
| 2026-11-12 17:02:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.076 |  |
| 2026-11-12 16:06:25 | Badalgama (Maha Oya) | 4.04 | 🟢 Normal | -0.080 |  |
| 2026-11-12 16:09:14 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.094 |  |
| 2026-11-12 17:00:30 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.120 |  |
| 2026-11-12 16:04:18 | Wellawaya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)