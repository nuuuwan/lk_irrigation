# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_23:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 23:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.080 |  |
| 2026-11-10 23:03:05 | Peradeniya (Mahaweli Ganga) | 5.50 | 🟡 Alert | -0.218 |  |
| 2026-11-10 23:02:47 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-10 23:02:39 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | -0.034 |  |
| 2026-11-10 23:02:38 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-10 23:02:37 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-11-10 23:02:36 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-10 23:02:27 | Dunamale (Aththanagalu Oya) | 4.44 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-10 23:02:03 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:02:01 | Moragaswewa (Deduru Oya) | 3.46 | 🟢 Normal | -0.080 |  |
| 2026-11-10 23:01:30 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:01:25 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-10 23:01:13 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:00:27 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.060 |  |
| 2026-11-10 22:28:44 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:25:23 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.003 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 22:01:44 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | 0.082 | 🔺 Rising |
| 2026-11-10 22:08:09 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 22:07:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | -0.009 |  |
| 2026-11-10 23:02:27 | Dunamale (Aththanagalu Oya) | 4.44 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-10 23:01:25 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-10 22:05:29 | Thawalama (Gin Ganga) | 4.10 | 🟡 Alert | 0.273 | 🔺 Rising |
| 2026-11-10 22:04:50 | Rathnapura (Kalu Ganga) | 5.75 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-10 22:08:28 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | -0.020 |  |
| 2026-11-10 23:03:05 | Peradeniya (Mahaweli Ganga) | 5.50 | 🟡 Alert | -0.218 |  |
| 2026-11-10 22:01:12 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-11-10 23:02:47 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-10 23:02:38 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 22:02:57 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-10 22:02:07 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-10 22:01:14 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-10 23:02:03 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:01:13 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:07:18 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:05:25 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:28:44 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:25:23 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.003 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-10 22:06:31 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-11-10 22:07:30 | Holombuwa (Kelani Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:01:30 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:02:36 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-10 23:02:37 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-11-10 23:02:39 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | -0.034 |  |
| 2026-11-10 22:07:19 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.040 |  |
| 2026-11-10 22:08:07 | Moraketiya (Walawe Ganga) | 2.46 | 🟢 Normal | -0.055 |  |
| 2026-11-10 23:00:27 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.060 |  |
| 2026-11-10 23:02:01 | Moragaswewa (Deduru Oya) | 3.46 | 🟢 Normal | -0.080 |  |
| 2026-11-10 23:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.080 |  |
| 2026-11-10 22:04:12 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.080 |  |
| 2026-11-10 22:02:00 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.082 |  |
| 2026-11-10 21:03:47 | Siyambalanduwa (Heda Oya) | 1.40 | 🟢 Normal | -0.092 |  |
| 2026-11-10 22:08:32 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)