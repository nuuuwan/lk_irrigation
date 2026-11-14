# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_20:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,862 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 20:03:06 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:02:43 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-14 20:02:34 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:02:29 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-14 20:02:19 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-14 20:02:06 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:01:47 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.032 |  |
| 2026-11-14 20:01:46 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:01:33 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-14 20:01:31 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:01:19 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:17:14 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.017 |  |
| 2026-11-14 19:11:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.086 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 19:03:24 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 19:02:28 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.031 |  |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 19:03:42 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-14 20:01:46 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:03:46 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:04:17 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:03:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:02:34 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:10:40 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:03:06 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:02:38 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:02:55 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:01:19 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:03:08 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:02:06 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:00:16 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:05:52 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-14 19:06:53 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.009 |  |
| 2026-11-14 20:01:33 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-14 20:02:19 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-14 19:01:13 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-11-14 19:01:20 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-11-14 20:02:29 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-14 19:17:14 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.017 |  |
| 2026-11-14 19:07:08 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.018 |  |
| 2026-11-14 19:11:19 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.018 |  |
| 2026-11-14 20:02:43 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-14 19:03:40 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-11-14 19:01:18 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-11-14 20:01:47 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.032 |  |
| 2026-11-14 19:06:31 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2026-11-14 19:04:00 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.041 |  |
| 2026-11-14 19:08:46 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.045 |  |
| 2026-11-14 19:11:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.086 |  |
| 2026-11-14 19:04:31 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)