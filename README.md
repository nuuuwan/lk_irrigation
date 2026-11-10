# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_08:02:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,804 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 08:02:37 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-11-10 08:02:34 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.060 |  |
| 2026-11-10 08:02:29 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 08:02:28 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.049 |  |
| 2026-11-10 08:02:26 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-10 08:02:02 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-11-10 08:01:52 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | -0.093 |  |
| 2026-11-10 08:01:35 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 08:01:29 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.060 |  |
| 2026-11-10 08:01:26 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.064 |  |
| 2026-11-10 08:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-10 08:00:45 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | -0.079 |  |
| 2026-11-10 08:00:20 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 08:00:13 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 08:00:11 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 07:07:21 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2026-11-10 08:02:29 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 08:02:26 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-10 07:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.45 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-11-10 06:59:52 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-10 07:09:24 | Magura (Kalu Ganga) | 5.14 | 🟡 Alert | -0.027 |  |
| 2026-11-10 07:07:32 | Thawalama (Gin Ganga) | 4.63 | 🟡 Alert | -0.098 |  |
| 2026-11-10 07:02:47 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.103 |  |
| 2026-11-10 07:03:17 | Moragaswewa (Deduru Oya) | 4.07 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-10 07:08:52 | Badalgama (Maha Oya) | 4.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-10 07:09:58 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-10 07:02:21 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-10 08:00:13 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 08:01:35 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 08:00:20 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 07:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 07:02:29 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 07:05:54 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 07:17:53 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | -0.008 |  |
| 2026-11-10 08:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-10 07:02:22 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-11-10 08:02:02 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-11-10 08:00:11 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.022 |  |
| 2026-11-10 07:06:46 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-11-10 08:02:37 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-11-10 08:02:28 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.049 |  |
| 2026-11-10 08:01:29 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.060 |  |
| 2026-11-10 08:02:34 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.060 |  |
| 2026-11-10 07:05:56 | Hanwella (Kelani Ganga) | 6.23 | 🟢 Normal | -0.062 |  |
| 2026-11-10 08:01:26 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.064 |  |
| 2026-11-10 07:03:03 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | -0.074 |  |
| 2026-11-10 08:00:45 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | -0.079 |  |
| 2026-11-10 07:04:08 | Thanamalwila (Kirindi Oya) | 2.12 | 🟢 Normal | -0.091 |  |
| 2026-11-10 08:01:52 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | -0.093 |  |
| 2026-11-10 07:02:47 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.157 |  |
| 2026-11-10 07:11:35 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.220 |  |
| 2026-11-10 07:09:41 | Glencourse (Kelani Ganga) | 13.84 | 🟢 Normal | -0.245 |  |
| 2026-11-10 07:01:17 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)