# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_04:29:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,749 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 04:29:13 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:21:07 | Panadugama (Nilwala Ganga) | 4.91 | 🟢 Normal | -0.031 |  |
| 2026-10-20 04:13:34 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.025 |  |
| 2026-10-20 04:11:11 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:10:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:07:26 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-20 04:05:59 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:05:34 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.022 |  |
| 2026-10-20 04:05:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:05:15 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-20 04:04:48 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:04:23 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-20 04:03:40 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.023 |  |
| 2026-10-20 04:03:32 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-20 04:03:29 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-10-20 04:02:58 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:02:41 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-20 04:02:38 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-20 04:02:34 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.064 |  |
| 2026-10-20 04:02:10 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-20 04:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-20 04:02:05 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 04:02:01 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-20 04:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.024 |  |
| 2026-10-20 04:01:38 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.031 |  |
| 2026-10-20 04:01:37 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-10-20 04:01:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-10-20 04:01:25 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-20 04:01:11 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 04:00:34 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-20 04:00:25 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.070 |  |
| 2026-10-20 04:00:18 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.227 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 04:00:34 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-20 04:00:18 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-20 04:05:15 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-20 04:02:01 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-20 04:01:25 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-20 04:02:41 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-20 04:07:26 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-20 04:02:10 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-20 04:02:05 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 04:01:11 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 03:09:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:01:39 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:11:51 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:04:48 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:07:57 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:10:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:02:58 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:05:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:29:13 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:05:59 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:11:11 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 04:04:23 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-20 04:01:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-10-20 04:03:32 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-20 04:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-20 04:02:38 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-20 04:01:37 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-10-20 04:05:34 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.022 |  |
| 2026-10-20 04:03:40 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.023 |  |
| 2026-10-20 04:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.024 |  |
| 2026-10-20 04:13:34 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.025 |  |
| 2026-10-20 04:21:07 | Panadugama (Nilwala Ganga) | 4.91 | 🟢 Normal | -0.031 |  |
| 2026-10-20 04:01:38 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.031 |  |
| 2026-10-20 04:03:29 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-10-20 04:02:34 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.064 |  |
| 2026-10-20 04:00:25 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.070 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)