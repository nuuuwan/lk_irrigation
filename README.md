# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_08:03:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,696 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 08:03:11 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.232 |  |
| 2026-11-11 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.045 |  |
| 2026-11-11 08:02:30 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.041 |  |
| 2026-11-11 08:02:26 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 08:02:09 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.114 |  |
| 2026-11-11 08:02:02 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:43 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:01:39 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-11-11 08:01:21 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-11 08:01:09 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:01:04 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-11-11 08:00:58 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.061 |  |
| 2026-11-11 08:00:56 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 08:00:28 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-11-11 07:26:29 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 07:24:50 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 07:05:12 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 07:24:50 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 07:04:38 | Dunamale (Aththanagalu Oya) | 4.23 | 🟡 Alert | -0.029 |  |
| 2026-11-11 07:04:52 | Panadugama (Nilwala Ganga) | 5.87 | 🟡 Alert | -0.061 |  |
| 2026-11-11 07:06:23 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-11 07:07:08 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-11 07:07:35 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-11 07:06:10 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 08:00:56 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 08:01:09 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 07:04:21 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-11 07:05:26 | Hanwella (Kelani Ganga) | 4.86 | 🟢 Normal | 0.000 |  |
| 2026-11-11 07:06:44 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:01:43 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 07:03:38 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 08:02:02 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:39 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:02:26 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-11 08:01:04 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-11-11 08:01:21 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-11 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-11-11 07:06:56 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-11-11 08:00:28 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-11-11 07:08:24 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.036 |  |
| 2026-11-11 07:03:04 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.038 |  |
| 2026-11-11 07:04:19 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.040 |  |
| 2026-11-11 08:02:30 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.041 |  |
| 2026-11-11 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.045 |  |
| 2026-11-11 07:15:48 | Magura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.049 |  |
| 2026-11-11 07:18:18 | Moragaswewa (Deduru Oya) | 2.62 | 🟢 Normal | -0.056 |  |
| 2026-11-11 08:00:58 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.061 |  |
| 2026-11-11 07:06:57 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.065 |  |
| 2026-11-11 08:02:09 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.114 |  |
| 2026-11-11 07:04:37 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | -0.132 |  |
| 2026-11-11 07:08:01 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | -0.180 |  |
| 2026-11-11 08:03:11 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.232 |  |
| 2026-11-11 07:09:15 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.300 |  |
| 2026-11-11 07:04:34 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.316 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)