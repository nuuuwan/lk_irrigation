# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_10:03:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 10:03:09 | Giriulla (Maha Oya) | 2.64 | 🟢 Normal | -0.100 |  |
| 2026-11-10 10:03:04 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:02:53 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 10:02:34 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-11-10 10:02:14 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.050 |  |
| 2026-11-10 10:02:09 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.071 |  |
| 2026-11-10 10:01:43 | Moraketiya (Walawe Ganga) | 2.99 | 🟢 Normal | -0.031 |  |
| 2026-11-10 10:01:22 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.040 |  |
| 2026-11-10 10:01:14 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-11-10 10:01:11 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.106 |  |
| 2026-11-10 10:00:13 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-10 10:00:13 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 10:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-11-10 09:05:43 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-11-10 09:02:03 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 10:02:14 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.050 |  |
| 2026-11-10 09:02:13 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-11-10 09:07:55 | Magura (Kalu Ganga) | 5.01 | 🟡 Alert | -0.084 |  |
| 2026-11-10 09:05:35 | Thawalama (Gin Ganga) | 4.25 | 🟡 Alert | -0.253 |  |
| 2026-11-10 09:02:36 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.960 | 🔺 Rising |
| 2026-11-10 10:00:13 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-10 09:02:06 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-10 09:03:44 | Moragaswewa (Deduru Oya) | 4.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-10 10:02:53 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 09:02:54 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-10 09:05:56 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 09:05:37 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:01:14 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 09:06:16 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:03:04 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-10 09:02:28 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:02:34 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:00:13 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-10 09:05:44 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-11-10 09:08:08 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-11-10 10:01:43 | Moraketiya (Walawe Ganga) | 2.99 | 🟢 Normal | -0.031 |  |
| 2026-11-10 10:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-11-10 10:01:22 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.040 |  |
| 2026-11-10 09:03:01 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.043 |  |
| 2026-11-10 09:06:00 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | -0.060 |  |
| 2026-11-10 09:06:57 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-11-10 10:02:09 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.071 |  |
| 2026-11-10 10:03:09 | Giriulla (Maha Oya) | 2.64 | 🟢 Normal | -0.100 |  |
| 2026-11-10 10:01:11 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.106 |  |
| 2026-11-10 09:01:23 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | -0.108 |  |
| 2026-11-10 09:04:34 | Hanwella (Kelani Ganga) | 6.05 | 🟢 Normal | -0.117 |  |
| 2026-11-10 09:03:58 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.133 |  |
| 2026-11-10 09:08:38 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.211 |  |
| 2026-11-10 09:05:05 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.237 |  |
| 2026-11-10 09:07:46 | Glencourse (Kelani Ganga) | 13.30 | 🟢 Normal | -0.271 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)