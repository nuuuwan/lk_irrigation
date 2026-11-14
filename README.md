# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_23:02:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,972 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 23:02:25 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:16 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:05 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:01 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:01:22 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:01:08 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 23:00:11 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:49:01 | Panadugama (Nilwala Ganga) | 5.13 | 🟡 Alert | -0.017 |  |
| 2026-11-14 22:45:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 22:06:48 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 22:49:01 | Panadugama (Nilwala Ganga) | 5.13 | 🟡 Alert | -0.017 |  |
| 2026-11-14 22:01:40 | Wellawaya (Kirindi Oya) | 1.82 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-14 22:03:07 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-14 22:02:25 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 22:03:13 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 23:01:08 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 23:02:05 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:16 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:02:05 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:02:05 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:01:30 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:25 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:00:11 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:01:22 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:01 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:10:54 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:04:08 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:08:44 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:11:26 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-11-14 22:06:21 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-11-14 22:05:56 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-14 22:05:09 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-14 22:00:53 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-11-14 22:18:29 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.016 |  |
| 2026-11-14 22:05:40 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-11-14 22:02:46 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-11-14 22:02:23 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-11-14 22:03:31 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.020 |  |
| 2026-11-14 22:04:38 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-11-14 22:00:50 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.032 |  |
| 2026-11-14 22:14:28 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.033 |  |
| 2026-11-14 22:45:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.035 |  |
| 2026-11-14 22:05:54 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.041 |  |
| 2026-11-14 22:09:12 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)